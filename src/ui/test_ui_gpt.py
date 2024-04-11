#!/usr/bin/python
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
import pandas as pd
from PyQt5.QtGui import QImage, QPixmap
import rclpy
# from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import serial
import json
import time

sys.path.append("/home/witsarut/workstudy02_ws/src/module_workstudy")
# sys.path.append("/home/witsarut/workstudy_ws/src/opencv_ros/opencv_ros")

import HolisticModule as hm
import AssemblePats as ap
import draw_pose as dp
import Motion as M
import utils as u
# from opencv_ros2_sub import ImageSubscriber, cv_bridge_to_pixmap
import pandas_f as pdf
from timer_ import Timer
import cal_st_

sys.path.append("/home/witsarut/workstudy02_ws/src/plot")
# import test_polt01 as tp01
import plot_time_process as ptp
import plot_poor_graph as ppg


import plot_process_time as ppt
import plot_poor as pp
import calculate_st as cal_st

rclpy.init()


class VideoCaptureWidget(QtWidgets.QLabel):
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.video_capture = None
        # self.subscriber = ImageSubscriber()
        self.holistic = hm.holistic_module()
        self.motion = M.Motion_time()

        self.timer = QtCore.QTimer(self)
        self.timer2 = QtCore.QTimer(self)
        self.save_data = pdf.C_pandas("Test")

        # self.anime_p = ptr.anime_polt()
        # self.process_time = pws.plotlib()

        try:
            self.arduino = serial.Serial(port="/dev/ttyACM0", baudrate=115200, timeout=0.1)

        except Exception as e:
            print('Error = ', e)

        self.bridge = CvBridge()

        self.timer.timeout.connect(self.update_frame)

        self.is_running = False
        self.poeslist = None

        self.scrip_r = [6,7,8]
        self.scrip_l = [5,4,3]

        self.sensor_r = 0
        self.sensor_l = 0

        self.round = 0
        self._runpoor = 0
        self._stoppoor = 0

        self.time_program = Timer()
        self.s_time_program = 0
        self.e_time_program = 0
        self.all_time_program = []

        self.set_shoulder = []
        self.aruco_marker_memory = {}

        self.point_h_r_x = []
        self.point_h_r_y = []
        self.point_h_l_x = []
        self.point_h_l_y = []

        self.time_poon = None
        self.poor_body = None
        self.poor = False
        self.time_all_poor = []

        self.check_ = []
        self.index = 0
        self.index_ = 0
        self.index_copy = 0

        self.sensor_po = None
        self.sensor_po2 = None

        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)

        self.average_shoulder_width_cm = 44.4
        self.hypothetical_pixel_width = 200
        self.pixels_per_cm = (
            self.hypothetical_pixel_width / self.average_shoulder_width_cm
        )

    def start_video(self, source):
        if not self.is_running:
            self.s_time_program = time.time()
            self._runpoor = time.time()
            self.round+=1
            self.video_capture = cv2.VideoCapture(source)
            self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.timer.start(1)
            self.is_running = True

    def stop_video(self):
        if self.is_running:
            self.timer.stop()
            self.e_time_program = time.time()
            totol = round(self.e_time_program - self.s_time_program,3)
            self.all_time_program.append(totol)
            self.save_data.list_to_pasdan(self.all_time_program,"all_Time",self.round)
            # self.timer4.stop()
            self.video_capture.release()
            self.is_running = False
            self.save_data.list_to_pasdan(self.motion.return_time_l(),"Left",self.round)
            self.save_data.list_to_pasdan(self.motion.return_time_r(),"Right",self.round)
            print(f"Time)_L: {self.motion.return_time_l()}\n")
            print(f"Time_R: {self.motion.return_time_r()}\n")
            self.save_data.list_to_pasdan(self.motion.return_time_real_l(),"real_Left",self.round)
            self.save_data.list_to_pasdan(self.motion.return_time_real_r(),"real_Right",self.round)
            print(f"Time_real_L: {self.motion.return_time_real_l()}\n")
            print(f"Time_real_R: {self.motion.return_time_real_r()}\n")
            # df = pd.DataFrame(self.time_)
            # print(self.motion.return_time_l())
            # print(df)

    def stop_video2(self):
        if self.is_running:
            self.timer.stop()
            self.video_capture.release()
            self.is_running = False
            self.save_data.list_to_pasdan(self.poor_body['time'],"time_poor",self.round)
            self.save_data.list_to_pasdan(self.time_all_poor,"time_poor_alert",self.round)
            self.save_data.list_to_pasdan(self.poor_body['neck'],"neck_poor",self.round)
            print(f"Poor_time: {self.poor_body}\n")

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            # print(f"{ptr.anime_polt().y_vals}")

            if isinstance(self, VideoCaptureWidget):
                if self == self.ui.cam_frontlabel:

                    # list_aruco = self.memory_aruco(frame)
                    try:
                        id_0 = self.memory_aruco(0, frame)
                        id_1 = self.memory_aruco(1, frame)

                        id_10 = self.memory_aruco(10, frame)
                        id_11 = self.memory_aruco(11, frame)

                    except Exception as e:
                        print('Error = ', e)
                    # id_l = self.memory_aruco(self.sci[self.index_], frame)
                    # print(id_l, self.index_, id_0)

                    # print(self.list_proxi_left_top_1, self.list_proxi_left_top_2, self.list_proxi_left_top_3)

                    self.holistic.show_action(frame)
                    poeslist = self.holistic.finepos(frame)
                    # print(f"cam1: {poeslist} \n")
                    if len(poeslist) > 0:
                        try:
                            r_shoulder = poeslist[12]
                            l_shoulder = poeslist[11]

                            r_elbow = poeslist[14]
                            r_wrist = poeslist[16]

                            l_elbow = poeslist[13]
                            l_wrist = poeslist[15]

                            r_index = poeslist[20]
                            l_index = poeslist[19]

                            drawPose = dp.DrawPose(frame, poeslist)

                            sho_90_ = ap.findAngle(r_shoulder, l_shoulder)

                            A_arm_r = ap.findAngle(r_elbow, r_wrist)
                            A_arm_l = ap.findAngle(l_elbow, l_wrist)

                            A_shr_l = ap.findAngle(l_shoulder, l_elbow)
                            A_shr_r = ap.findAngle(r_shoulder, r_elbow)

                            A_elbow_l = ap.findAngle_elbow(l_shoulder, l_elbow, l_wrist)
                            A_elbow_r = ap.findAngle_elbow(r_shoulder, r_elbow, r_wrist)

                            tp = ap.findAngle(r_shoulder, r_wrist)

                            # d_s_e_r = ap.findDistance(r_shoulder, r_elbow)
                            # d_e_w_r = ap.findDistance(r_shoulder, r_index)

                            # d_s_e_l = ap.findDistance(l_shoulder, l_elbow)
                            # d_e_w_l = ap.findDistance(l_index, l_index)
                            
                            dis_r_wrist_0 = ap.findDistance(r_index, id_0)
                            dis_r_wrist_1 = ap.findDistance(r_index, id_1)

                            dis_l_wrist_10 = ap.findDistance(l_index, id_10)
                            dis_l_wrist_11 = ap.findDistance(l_index, id_11)

                            self.read_serial()

                            # print(f"rigth: {dis_r_wrist_0,dis_r_wrist_1} letf: {dis_l_wrist_10,dis_l_wrist_11}")
                            if self.sensor_po2 is not None:
                                self.motion.duo_move_action_l(self.scrip_l, self.sensor_l,dis_l_wrist_10, dis_l_wrist_11)
                            if self.sensor_po is not None:
                                self.motion.duo_move_action_r(self.scrip_r,self.sensor_r, dis_r_wrist_0, dis_r_wrist_1)

                            # print(dis_l_wrist_10, dis_l_wrist_11)

                            pixel_distance_shoulders = abs(
                                r_shoulder[0] - l_shoulder[0]
                            )
                            distance_shoulders_cm = (
                                pixel_distance_shoulders / self.pixels_per_cm
                            )

                            if (
                                distance_shoulders_cm >= 38
                                and len(self.set_shoulder) == 0
                            ):

                            #     if sho_90_ == 90:
                            #         self.set_shoulder.append(r_shoulder)
                            #         self.set_shoulder.append(l_shoulder)

                            # if len(self.set_shoulder) > 0:
                            #     cv2.circle(
                            #         frame,
                            #         self.set_shoulder[0],
                            #         int(44.2 * self.pixels_per_cm),
                            #         (0, 255, 0),
                            #         3,
                            #     )
                            #     cv2.circle(
                            #         frame,
                            #         self.set_shoulder[0],
                            #         int(72.1 * self.pixels_per_cm),
                            #         (0, 0, 255),
                            #         3,
                            #     )

                            #     cv2.circle(
                            #         frame,
                            #         self.set_shoulder[1],
                            #         int(44.2 * self.pixels_per_cm),
                            #         (0, 255, 0),
                            #         3,
                            #     )
                            #     cv2.circle(
                            #         frame,
                            #         self.set_shoulder[1],
                            #         int(72.1 * self.pixels_per_cm),
                            #         (0, 0, 255),
                            #         3,
                            #     )
                                self.point_h_r_x.append(r_wrist[0])
                                self.point_h_r_y.append(r_wrist[1])
                                self.point_h_l_x.append(l_wrist[0])
                                self.point_h_l_y.append(l_wrist[1])

                        except Exception as e:
                            print('Error = ', e)

                elif self == self.ui.cam_sidelabel:
                    self.holistic.show_action(frame)
                    poeslist = self.holistic.finepos(frame)
                    # print(f"cam2: {poeslist} \n")
                    if len(poeslist) > 0:
                        l_shoulder = poeslist[11]
                        l_hip = poeslist[23]
                        l_eye = poeslist[5]

                        r_shoulder = poeslist[12]
                        r_hip = poeslist[24]
                        r_eye = poeslist[2]

                        neck = ap.findAngle(r_shoulder, r_eye)
                        torso = ap.findAngle(r_hip, r_shoulder)

                        posture = self.motion.body_posture_detection(neck, torso)

                        if posture:
                            if self.poor:
                                self._stoppoor = time.time()
                                total = round(self._stoppoor - self._runpoor,3)
                                self.time_all_poor.append(total)
                                self.poor = False

                        else:
                            if not self.poor:
                                self.poor = True

                        drawPose = dp.DrawPose(frame, poeslist)
                        drawPose.draw_side_pos(
                            frame, detection=posture, rad_circle=5, size_line=2
                        )
                        self.time_poon = self.motion.poor_body(posture, neck, torso)

                        self.poor_body = self.motion.return_poor_time()
                        # print(self.poor_body)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            convert_to_qt_format = QImage(
                frame.data, w, h, bytes_per_line, QImage.Format_RGB888
            )
            p = convert_to_qt_format.scaled(352, 288, QtCore.Qt.KeepAspectRatio)
            self.setPixmap(QPixmap.fromImage(p))

        # return self.poeslist

    def memory_aruco(self, ids_num, image):
        if ids_num not in self.aruco_marker_memory:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            corners, ids, _ = cv2.aruco.detectMarkers(gray, self.aruco_dict)
            list_posAruco = u.aruco_display(corners, ids, 17, image)
            for market_id, cX, cY in list_posAruco:
                # print(ids)
                if market_id == ids_num:
                    self.aruco_marker_memory[ids_num] = (cX, cY)
                    return self.aruco_marker_memory

        else:
            return self.aruco_marker_memory[ids_num]

    def cal_dits(self, point, id_point):

        if id_point is not None:
            dits = ap.findDistance(point, id_point)
            # Text(image, dits, id_point[0], id_point[1])
            return dits
        else:
            pass

    
    def read_serial(self):
        # self.sensor_po = None
        if self.arduino.in_waiting > 0:
            data = self.arduino.readline().decode("utf").rstrip('\n')
            self.sensor_po = int(data)
            self.sensor_po2 = int(data)
            if self.sensor_po in self.scrip_r:
                self.sensor_r = self.sensor_po
            if self.sensor_po2 in self.scrip_l:
                self.sensor_l = self.sensor_po2


class Ui_MainWindow(object):
    def __init__(self):
        self.fname_alltime = None
        self.fname_timealert = None
        self.fname_timepoor = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Workstudy")
        MainWindow.resize(1209, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frontview_label = QtWidgets.QLabel(self.centralwidget)
        self.frontview_label.setGeometry(QtCore.QRect(126, 10, 351, 20))
        self.frontview_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frontview_label.setTextFormat(QtCore.Qt.AutoText)
        self.frontview_label.setObjectName("frontview_label")
        self.topview_label = QtWidgets.QLabel(self.centralwidget)
        self.topview_label.setGeometry(QtCore.QRect(120, 330, 351, 20))
        self.topview_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.topview_label.setTextFormat(QtCore.Qt.AutoText)
        self.topview_label.setObjectName("topview_label")
        self.side_label = QtWidgets.QLabel(self.centralwidget)
        self.side_label.setGeometry(QtCore.QRect(480, 10, 351, 20))
        self.side_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.side_label.setTextFormat(QtCore.Qt.AutoText)
        self.side_label.setObjectName("side_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1040, 220, 31, 251))
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(880, 290, 161, 171))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 159, 169))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.topvideo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.topvideo_label.setGeometry(QtCore.QRect(0, 130, 141, 17))
        self.topvideo_label.setObjectName("topvideo_label")
        self.video_front_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.video_front_button.setGeometry(QtCore.QRect(0, 0, 141, 25))
        self.video_front_button.setObjectName("video_front_button")
        self.video_top_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.video_top_button.setGeometry(QtCore.QRect(0, 100, 141, 25))
        self.video_top_button.setObjectName("video_top_button")
        self.video_side_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.video_side_button.setGeometry(QtCore.QRect(0, 50, 141, 25))
        self.video_side_button.setObjectName("video_side_button")
        self.sidevideo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sidevideo_label.setGeometry(QtCore.QRect(0, 80, 141, 17))
        self.sidevideo_label.setObjectName("sidevideo_label")
        self.frontvideo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.frontvideo_label.setGeometry(QtCore.QRect(0, 30, 141, 17))
        self.frontvideo_label.setObjectName("frontvideo_label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(860, 30, 151, 161))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.start_button = QtWidgets.QPushButton(self.splitter)
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.splitter)
        self.stop_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stop_button.setAutoFillBackground(False)
        self.stop_button.setObjectName("stop_button")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(860, 200, 181, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.source_label = QtWidgets.QLabel(self.layoutWidget)
        self.source_label.setObjectName("source_label")
        self.verticalLayout.addWidget(self.source_label)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.wedcam_radiobutton = QtWidgets.QRadioButton(self.layoutWidget)
        self.wedcam_radiobutton.setObjectName("wedcam_radiobutton")
        self.verticalLayout.addWidget(self.wedcam_radiobutton)
        self.video_radiobutton = QtWidgets.QRadioButton(self.layoutWidget)
        self.video_radiobutton.setObjectName("video_radiobutton")
        self.verticalLayout.addWidget(self.video_radiobutton)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1070, 200, 121, 106))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.view_label = QtWidgets.QLabel(self.layoutWidget1)
        # self.view_label.setObjectName("view_label")
        # self.verticalLayout_2.addWidget(self.view_label)
        # self.front_radiobutton = QtWidgets.QRadioButton(self.layoutWidget1)
        # self.front_radiobutton.setObjectName("front_radiobutton")
        # self.verticalLayout_2.addWidget(self.front_radiobutton)
        # self.side_radiobutton = QtWidgets.QRadioButton(self.layoutWidget1)
        # self.side_radiobutton.setObjectName("side_radiobutton")
        # self.verticalLayout_2.addWidget(self.side_radiobutton)
        # self.top_radiobutton = QtWidgets.QRadioButton(self.layoutWidget1)
        # self.top_radiobutton.setObjectName("top_radiobutton")
        # self.verticalLayout_2.addWidget(self.top_radiobutton)

        self.cam_frontlabel = VideoCaptureWidget(self,self.centralwidget)
        self.cam_frontlabel.setGeometry(QtCore.QRect(120, 30, 352, 288))
        self.cam_frontlabel.setTabletTracking(False)
        self.cam_frontlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.cam_frontlabel.setObjectName("cam_frontlabel")

        self.cam_sidelabel = VideoCaptureWidget(self,self.centralwidget)
        self.cam_sidelabel.setGeometry(QtCore.QRect(480, 30, 352, 288))
        self.cam_sidelabel.setTabletTracking(False)
        self.cam_sidelabel.setFrameShape(QtWidgets.QFrame.Box)
        self.cam_sidelabel.setObjectName("cam_sidelabel")

        self.cam_toplabel = VideoCaptureWidget(self,self.centralwidget)
        self.cam_toplabel.setGeometry(QtCore.QRect(120, 350, 352, 288))
        self.cam_toplabel.setTabletTracking(False)
        self.cam_toplabel.setFrameShape(QtWidgets.QFrame.Box)
        self.cam_toplabel.setObjectName("cam_toplabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Tool = QtWidgets.QMenu(self.menubar)
        self.menu_Tool.setObjectName("menu_Tool")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Graph_process_Round_Time_s = QtWidgets.QAction(MainWindow)
        self.action_Graph_process_Round_Time_s.setObjectName("action_Graph_process_Round_Time_s")
        self.action_Graph_process_Round_Time_s.triggered.connect(self.plot_process_time)

        self.Graph_poor = QtWidgets.QAction(MainWindow)
        self.Graph_poor.setObjectName("Graph_poor")
        self.Graph_poor.triggered.connect(self.plot_poor)

        self.calculate_st = QtWidgets.QAction(MainWindow)
        self.calculate_st.setObjectName("calculate_st")
        self.calculate_st.triggered.connect(self.calculate_standas)

        self.menu_Tool.addAction(self.action_Graph_process_Round_Time_s)
        self.menu_Tool.addAction(self.Graph_poor)
        self.menu_Tool.addAction(self.calculate_st)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Tool.menuAction())

        self.retranslateUi(MainWindow)
        # if self.wedcam_radiobutton.isChecked() == True or self.video_radiobutton.isChecked() == True:
        self.start_button.clicked.connect(self.start_video_)  # type: ignore
        self.start_button.clicked.connect(self.start_video_)  # type: ignore
        # self.start_button.clicked.connect(self.start_video_ros_)  # type: ignore
        self.stop_button.clicked.connect(self.stop_video_1)  # type: ignore
        self.stop_button.clicked.connect(self.stop_video_2)  # type: ignore
        # self.stop_button.clicked.connect(self.stop_video_ros_)  # type: ignore

        # self.action_Graph_process_Round_Time_s.triggered.connect(self.plot_process_time)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Workstudy DPU"))
        self.frontview_label.setText(_translate("MainWindow", "Top"))
        self.topview_label.setText(_translate("MainWindow", "Front"))
        self.side_label.setText(_translate("MainWindow", "Side"))
        self.topvideo_label.setText(_translate("MainWindow", "Top video"))
        self.video_front_button.setText(_translate("MainWindow", "select front video"))
        self.video_top_button.setText(_translate("MainWindow", "select top video"))
        self.video_side_button.setText(_translate("MainWindow", "select side video"))
        self.sidevideo_label.setText(_translate("MainWindow", "Side video"))
        self.frontvideo_label.setText(_translate("MainWindow", "Front video"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.source_label.setText(_translate("MainWindow", "Source"))
        self.wedcam_radiobutton.setText(_translate("MainWindow", "Wedcam"))
        self.video_radiobutton.setText(_translate("MainWindow", "Video"))
        # self.view_label.setText(_translate("MainWindow", "View"))
        # self.front_radiobutton.setText(_translate("MainWindow", "Front"))
        # self.side_radiobutton.setText(_translate("MainWindow", "Side"))
        # self.top_radiobutton.setText(_translate("MainWindow", "Top"))
        self.cam_frontlabel.setText(_translate("MainWindow", "cam1"))
        self.cam_sidelabel.setText(_translate("MainWindow", "cam2"))
        self.cam_toplabel.setText(_translate("MainWindow", "cam3"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Tool.setTitle(_translate("MainWindow", "&Tool"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Graph_process_Round_Time_s.setText(_translate("MainWindow", "&Graph process : Item/Time(s)"))
        self.Graph_poor.setText(_translate("MainWindow", "&Graph poor : Time(s)/Event Index"))
        self.calculate_st.setText(_translate("MainWindow", "&Standard Time"))

    def plot_process_time(self):
        self.plot_window = QtWidgets.QDialog()
        self.plot_ui = ppt.Ui_Plot_process_time()
        self.plot_ui.setupUi(self.plot_window)
        self.plot_ui.pushButton_Browse.clicked.connect(self.browsefile)
        self.plot_ui.pushButton_plot.clicked.connect(self.plot_)
        self.plot_window.exec_()

    def plot_poor(self):
        plot_window = QtWidgets.QDialog()
        self.plot_p = pp.Ui_plot_poor_body()
        self.plot_p.setupUi(plot_window)
        self.plot_p.pushButton_alltime.clicked.connect(self.browsefile_alltime)
        self.plot_p.pushButton_timepooralert.clicked.connect(self.browsefile_timealert)
        self.plot_p.pushButton_timepoor.clicked.connect(self.browsefile_timepoor)
        self.plot_p.pushButton.clicked.connect(self.plot_poorgraph)
        plot_window.exec_()

    def calculate_standas(self):
        plot_window = QtWidgets.QDialog()
        self.cal_st = cal_st.Ui_CalST()
        # self.browsefile_calST()
        self.cal_st.setupUi(plot_window)
        self.cal_st.pushButton_browsest.clicked.connect(self.browsefile_calST)
        self.cal_st.pushButton_calculate.clicked.connect(self.calcu_st)
        plot_window.exec_()

    def plot_(self):
        if self.fname:
            ptp.plotTimeProcess(self.fname)

    def plot_poorgraph(self):
        if (self.fname_alltime and self.fname_timealert) and self.fname_timepoor:
            plot_poor = ppg.plot_poor_()
            plot_poor.plotgraph(self.fname_alltime,self.fname_timealert,self.fname_timepoor)

    def calcu_st(self):
        ratfac = self.cal_st.doubleSpinBox_retingfactor.value()
        allow = self.cal_st.doubleSpinBox_allowances.value()
        if self.fname_calST:
            if ratfac > 0.00 and allow > 0.00:
                time_st = cal_st_.calcu_stantime(self.fname_calST,ratfac,allow)
                self.cal_st.lcdNumber_averagetime.display(time_st[0])
                self.cal_st.lcdNumber_normaltime.display(time_st[1])
                self.cal_st.lcdNumber_standardtime.display(time_st[2])

    def browsefile(self):
        self.fname, _ = QFileDialog.getOpenFileName(None, 'Open file','CSV files (.csv)')
        if self.fname:
            self.plot_ui.lineEdit_file.setText(self.fname)

    def browsefile_alltime(self):
        fname_alltime, _ = QFileDialog.getOpenFileName(None, 'Open file','CSV files (.csv)')
        self.fname_alltime = fname_alltime
        if self.fname_alltime:
            self.plot_p.lineEdit_filenamealltime.setText(self.fname_alltime)

    def browsefile_timealert(self):
        fname_timealert, _ = QFileDialog.getOpenFileName(None, 'Open file','CSV files (.csv)')
        self.fname_timealert = fname_timealert
        if self.fname_timealert:
            self.plot_p.lineEdit_filetimepooralert.setText(self.fname_timealert)

    def browsefile_timepoor(self):
        fname_timepoor, _ = QFileDialog.getOpenFileName(None, 'Open file','CSV files (.csv)')
        self.fname_timepoor = fname_timepoor
        if self.fname_timepoor:
            self.plot_p.lineEdit_filetimepoor.setText(self.fname_timepoor)

    def browsefile_calST(self):
        self.fname_calST, _ = QFileDialog.getOpenFileName(None, 'Open file','CSV files (.csv)')
        if self.fname_calST:
            self.cal_st.lineEdit_filerealtime.setText(self.fname_calST)

    def start_video_(self):
        if self.wedcam_radiobutton.isChecked():
            self.cam_frontlabel.start_video(0)  # Change the index based on your webcam
            self.cam_sidelabel.start_video(2)
        elif self.video_radiobutton.isChecked():
            self.cam_frontlabel.start_video(
                "video/Workstudy_Test_Top_New.avi"
            )  # Change the file path
            self.cam_sidelabel.start_video("video/Workstudy_Test_Side_New.avi")

    # def start_video_ros_(self):
    #     if self.wedcam_radiobutton.isChecked():
    #         self.cam_toplabel.start_video_ros("image_topic")

    #     elif self.video_radiobutton.isChecked():
    #         self.cam_toplabel.start_video("Workstudy_Test_Side_New.avi")

    # def start_video2(self):
    #     if self.wedcam_radiobutton.isChecked():
    #         self.cam_sidelabel.start_video(2)  # Change the index based on your webcam

    #     elif self.video_radiobutton.isChecked():
    #         self.cam_sidelabel.start_video("Video/test_workstudy_side.avi")  # Change the file path

    def stop_video_1(self):
        self.cam_frontlabel.stop_video()
        # self.cam_sidelabel.stop_video()

    def stop_video_2(self):
        self.cam_sidelabel.stop_video2()

    # def stop_video_ros_(self):
    #     self.cam_toplabel.stop_video_ros()

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    # plot_ui = ppt.Ui_Plot_process_time()
    # plot_ui.activatePlotprocess()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
