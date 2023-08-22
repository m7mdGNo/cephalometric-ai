from .utils import get_middle
# import cv2

def detect_landmarks(frame, model,imgsz=800,conf=0.01,iou=0.07):
    names = {
            0: 'S',1: 'Go',2: 'L1',3: 'U1',4: 'ULA',
            5: 'LLA',6: 'SN',7: 'GN`',8: 'PNS',9: 'ANS',
            10: 'Ar',11: 'N',12: 'Or',13: 'Po',14: 'A',
            15: 'B',16: 'Pg',17: 'Mb',18: 'Gn'
            }
    results = model(frame,conf=conf,iou=iou, verbose=False,imgsz=imgsz)
    points = {}
    landmarks = {}
    for result in results[0]:
        classes = result.boxes.cls.tolist()
        bboxs = result.boxes.xyxy.tolist()     
        scores = result.boxes.conf.tolist()   
        for i, bbox in enumerate(bboxs):
            index = int(classes[i])
            class_name = names[index]
            score = scores[i]
            x1, y1, x2, y2 = [int(p) for p in bbox]

            #check if class in points and if it's score is better save it
            if class_name in points:
                if points[class_name][1] < score:
                    points[class_name] = [get_middle(x1, y1, x2 - x1, y2 - y1),score]
            else:
                points[class_name] = [get_middle(x1, y1, x2 - x1, y2 - y1),score]
    # save only point coords in landmarks dict
    for key,value in points.items():
        landmarks[key] = value[0]
    
    return landmarks

def detect_landmarks_roboflow(img,model,imgsz,conf=1,overlap=7):
    names = {
            1: 'S',10: 'Go',11: 'L1',12: 'U1',13: 'ULA',
            14: 'LLA',15: 'SN',16: 'GN`',17: 'PNS',18: 'ANS',
            19: 'Ar',2: 'N',3: 'Or',4: 'Po',5: 'A',
            6: 'B',7: 'Pg',8: 'Mb',9: 'Gn'
            }
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # img = cv2.resize(img,(imgsz,imgsz))
    results = model.predict(img, confidence=1,overlap=7).json()
    points = {}
    landmarks = {}
    for pred in results['predictions']:
        x = int(pred['x'])
        y = int(pred['y'])
        class_name = names[int(pred['class'])]
        conf = pred['confidence']
        if class_name in points:
            if points[class_name][1] < conf:
                points[class_name] = [(x,y),conf]
        else:
            points[class_name] = [(x,y),conf]
    # save only point coords in landmarks dict
    for key,value in points.items():
        landmarks[key] = value[0]
    
    return landmarks