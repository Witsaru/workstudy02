import cv2
import mediapipe as mp
import numpy as np

class holistic_module():
    """
    static_image_mode
    If set to false, the solution treats the input images as a video stream. It will try to detect the most prominent person in the very first images, and upon a successful detection further localizes the pose and other landmarks. In subsequent images, it then simply tracks those landmarks without invoking another detection until it loses track, on reducing computation and latency. If set to true, person detection runs every input image, ideal for processing a batch of static, possibly unrelated, images. Default to false.
    
    model_complexity
    Complexity of the pose landmark model: 0, 1 or 2. Landmark accuracy as well as inference latency generally go up with the model complexity. Default to 1.
    
    smooth_landmarks
    If set to true, the solution filters pose landmarks across different input images to reduce jitter, but ignored if static_image_mode is also set to true. Default to true.
    
    enable_segmentation
    If set to true, in addition to the pose, face and hand landmarks the solution also generates the segmentation mask. Default to false.
    
    smooth_segmentation
    If set to true, the solution filters segmentation masks across different input images to reduce jitter. Ignored if enable_segmentation is false or static_image_mode is true. Default to true.
    
    refine_face_landmarks
    Whether to further refine the landmark coordinates around the eyes and lips, and output additional landmarks around the irises. Default to false.
    
    min_detection_confidence
    Minimum confidence value ([0.0, 1.0]) from the person-detection model for the detection to be considered successful. Default to 0.5.
    
    min_tracking_confidence
    Minimum confidence value ([0.0, 1.0]) from the landmark-tracking model for the pose landmarks to be considered tracked successfully, or otherwise person detection will be invoked automatically on the next input image. Setting it to a higher value can increase robustness of the solution, at the expense of a higher latency. Ignored if static_image_mode is true, where person detection simply runs on every image. Default to 0.5.
    """

    def __init__(self):

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic(
            static_image_mode = False,
            model_complexity = 1,
            enable_segmentation = False,
            min_detection_confidence = 0.6,
            min_tracking_confidence = 0.6
        )

        self.frame_count = 0
        self.frame_skip = 3

        self.BG_COLOR = (192, 192, 192)

        self.memory_pose = {}

    def show_action(self, image, draw=True, face = False):
        self.frame_count += 1
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_np = np.array(imgRGB)
        image_np.flags.writeable = True
        self.results = self.holistic.process(imgRGB)
            # image.flags.writeable = True

        if not face:
            if draw:

                self.mp_drawing.draw_landmarks(
                    image,
                    self.results.pose_landmarks,
                    self.mp_holistic.POSE_CONNECTIONS,
                    landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style()
                    )
        
        else:
            if draw:
                
                self.mp_drawing.draw_landmarks(
                        image,
                        self.results.face_landmarks,
                        self.mp_holistic.FACEMESH_TESSELATION,
                        landmark_drawing_spec = None,
                        connection_drawing_spec=self.mp_drawing_styles.get_default_face_mesh_tesselation_style()
                        )
                
                self.mp_drawing.draw_landmarks(
                    image,
                    self.results.face_landmarks,
                    self.mp_holistic.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=self.mp_drawing_styles.get_default_face_mesh_contours_style())
                
                # self.mp_drawing.draw_landmarks(
                #     image,
                #     self.results.face_landmarks,
                #     self.mp_holistic.FACEMESH_IRISES,
                #     landmark_drawing_spec=None,
                #     connection_drawing_spec=self.mp_drawing_styles.get_default_face_mesh_iris_connections_style()
                #     )



        return image
     
    def segmentation_mask_(self,image):
        annotated_image = image.copy()
        # Draw segmentation on the image.
        # To improve segmentation around boundaries, consider applying a joint
        # bilateral filter to "results.segmentation_mask" with "image".
        condition = np.stack((self.results.segmentation_mask,) * 3, axis=-1)
        bg_image = np.zeros(image.shape, dtype=np.uint8)
        bg_image[:] = self.BG_COLOR
        annotated_image = np.where(condition, annotated_image, bg_image)

        return annotated_image

    def finepos(self, image):
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = image.shape

                cx, cy = int(lm.x * w), int(lm.y * h)
                self.memory_pose[id] = (cx,cy)
            # print(type(enumerate(self.results.pose_landmarks.landmark)), type(self.poslist))
            # print(list(enumerate(self.results.pose_landmarks.landmark)))
            # print(type(self.results.pose_landmarks.landmark))
        else:
            self.memory_pose = {}

        return self.memory_pose

    def finehand(self, image):
        self.handleft_list = []
        self.handright_list = []
        if self.frame_count % self.frame_skip == 0:
            if self.results.left_hand_landmarks:
                # print(self.results.right_hand_landmarks.landmark)
                for x in enumerate(self.results.left_hand_landmarks.landmark):
                    h, w, c = image.shape
                    id, lm = x
                    # print(id)

                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.handleft_list.append([id, cx, cy])
            if self.results.right_hand_landmarks:
                for y in enumerate(self.results.right_hand_landmarks.landmark):
                    # print(y)
                    h, w, c = image.shape
                    id, lm = y

                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.handright_list.append([id, cx, cy])
                    # print(lm)

        return self.handleft_list, self.handright_list
    
    def hands_online(self):
        if self.results.left_hand_landmarks and self.results.right_hand_landmarks:
            # print(len(self.handleft_list),len(self.handright_list))
            if len(self.handleft_list) > 0 and len(self.handright_list) > 0:
                return True

if __name__ == '__main__':
    from timeit import default_timer as timer

    cap = cv2.VideoCapture(2)
    # cap1 = cv2.VideoCapture('Video/Workstudy_Test_Top_2.mp4')
    # cap2 = cv2.VideoCapture('Video/Workstudy_Test_Side.mp4')
    holistic = holistic_module()
    start = timer()
    # cap.set(cv2.CAP_PROP_FPS,180)
    # cap2.set(cv2.CAP_PROP_FPS,180)

    while cap.isOpened():

        success, image = cap.read()
        holistic.show_action(image, face=True)

        if not success:
            print('Ignoring empty camera frame.')

            break


        cv2.imshow("Top", cv2.flip(image, 1))
        # cv2.imshow("Side", cv2.flip(image2, 1))

        if cv2.waitKey(5) & 0xFF == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    end = timer()
    print(end - start)
