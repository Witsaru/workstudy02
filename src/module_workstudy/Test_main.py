import HolisticModule as hm
import AssemblePats as ap
import draw_pose as dp
import Motion as M
import utils as u
# import gui

import cv2
from timeit import default_timer as timer
import time
import pandas as pd
import numpy as np
import threading

aruco_marker_memory = {}
poes_memory = {}

set_shoulder = []

r_pack_move_id0_1 = []
r_pack_move_id1_2 = []
r_pack_move_id4_3 = []
r_pack_move_id5_4 = []
r_pack_move_id6_5 = []

count_step = 0
step_one_zero = 0

point_h_r_x = []
point_h_r_y = []
point_h_l_x = []
point_h_l_y = []

# class GuiThread(threading.Thread):
#     def run(self):
#         gui_=gui.GUI_study()
#         gui_.Flow_process_ui()


def Recap(cap):
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,800)

def Bootfpss(cap):
    cap.set(cv2.CAP_PROP_FPS,5)

def Thra(cap):
    cap.set(cv2.CAP_PROP_N_THREADS, 12)

def Text(image, num, posx, posy):
    cv2.putText(image, str(int(num)), (posx, posy), cv2.FONT_HERSHEY_PLAIN, 1,
                (102,102,255), 2)
              
def memory_aruco(ids_num, image):
    if ids_num not in aruco_marker_memory:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict)
        list_posAruco = u.aruco_display(corners,ids, 17,image)
        for market_id, cX, cY in list_posAruco:
            # print(ids)
            if market_id == ids_num:
                aruco_marker_memory[ids_num] = (cX, cY)
                return aruco_marker_memory[ids_num]
    else:
        return aruco_marker_memory[ids_num]
    
def memory_pose(ids_list):
    for ids, cX, cY in ids_list :
        poes_memory[ids] = (cX, cY)
    
    return poes_memory
    
def cal_dits(point, id_point):

    if id_point is not None:
        dits = ap.findDistance(point, id_point)
        # Text(image, dits, id_point[0], id_point[1])
        return dits
    else:
        pass


aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)

# gui_threa = GuiThread()
# gui_threa.start()

selet = int(input('1: wedcam 2: video : '))

if selet == 1:
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(2)
elif selet == 2:
    cap1 = cv2.VideoCapture('Video/test_workstudy_top.avi')
    cap2 = cv2.VideoCapture('Video/test_workstudy_side.avi')

if selet == 1:
    Recap(cap1)
    Recap(cap2)
    # Bootfpss(cap1)
    # Bootfpss(cap2)
    Thra(cap1)
    Thra(cap2)
elif selet == 2:
    pass

print(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT),cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap1.get(cv2.CAP_PROP_N_THREADS
print(cap1.get(cv2.CAP_PROP_FPS))

frame_fps = cap1.get(cv2.CAP_PROP_FPS)
frame_count = cap1.get(cv2.CAP_PROP_FRAME_COUNT)
print(f"video time : {frame_count/frame_fps}")
video_time = frame_count/frame_fps
print(cv2.__version__)
holistic = hm.holistic_module()
motion = M.Motion_time(7,7,8)

ffcc99 = (153, 204, 255)
ccff99 = (153,255,204)

step_l = 0
step_r = 0

pTime = 0

start = timer()

time_s_assm_l = 0
time_e_assm_l = 0
time_s_mov_l = 0
time_e_mov_l = 0

time_s_assm_r = 0
time_e_assm_r = 0
time_s_mov_r = 0
time_e_mov_r = 0

l_assemble_min = (120, 115, 250)
l_assemble_max = (155, 145, 285)
l_move_min = (150, 125, 185)
l_move_max = (180, 180, 215)

r_assemble_min = (110, 120, 70)
r_assemble_max = (155, 145, 105)
r_move_min = (155, 125, 135)
r_move_max = (180, 180, 175)

deter = True

mode = 0

paused = False

time_ = 0

average_shoulder_width_cm = 44.4
hypothetical_pixel_width = 200
pixels_per_cm = hypothetical_pixel_width / average_shoulder_width_cm

if deter:
    mode = int(input("1: Top 2: Side: "))


# if selet == 1:
#     out1 = cv2.VideoWriter('/home/witsarut/workstudy_ws/src/Video/test_workstudy_top.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (800,600))
#     out2 = cv2.VideoWriter('/home/witsarut/workstudy_ws/src/Video/test_workstudy_side.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (800,600))

while cap1.isOpened():

    if not paused:

        success1, image = cap1.read()
        success2, image2 = cap2.read()

        if not success1:
            print('Ignoring empty camera frame.')

            break
    # success1, image = cap1.read()
    # success2, image2 = cap2.read()

    # if selet == 1:
    #     out1.write(image.copy())
    #     out2.write(image2.copy())

    # if not success1:
    #         print('Ignoring empty camera frame.')

    #         break

    # print(paused)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    id_0 = u.memory_aruco(0, image, aruco_dict)
    id_1 = u.memory_aruco(1, image, aruco_dict)
    id_2 = u.memory_aruco(2, image, aruco_dict)
    id_3 = u.memory_aruco(3, image, aruco_dict)
    id_4 = u.memory_aruco(4, image, aruco_dict)
    id_5 = u.memory_aruco(5, image, aruco_dict)
    id_6 = u.memory_aruco(6, image, aruco_dict)
    # print(id_2)

    id_10 = u.memory_aruco(10, image, aruco_dict)
    id_11 = u.memory_aruco(11, image, aruco_dict)
    id_12 = u.memory_aruco(12, image, aruco_dict)
    id_13 = u.memory_aruco(13, image, aruco_dict)
    id_14 = u.memory_aruco(14, image, aruco_dict)
    id_15 = u.memory_aruco(15, image, aruco_dict)
    id_16 = u.memory_aruco(16, image, aruco_dict)

    if deter and not paused:

        if mode == 1:
            holistic.show_action(image, draw=True)
            # image_mask = holistic.segmentation_mask_(image)
            # holistic.show_action(image2, draw=True)

        elif mode == 2:
            holistic.show_action(image2, draw=True)

        list_pose = holistic.finepos(image)
        list_hands = holistic.finehand(image)

        if len(list_pose) > 0:

            r_shoulder = list_pose[12]
            l_shoulder = list_pose[11]

            r_elbow = list_pose[14]
            r_wrist = list_pose[16]

            l_elbow = list_pose[13]
            l_wrist = list_pose[15]

            r_index = list_pose[19]
            l_index = list_pose[20]
            # print(f"l_shoulder: {l_shoulder}  r_shoulder: {r_shoulder}")
            # print(image[5])


            # listener = keyboard.Listener(on_release=action_move)
            # listener.start()

            if mode == 1 :


                drawPose = dp.DrawPose(image, list_pose)

                sho_90_ = ap.findAngle(r_shoulder, l_shoulder)

                A_arm_r = ap.findAngle(r_elbow,r_wrist)
                A_arm_l = ap.findAngle(l_elbow,l_wrist)

                A_shr_l = ap.findAngle(l_shoulder,l_elbow)
                A_shr_r = ap.findAngle(r_shoulder,r_elbow)

                A_elbow_l = ap.findAngle_elbow(l_shoulder, l_elbow, l_wrist)
                A_elbow_r = ap.findAngle_elbow(r_shoulder, r_elbow, r_wrist)

                tp = ap.findAngle(r_shoulder,r_wrist)

                d_s_e_r = ap.findDistance(r_shoulder,r_elbow)
                d_e_w_r = ap.findDistance(r_shoulder, r_index)

                d_s_e_l = ap.findDistance(l_shoulder,l_elbow)
                d_e_w_l = ap.findDistance(l_shoulder, l_index)

                pixel_distance_shoulders = abs(r_shoulder[0] - l_shoulder[0])
                distance_shoulders_cm = pixel_distance_shoulders / pixels_per_cm

                # print(sho_90_)

                if distance_shoulders_cm >= 38 and len(set_shoulder) == 0:
                    if sho_90_ == 90:
                        set_shoulder.append(r_shoulder)
                        set_shoulder.append(l_shoulder)
                    # print(set_shoulder[0])


                if len(set_shoulder) > 0:
                    cv2.circle(image, set_shoulder[0], int(44.2 * pixels_per_cm), (0,255,0), 3)
                    cv2.circle(image, set_shoulder[0], int(72.1 * pixels_per_cm), (0,0,255), 3)

                    cv2.circle(image, set_shoulder[1], int(44.2 * pixels_per_cm), (0,255,0), 3)
                    cv2.circle(image, set_shoulder[1], int(72.1 * pixels_per_cm), (0,0,255), 3)
                    point_h_r_x.append(r_wrist[0])
                    point_h_r_y.append(r_wrist[1])
                    point_h_l_x.append(l_wrist[0])
                    point_h_l_y.append(l_wrist[1])

                # print(180-tp) 


                distan_id_0 = cal_dits(l_wrist, id_0)
                distan_id_1 = cal_dits(l_wrist, id_1)
                distan_id_2 = cal_dits(l_wrist, id_2)
                distan_id_3 = cal_dits(l_wrist, id_3)
                distan_id_4 = cal_dits(l_wrist, id_4)
                distan_id_5 = cal_dits(l_wrist, id_5)
                distan_id_6 = cal_dits(l_wrist, id_6)

                distan_id_10 = cal_dits(r_wrist, id_10)
                distan_id_11 = cal_dits(r_wrist, id_11)
                distan_id_12 = cal_dits(r_wrist, id_12)
                distan_id_13 = cal_dits(r_wrist, id_13)
                distan_id_14 = cal_dits(r_wrist, id_14)
                distan_id_15 = cal_dits(r_wrist, id_15)
                distan_id_16 = cal_dits(r_wrist, id_16)
                
                time_ = motion.move_action_r(A_shr_r,A_elbow_r,A_arm_r,[distan_id_10, distan_id_11, distan_id_14, distan_id_16, distan_id_15])
                time_2 = motion.move_action_l(A_shr_l,A_elbow_l,A_arm_l,[distan_id_0, distan_id_1, distan_id_4, distan_id_6, distan_id_5])
                product = motion.count_product()

                # action_move()

                # distan_id_10 = ap.findDistance(l_wrist, id_10)
                # distan_id_11 = ap.findDistance(l_wrist, id_11)
                # distan_id_12 = ap.findDistance(l_wrist, id_12)
                # distan_id_16 = ap.findDistance(l_wrist, id_16)

                drawPose.draw_top_pos()

                # Text(image, motion.count_process(), 200, 200)

                # Text(image, A_shr_r, r_shoulder[0], r_shoulder[1])
                # Text(image, A_elbow_r, r_elbow[0], r_elbow[1])
                # Text(image, A_arm_r, r_wrist[0], r_wrist[1])

                # Text(image, A_shr_l, l_shoulder[0], l_shoulder[1])
                # Text(image, A_elbow_l, l_elbow[0], l_elbow[1])
                # Text(image, A_arm_l, l_wrist[0], l_wrist[1])

                Text(image, distance_shoulders_cm, l_shoulder[0] - (pixel_distance_shoulders // 2), l_shoulder[1] - 20)
            elif mode == 2:
                l_shoulder = list_pose[11]
                l_hip = list_pose[23]
                l_ear = list_pose[7]

                r_shoulder = list_pose[12]
                r_hip = list_pose[24]
                r_ear = list_pose[8]

                neck = ap.findAngle(r_shoulder,r_ear)
                torso = ap.findAngle(r_hip,r_shoulder)

                posture = motion.body_posture_detection(neck, torso)

                drawPose = dp.DrawPose(image2, list_pose)
                drawPose.draw_side_pos(image2,detection= posture, rad_circle= 5, size_line= 2)
                time_poon = motion.poor_body(posture, neck, torso)
                # print(time_poon)

            # print(f'angle_l: {A_arm_l} angle_r: {- (A_arm_r - 180)}')
            # print(f'arm_l:{A_arm_l},{A_shr_l},{A_elbow_l} arm_r:{A_arm_r},{A_shr_r},{A_elbow_r}')
            # print(f'arm_l:{action_l} arm_r:{action_r}')


    # cv2.putText(image, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    #             (255, 0, 0), 3)
    # cv2.putText(image, str(motion.count_process_l()), (200, 200), cv2.FONT_HERSHEY_PLAIN, 3,
    #             (255, 0, 0), 3)

    # out1.write(image)
    # out2.write(image2)

    cv2.imshow("Top", image)
    # cv2.imshow("mark", image_mask)
    cv2.imshow("Side", image2)

    if cv2.waitKey(5) & 0xFF == 27:
        paused = not paused

    # if cv2.waitKey(1) == ord('q'):
        # paused = not paused

    # elif cv2.waitKey(5) & 0xFF == ord("s"):
    #     if step_one_zero == 0:
    #         if count_step == 0:
    #             r_pack_move_id0_1.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_0])
    #             print("Save Done! id 0")
    #             count_step +=1
    #             step_one_zero = 1

    #         elif count_step == 1:
    #             r_pack_move_id1_2.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_1])
    #             print("Save Done! id 1")
    #             count_step +=1
    #             step_one_zero = 1

    #         elif count_step == 2:
    #             r_pack_move_id4_3.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_4])
    #             print("Save Done! id 4")
    #             count_step +=1
    #             step_one_zero = 1
                        
    #         elif count_step == 3:
    #             r_pack_move_id6_5.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_6])
    #             print("Save Done! id 6")
    #             count_step +=1

    #         if count_step >= 4:
    #             count_step = 0
                    
    #         elif step_one_zero == 1:
    #             r_pack_move_id5_4.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_5])
    #             print("Save Done! id 5")
    #             step_one_zero = 0
        
cap1.release()
cap2.release()
cv2.destroyAllWindows()
end = timer()
print(end - start)

# print(f"Step1_l: {time_2['Step1']} Step1_r: {time_['Step1']}")
# print(f"Step2_l: {time_2['Step2']} Step2_r: {time_['Step2']}")
# print(f"Step3_l: {time_2['Step3']} Step3_r: {time_['Step3']}")
# print(f"Step4_l: {time_2['Step4']} Step4_r: {time_['Step4']}")
# print(f"Step5_l: {time_2['Step5']} Step5_r: {time_['Step5']}")
# print(f"Step6_l: {time_2['Step6']} Step6_r: {time_['Step6']}")
# print(f"Step7_l: {time_2['Step7']} Step7_r: {time_['Step7']}")
# print(f"num_product_l: {product[1]}  num_product_r: {product[0]}")

if mode == 1:
    index_l = []
    index_r = []

    product_r = product[0]
    product_l = product[1]

    for i in range(0,product_l):
        index_l.append(f"Round{i+1}")

    for i in range(0,product_r):
        index_r.append(f"Round{i+1}")

    df_r = pd.DataFrame(time_, index=index_r)
    df_l = pd.DataFrame(time_2, index=index_l)

    print(f"\nright:\n{df_r}\n")
    print(f"\nleft:\n{df_l}\n")

    print(f"set: {set_shoulder}\n")

    print(f"\npoint_h_l: {point_h_l_x}\n")
    print(f"\npoint_h_l: {point_h_l_y}\n")
    print(f"\npoint_h_r: {point_h_r_x}\n")
    print(f"\npoint_h_r: {point_h_r_y}\n")

else:
    myvar = pd.DataFrame(time_poon)
    print(myvar)
    # print(sum(time_poon[1::]))
    # print(time_poon)


aruco_marker_memory = {}
