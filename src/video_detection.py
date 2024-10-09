import cv2
from image_detection import Detect

class Video:

    def videodetection(self,video_input:int = 0):
        video = cv2.VideoCapture(video_input)

        while video.isOpened():
            ret,frame = video.read()
            if not ret:
                print("failed")
            image = Detect().image_detection(image_path=frame,video_input=True)
            cv2.imshow("video",image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    Video().videodetection()