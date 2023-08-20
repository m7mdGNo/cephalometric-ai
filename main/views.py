import csv
import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import generic
from ultralytics import YOLO
import numpy as np
import cv2
from ai_model.extract import extract_ANB,extract_SNA,extract_SNB
from ai_model.detect import detect_landmarks
from ai_model.utils import draw_circle
import base64
from docx import Document
import docx

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'


class UploatView(generic.TemplateView):
    template_name = 'upload.html'


def get_analytics(img,model):
    h,w,_=img.shape
    imgsz = 800
    img = cv2.resize(img,(imgsz,imgsz))

    points = detect_landmarks(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),model,imgsz=imgsz,conf=0.01,iou=0.07)

    for key,value in points.items():
        img = draw_circle(img,value,(0,255,0))
        cv2.putText(img,key,(value[0]+5,value[1]+5),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

    analytics = {}

    anb_ret,anb_angle = extract_ANB(img,points)
    if anb_ret:
        cv2.putText(img,f'ANB: {anb_angle}',(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
        analytics['ANB'] = f'{round(anb_angle,2)}°'
    snb_ret,snb_angle = extract_SNB(img,points)
    if snb_ret:
        cv2.putText(img,f'SNB: {snb_angle}',(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
        analytics['SNB'] = f'{round(snb_angle,2)}°'
    sna_ret,sna_angle = extract_SNA(img,points)
    if sna_ret:
        cv2.putText(img,f'SNA: {sna_angle}',(10,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
        analytics['SNA'] = f'{round(sna_angle,2)}°'

    img = cv2.resize(img,(w,h))
    return img,analytics

model = YOLO('ai_model/weights/best.pt')

class AnalysisView(generic.View):

    def post(self, request):
        global model
        img = request.FILES['image']
        img = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        img, analytics = get_analytics(img, model)
        _, img_encoded = cv2.imencode('.jpg', img)
        img_bytes = img_encoded.tobytes()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')  # Encode bytes as base64 string


        request.session['analysis'] = analytics
        request.session['image'] = img_base64

        response_data = {
            'image': img_base64,
        }
        return JsonResponse(response_data)


class DownloadReportView(generic.View):
    def get(self, request):
        # Get the stored image and analytics data from the session
        img_base64 = request.session.get('image')
        analytics = request.session.get('analysis')

        # Decode the base64 image data
        img_bytes = base64.b64decode(img_base64)

        # Create a new Word document
        doc = Document()
        
        # Add the image to the document
        img_io = io.BytesIO(img_bytes)
        doc.add_picture(img_io, width=docx.shared.Inches(6))  # Adjust the width as needed

        # Add a section break and analytics data
        # doc.add_section()  # Add a section break
        # doc.add_heading('Analytics', level=1)
        for key, value in analytics.items():
            doc.add_paragraph(f'{key}: {value}')

        # Create a response with the Word document content
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="analysis_report.docx"'

        # Save the document to the response
        doc.save(response)

        return response