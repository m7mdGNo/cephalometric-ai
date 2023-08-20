from .utils import get_middle

def detect_landmarks(frame, model,imgsz=800,conf=0.01,iou=0.07):
    names = {
            0: 'S',1: 'Go',2: 'L1',3: 'U1',4: 'ULA',
            5: 'LLA',6: 'SN',7: 'GN`',8: 'PNS',9: 'ANS',
            10: 'Ba',11: 'N',12: 'Or',13: 'Po',14: 'A',
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