import HolisticModule as hm
import cv2

class DrawPose():
    def __init__(self, image, list_pose):
        self.image = image
        self.list_pose = list_pose
        # self.list_hands = list_hands

        self.ffcc99 = (153, 204, 255)
        self.ccff99 = (153,255,204)
        self.ffffff = (255, 255, 255)
        self.cc0000 = (0, 0, 204)
        self.ff9999 = (153, 153, 255)
        self._99ff99 = (153, 255, 153)
        self.ff6666 = (102, 102, 255)


    def draw_top_pos(self, size_line = 3, R_circle = 5):
        ffcc99 = (153, 204, 255)
        ccff99 = (153,255,204)
        
        if len(self.list_pose) > 0:
            r_shoulder = self.list_pose[12]
            l_shoulder = self.list_pose[11]

            r_elbow = self.list_pose[14]
            r_wrist = self.list_pose[16]

            l_elbow = self.list_pose[13]
            l_wrist = self.list_pose[15]

            cv2.line(self.image, (r_shoulder), (l_shoulder),(255,255,255),size_line)
            
            cv2.line(self.image, (r_shoulder), (r_elbow),(255,255,255),size_line)
            cv2.line(self.image, (l_shoulder), (l_elbow),(255,255,255),size_line)
            cv2.line(self.image, (r_elbow), (r_wrist),(255,255,255),size_line)
            cv2.line(self.image, (l_elbow), (l_wrist),(255,255,255),size_line)
            
            cv2.circle(self.image, (r_shoulder[0],r_shoulder[1]),R_circle,ffcc99,-1)
            cv2.circle(self.image, (l_shoulder[0],l_shoulder[1]),R_circle,ccff99,-1)


            cv2.circle(self.image, (r_elbow[0],r_elbow[1]),R_circle,ffcc99,-1)
            cv2.circle(self.image, (r_elbow[0],r_elbow[1] - 50),R_circle,ffcc99,-1)
            cv2.circle(self.image, (r_wrist[0],r_wrist[1]),R_circle,ffcc99,-1)

            cv2.circle(self.image, (l_elbow[0],l_elbow[1]),R_circle,ccff99,-1)
            cv2.circle(self.image, (l_elbow[0],l_elbow[1] - 50),R_circle,ccff99,-1)
            cv2.circle(self.image, (l_wrist[0],l_wrist[1]),R_circle,ccff99,-1)

            # print(f'L:{ap.findAngle(l_elbow,l_wrist)}, R:{ap.findAngle(r_elbow,r_wrist)}')

            # if len(self.list_hands[0]) > 0 and len(self.list_hands[1]) > 0:
            #     r_thumb_cmc = self.list_hands[1][1][1::]
            #     r_thumb_mcp = self.list_hands[1][2][1::]
            #     r_thumb_ip = self.list_hands[1][3][1::]
            #     r_thumb_tip = self.list_hands[1][4][1::]
                
            #     r_index_finger_mcp = self.list_hands[1][5][1::]
            #     r_index_finger_pip = self.list_hands[1][6][1::]
            #     r_index_finger_dip = self.list_hands[1][7][1::]
            #     r_index_finger_tip = self.list_hands[1][8][1::]
                
            #     r_middle_finger_mcp = self.list_hands[1][9][1::]
            #     r_middle_finger_pip = self.list_hands[1][10][1::]
            #     r_middle_finger_dip = self.list_hands[1][11][1::]
            #     r_middle_finger_tip = self.list_hands[1][12][1::]

            #     r_ring_finger_mcp = self.list_hands[1][13][1::]
            #     r_ring_finger_pip = self.list_hands[1][14][1::]
            #     r_ring_finger_dip = self.list_hands[1][15][1::]
            #     r_ring_finger_tip = self.list_hands[1][16][1::]

            #     r_pinky_mcp = self.list_hands[1][17][1::]
            #     r_pinky_pip = self.list_hands[1][18][1::]
            #     r_pinky_dip = self.list_hands[1][19][1::]
            #     r_pinky_tip = self.list_hands[1][20][1::]

            #     l_thumb_cmc = self.list_hands[0][1][1::]
            #     l_thumb_mcp = self.list_hands[0][2][1::]
            #     l_thumb_ip = self.list_hands[0][3][1::]
            #     l_thumb_tip = self.list_hands[0][4][1::]
                
            #     l_index_finger_mcp = self.list_hands[0][5][1::]
            #     l_index_finger_pip = self.list_hands[0][6][1::]
            #     l_index_finger_dip = self.list_hands[0][7][1::]
            #     l_index_finger_tip = self.list_hands[0][8][1::]
                
            #     l_middle_finger_mcp = self.list_hands[0][9][1::]
            #     l_middle_finger_pip = self.list_hands[0][10][1::]
            #     l_middle_finger_dip = self.list_hands[0][11][1::]
            #     l_middle_finger_tip = self.list_hands[0][12][1::]

            #     l_ring_finger_mcp = self.list_hands[0][13][1::]
            #     l_ring_finger_pip = self.list_hands[0][14][1::]
            #     l_ring_finger_dip = self.list_hands[0][15][1::]
            #     l_ring_finger_tip = self.list_hands[0][16][1::]

            #     l_pinky_mcp = self.list_hands[0][17][1::]
            #     l_pinky_pip = self.list_hands[0][18][1::]
            #     l_pinky_dip = self.list_hands[0][19][1::]
            #     l_pinky_tip = self.list_hands[0][20][1::]

            #     cv2.circle(self.image, (r_thumb_cmc[0],r_thumb_cmc[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_thumb_mcp[0],r_thumb_mcp[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_thumb_ip[0],r_thumb_ip[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_thumb_tip[0],r_thumb_tip[1]),1,ffcc99,-1)

            #     cv2.circle(self.image, (r_index_finger_mcp[0],r_index_finger_mcp[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_index_finger_pip[0],r_index_finger_pip[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_index_finger_dip[0],r_index_finger_dip[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_index_finger_tip[0],r_index_finger_tip[1]),1,ffcc99,-1)

            #     cv2.circle(self.image, (r_middle_finger_mcp[0],r_middle_finger_mcp[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_middle_finger_pip[0],r_middle_finger_pip[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_middle_finger_dip[0],r_middle_finger_dip[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_middle_finger_tip[0],r_middle_finger_tip[1]),1,ffcc99,-1)

            #     cv2.circle(self.image, (r_ring_finger_mcp[0],r_ring_finger_mcp[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_ring_finger_pip[0],r_ring_finger_pip[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_ring_finger_dip[0],r_ring_finger_dip[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_ring_finger_tip[0],r_ring_finger_tip[1]),1,ffcc99,-1)

            #     cv2.circle(self.image, (r_pinky_mcp[0],r_pinky_mcp[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_pinky_pip[0],r_pinky_pip[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_pinky_dip[0],r_pinky_dip[1]),1,ffcc99,-1)
            #     cv2.circle(self.image, (r_pinky_tip[0],r_pinky_tip[1]),1,ffcc99,-1)

            #     cv2.circle(self.image, (l_thumb_cmc[0],l_thumb_cmc[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_thumb_mcp[0],l_thumb_mcp[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_thumb_ip[0],l_thumb_ip[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_thumb_tip[0],l_thumb_tip[1]),1,ccff99,-1)

            #     cv2.circle(self.image, (l_index_finger_mcp[0],l_index_finger_mcp[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_index_finger_pip[0],l_index_finger_pip[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_index_finger_dip[0],l_index_finger_dip[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_index_finger_tip[0],l_index_finger_tip[1]),1,ccff99,-1)

            #     cv2.circle(self.image, (l_middle_finger_mcp[0],l_middle_finger_mcp[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_middle_finger_pip[0],l_middle_finger_pip[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_middle_finger_dip[0],l_middle_finger_dip[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_middle_finger_tip[0],l_middle_finger_tip[1]),1,ccff99,-1)

            #     cv2.circle(self.image, (l_ring_finger_mcp[0],l_ring_finger_mcp[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_ring_finger_pip[0],l_ring_finger_pip[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_ring_finger_dip[0],l_ring_finger_dip[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_ring_finger_tip[0],l_ring_finger_tip[1]),1,ccff99,-1)

            #     cv2.circle(self.image, (l_pinky_mcp[0],l_pinky_mcp[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_pinky_pip[0],l_pinky_pip[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_pinky_dip[0],l_pinky_dip[1]),1,ccff99,-1)
            #     cv2.circle(self.image, (l_pinky_tip[0],l_pinky_tip[1]),1,ccff99,-1)

            #     cv2.line(self.image, (r_wrist), (r_thumb_cmc),(255,255,255),1)
            #     cv2.line(self.image, (r_thumb_cmc), (r_thumb_mcp),(255,255,255),1)
            #     cv2.line(self.image, (r_thumb_mcp), (r_thumb_ip),(255,255,255),1)
            #     cv2.line(self.image, (r_thumb_ip), (r_thumb_tip),(255,255,255),1)

            #     cv2.line(self.image, (r_wrist), (r_index_finger_mcp),(255,255,255),1)
            #     cv2.line(self.image, (r_index_finger_mcp), (r_index_finger_pip),(255,255,255),1)
            #     cv2.line(self.image, (r_index_finger_pip), (r_index_finger_dip),(255,255,255),1)
            #     cv2.line(self.image, (r_index_finger_dip), (r_index_finger_tip),(255,255,255),1)

            #     cv2.line(self.image, (r_index_finger_mcp), (r_middle_finger_mcp),(255,255,255),1)
                
            #     cv2.line(self.image, (r_middle_finger_mcp), (r_middle_finger_pip),(255,255,255),1)
            #     cv2.line(self.image, (r_middle_finger_pip), (r_middle_finger_dip),(255,255,255),1)
            #     cv2.line(self.image, (r_middle_finger_dip), (r_middle_finger_tip),(255,255,255),1)

            #     cv2.line(self.image, (r_middle_finger_mcp), (r_ring_finger_mcp),(255,255,255),1)
                
            #     cv2.line(self.image, (r_ring_finger_mcp), (r_ring_finger_pip),(255,255,255),1)
            #     cv2.line(self.image, (r_ring_finger_pip), (r_ring_finger_dip),(255,255,255),1)
            #     cv2.line(self.image, (r_ring_finger_dip), (r_ring_finger_tip),(255,255,255),1)

            #     cv2.line(self.image, (r_ring_finger_mcp), (r_pinky_mcp),(255,255,255),1)

            #     cv2.line(self.image, (r_pinky_mcp), (r_pinky_pip),(255,255,255),1)
            #     cv2.line(self.image, (r_pinky_pip), (r_pinky_dip),(255,255,255),1)
            #     cv2.line(self.image, (r_pinky_dip), (r_pinky_tip),(255,255,255),1)

            #     cv2.line(self.image, (r_wrist), (r_pinky_mcp),(255,255,255),1)##

            #     cv2.line(self.image, (l_wrist), (l_thumb_cmc),(255,255,255),1)
            #     cv2.line(self.image, (l_thumb_cmc), (l_thumb_mcp),(255,255,255),1)
            #     cv2.line(self.image, (l_thumb_mcp), (l_thumb_ip),(255,255,255),1)
            #     cv2.line(self.image, (l_thumb_ip), (l_thumb_tip),(255,255,255),1)

            #     cv2.line(self.image, (l_wrist), (l_index_finger_mcp),(255,255,255),1)
            #     cv2.line(self.image, (l_index_finger_mcp), (l_index_finger_pip),(255,255,255),1)
            #     cv2.line(self.image, (l_index_finger_pip), (l_index_finger_dip),(255,255,255),1)
            #     cv2.line(self.image, (l_index_finger_dip), (l_index_finger_tip),(255,255,255),1)

            #     cv2.line(self.image, (l_index_finger_mcp), (l_middle_finger_mcp),(255,255,255),1)
                
            #     cv2.line(self.image, (l_middle_finger_mcp), (l_middle_finger_pip),(255,255,255),1)
            #     cv2.line(self.image, (l_middle_finger_pip), (l_middle_finger_dip),(255,255,255),1)
            #     cv2.line(self.image, (l_middle_finger_dip), (l_middle_finger_tip),(255,255,255),1)

            #     cv2.line(self.image, (l_middle_finger_mcp), (l_ring_finger_mcp),(255,255,255),1)
                
            #     cv2.line(self.image, (l_ring_finger_mcp), (l_ring_finger_pip),(255,255,255),1)
            #     cv2.line(self.image, (l_ring_finger_pip), (l_ring_finger_dip),(255,255,255),1)
            #     cv2.line(self.image, (l_ring_finger_dip), (l_ring_finger_tip),(255,255,255),1)

            #     cv2.line(self.image, (l_ring_finger_mcp), (l_pinky_mcp),(255,255,255),1)

            #     cv2.line(self.image, (l_pinky_mcp), (l_pinky_pip),(255,255,255),1)
            #     cv2.line(self.image, (l_pinky_pip), (l_pinky_dip),(255,255,255),1)
            #     cv2.line(self.image, (l_pinky_dip), (l_pinky_tip),(255,255,255),1)

            #     cv2.line(self.image, (l_wrist), (l_pinky_mcp),(255,255,255),1)

    def draw_side_pos(self, image, detection = False, side = 2, rad_circle = 3, size_line = 1):
        l_shoulder = self.list_pose[11]
        l_hip = self.list_pose[23]
        l_ear = self.list_pose[7]

        r_shoulder = self.list_pose[12]
        r_hip = self.list_pose[24]
        r_ear = self.list_pose[8]      
        if side == 1:
            if len(self.list_pose) > 0:
                pass
        
        elif side == 2:
            if len(self.list_pose) > 0:
                cv2.circle(image, r_shoulder, rad_circle, self.ffcc99, -1)
                cv2.circle(image, (r_shoulder[0],r_shoulder[1]-50), rad_circle, self.ff9999, -1)
                cv2.circle(image, r_ear, rad_circle, self.ffcc99, -1)
                cv2.circle(image, r_hip, rad_circle, self.ffcc99, -1)
                cv2.circle(image, (r_hip[0],r_hip[1]-50), rad_circle, self.ff9999, -1)

                if not detection :
                    cv2.line(image, (r_shoulder), (r_ear), self._99ff99, size_line)
                    cv2.line(image, (r_shoulder), (r_shoulder[0],r_shoulder[1] - 50), self._99ff99, size_line)
                    cv2.line(image, (r_shoulder), (r_hip), self._99ff99, size_line)
                    cv2.line(image, (r_hip), (r_hip[0],r_hip[1] - 50), self._99ff99, size_line)

                else:
                    cv2.line(image, (r_shoulder), (r_ear), self.ff6666, size_line)
                    cv2.line(image, (r_shoulder), (r_shoulder[0],r_shoulder[1] - 50), self.ff6666, size_line)
                    cv2.line(image, (r_shoulder), (r_hip), self.ff6666, size_line)
                    cv2.line(image, (r_hip), (r_hip[0],r_hip[1] - 50), self.ff6666, size_line)