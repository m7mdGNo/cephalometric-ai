# import cv2
# from .utils import calculate_angle

# def extract_ANB(img,points:dict):
#     try:
#         A = points['A']
#         N = points['N']
#         B = points['B']
#         cv2.line(img,A,N,(0,0,255),2)
#         cv2.line(img,N,B,(0,0,255),2)
#         predicted_angle = calculate_angle(line1=[N,A],line2=[N,B])
#         return True,round(predicted_angle,2)
#     except:
#         return False,'not detected'


# def extract_SNA(img,points:dict):
#     try:
#         S = points['S']
#         N = points['N']
#         A = points['A']
#         cv2.line(img,S,N,(0,0,255),2)
#         cv2.line(img,N,A,(0,0,255),2)
#         predicted_angle = calculate_angle(line1=[N,S],line2=[N,A])
#         return True,round(predicted_angle,2)
#     except:
#         return False,'not detected'

# def extract_SNB(img,points:dict):
#     try:
#         S = points['S']
#         N = points['N']
#         B = points['B']
#         cv2.line(img,S,N,(0,0,255),2)
#         cv2.line(img,N,B,(0,0,255),2)
#         predicted_angle = calculate_angle(line1=[N,S],line2=[N,B])
#         return True,round(predicted_angle,2)
#     except:
#         return False,'not detected'