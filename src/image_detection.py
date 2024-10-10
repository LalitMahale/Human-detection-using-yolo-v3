import os
import cv2
import numpy as np
from src.setting import YOLO_CFG,YOLO_WEIGHTS,COCO_FILE,OBJECT

class ImageDetect:
    def __init__(self) -> None:
        pass
    def image_detection(self,image_path= None,video_input:bool=None):
        """
        image_Path : By default None Provide image path for image detection.

        video_input : By  default None It will be bool (True and False) for video Access.
        
        """
        net = cv2.dnn.readNet(YOLO_WEIGHTS,YOLO_CFG)
        layer_names =net.getLayerNames()

        output_layer = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

        with open(COCO_FILE,"r") as f:
            classes = f.read().split("\n")
        if not video_input:
            try:
                image = cv2.imread(image_path)
            except :
                image = image_path
            image = cv2.resize(image, (600,400))
        else:
            image = image_path
        height, width = image.shape[:2]
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layer)    

        class_ids = []
        confidences = []
        boxes = []

        # Loop over each detection
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and classes[class_id] == "person":
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        # Apply non-max suppression to remove overlaps
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        #bounding boxes around detected humans
        for i in indices:
            x, y, w, h = boxes[i]
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return image

if __name__ == "__main__":

    img = Detect().image_detection("test_docs/image.jpg")
    cv2.imshow("test",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()