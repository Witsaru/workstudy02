import cv2
import mediapipe as mp
import math


class poseDetector():

    # static_image_mode = False,
    # model_complexity = 1,
    # smooth_landmarks = True,
    # enable_segmentation = False,
    # smooth_segmentation = True,
    # min_detection_confidence = 0.5,
    # min_tracking_confidence = 0.5)

    def __init__(self, mode=False, model = 1, smooth=True,
                 enable_seg = False, smosegment = True,
                 detectionCon=0.7, trackCon=0.7):

        self.mode = mode
        self.model = model
        self.smooth = smooth
        self.enable_seg = enable_seg
        self.smosegment = smosegment
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.model, self.smooth,
                                     self.enable_seg, self.smosegment,
                                     self.detectionCon, self.trackCon)
        # self.pose = self.mpPose.Pose()

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw=True):

        # Get the landmarks
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        # Calculate the Angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360

        # print(angle)

        # Draw
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (51, 255, 51), cv2.FILLED)
            #cv2.circle(img, (x1, y1), 15, (153, 0, 0), 2)
            cv2.circle(img, (x2, y2), 10, (51, 255, 51), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (153, 0, 0), 2)
            cv2.circle(img, (x3, y3), 10, (51, 255, 51), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (153, 0, 0), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (51, 0, 0), 2)
        return angle
    
class handDetector():

    # static_image_mode = False,
    # model_complexity = 1,
    # smooth_landmarks = True,
    # enable_segmentation = False,
    # smooth_segmentation = True,
    # min_detection_confidence = 0.5,
    # min_tracking_confidence = 0.5)

    def __init__(self,mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

    def process_frame(self,frame, draw=True):
        # Convert the frame to RGB (MediaPipe uses RGB images)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = self.hands.process(frame_rgb)

        # Check if hands were detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the frame
                if draw:
                    self.mp_drawing.draw_landmarks(
                        frame, 
                        hand_landmarks, 
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        )

        return frame

if __name__ == "__main__":

    # OpenCV video capture setup
    cap = cv2.VideoCapture(0)  # Adjust the argument for your camera
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)

    deterhand = handDetector()
    deterpos = poseDetector()

    # Infinite loop to process video frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame
        deterhand.process_frame(frame)
        # deterpos.findPose(frame)


        # Display the processed frame
        cv2.imshow('Hand Landmarks', frame)
        # print(cap.get(cv2.CAP_PROP_FPS))

        # Break the loop when 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Release video capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

        
