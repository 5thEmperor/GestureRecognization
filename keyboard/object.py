import cv2
import pixellib
from pixellib.instance import instance_segmentation

segment_image = instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5") 

camera = cv2.VideoCapture(0)

while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        break

    # Resize frame for faster processing
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    # Apply segmentation
    result = segment_image.segmentFrame(frame, show_bboxes=True)
    image = result[1]

    cv2.imshow('Image Segmentation', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
