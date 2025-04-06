"""
Testing to see if bounding box coordinates work given a trained YOLOv8 model on the dataset.
(they work, but the results don't (they really suck))
"""

from ultralytics import YOLO

model = YOLO("/home/its-joji/Documents/yolov8_synthetic_run/src/runs/detect/train6/weights/best.pt")

results = model("/home/its-joji/Documents/yolov8_synthetic_run/coco_data/images/val/000373.jpg")

for result in results:
    boxes = result.boxes
    for box in boxes:
        print(box.xyxy)
    result.show()
    result.save("result.jpg")