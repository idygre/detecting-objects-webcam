# App 2 - Detect motion on webcam
from datetime import datetime
import cv2
import time
import pandas


class VideoCamera(object):

    # df = pandas.DataFrame(columns=["Start", "End"])

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        # first_frame = None
        # status_list = [None, None]
        # times = []

        # while True:
        check, frame = self.video.read()
        check, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

        # status = 0
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # if first_frame is None:
        #     first_frame = gray
        #     continue

        # delta_frame = cv2.absdiff(first_frame, gray)
        # thresh_frame = cv2.threshold(
        #     delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        # # remove the black holes from a white area to smooth threshold frame
        # thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

        # # contours of area
        # (cnts, _) = cv2.findContours(thresh_frame.copy(),
        #                              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # for contour in cnts:
        #     if cv2.contourArea(contour) < 10500:
        #         continue
        #     status = 1

        #     (x, y, w, h) = cv2.boundingRect(contour)
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        # status_list.append(status)

        # status_list = status_list[-2:]

        # if status_list[-1] == 1 and status_list[-2] == 0:
        #     times.append(datetime.now())
        # if status_list[-1] == 0 and status_list[-2] == 1:
        #     times.append(datetime.now())

        # cv2.imshow("Gray Frame", gray)
        # cv2.imshow("Delta frame", delta_frame)
        # cv2.imshow("Thresh frame", thresh_frame)
        #cv2.imshow("Color frame", frame)

        # key = cv2.waitKey(1)

        # if key == ord('q'):
        #     if status == 1:
        #         times.append(datetime.now())
        #     break

        # print(status_list)
        # print(times)
        # print(check)

        # for i in range(0, len(times), 2):
        #     df = df.append(
        #         {"Start": times[i], "End": times[i+1]}, ignore_index=True)

        # df.to_csv("Times.csv")

    # press 'q' to quit the window
   # cv2.destroyAllWindows()
