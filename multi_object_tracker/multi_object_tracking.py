import cv2 
from datetime import datetime


OPENCV_OBJECT_TRACKERS = {"csrt"      : cv2.legacy.TrackerCSRT_create,
		                  "kcf"       : cv2.legacy.TrackerKCF_create,
		                  "boosting"  : cv2.legacy.TrackerBoosting_create,
		                  "mil"       : cv2.legacy.TrackerMIL_create,
		                  "tld"       : cv2.legacy.TrackerTLD_create,
		                  "medianflow": cv2.legacy.TrackerMedianFlow_create,
		                  "mosse"     : cv2.legacy.TrackerMOSSE_create}

tracker_name = "csrt"

trackers = cv2.legacy.MultiTracker_create()

video_path = "MOT17-04-DPM.mp4"
cap = cv2.VideoCapture(0)

inference_time_y = 30
font_scale = 0.7
thickness = 2
fps = 30     
f = 0
text_x_align = 10
freq = cv2.getTickFrequency()
color_move_on = (255, 200, 90)
pred_shape = (480, 640, 3)
vis_shape = (800, 600)

while True:

    t1 = cv2.getTickCount()
    start = datetime.now()
    s = datetime.now()
    e = datetime.now()
    d = e - s
    inf_time = round(d.total_seconds(), 3)
    ret, frame = cap.read()
    out = frame.copy()
    (H, W) = frame.shape[:2]
    frame = cv2.resize(frame, dsize = (640, 480))
    
    (success , boxes) = trackers.update(frame)
    
    info = [("Tracker", tracker_name),
        	("Success", "Yes" if success else "No")]
    
    string_text = ""
    
    for (i, (k, v)) in enumerate(info):
        text = "{}: {}".format(k, v)
        string_text = string_text + text + " "

    #cv2.putText(frame, string_text, (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    for box in boxes:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    

    end = datetime.now()
    duration = end - start
    a_time = round(duration.total_seconds(), 3)

    inference_time = 'Inference Time: {}'.format(inf_time)
    label_size, base_line = cv2.getTextSize(inference_time, cv2.FONT_HERSHEY_SIMPLEX, font_scale,
                                            thickness)
    label_ymin = max(inference_time_y, label_size[1] + 10)
    cv2.rectangle(frame, (text_x_align, label_ymin - label_size[1] - 10),
                  (text_x_align + label_size[0], label_ymin + base_line - 10), (255, 255, 255),
                  cv2.FILLED)
    cv2.rectangle(frame, (text_x_align - 2, label_ymin - label_size[1] - 12),
                  (text_x_align + 2 + label_size[0], label_ymin + base_line - 8), (0, 0, 0))
    cv2.putText(frame, inference_time, (text_x_align, label_ymin - 7), cv2.FONT_HERSHEY_SIMPLEX,
                font_scale,
                color_move_on,
                thickness,
                cv2.LINE_AA)

    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("t"):
        
        box = cv2.selectROI("Frame", frame, fromCenter=False)
    
        tracker = OPENCV_OBJECT_TRACKERS[tracker_name]()
        trackers.add(tracker, frame, box)

    elif key == ord("q"):break

    f = f + 1
    
cap.release()
cv2.destroyAllWindows() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
