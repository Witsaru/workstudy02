import HolisticModule as hm

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('Agg')
from PIL import Image, ImageTk
from threading import Thread
import cv2
import time


class GUI_video():
    def __init__(self, master=None, **kwargs):
        self.holistic = hm.holistic_module()
        self.capture_state = False
        self.source_state = False
        self.root = tk.Tk()
        self.root.title("Video Capture")
        self.root.geometry("1200x700")

        # Functionality to select video source (webcam or video file)
        self.source_label = tk.Label(self.root, text="Select Webcam or Video:")
        self.source_label.pack()

        self.source_var = tk.StringVar()
        self.webcam_radio = tk.Radiobutton(self.root, text="Webcam", variable=self.source_var, value="webcam")
        self.webcam_radio.pack()

        self.video_radio = tk.Radiobutton(self.root, text="Video File", variable=self.source_var, value="video")
        self.video_radio.pack()

        # Checkbox to record video
        self.record_var = tk.IntVar()
        self.record_checkbox = tk.Checkbutton(self.root, text="Record Video", variable=self.record_var)
        self.record_checkbox.pack()

        # Functionality to select view (Top, Side, Front)
        self.view_label = tk.Label(self.root, text="Select View:")
        self.view_label.pack()

        self.view_var = tk.StringVar()
        self.top_radio = tk.Radiobutton(self.root, text="Top", variable=self.view_var, value="top")
        self.top_radio.pack()

        self.side_radio = tk.Radiobutton(self.root, text="Side", variable=self.view_var, value="side")
        self.side_radio.pack()

        self.front_radio = tk.Radiobutton(self.root, text="Front", variable=self.view_var, value="front")
        self.front_radio.pack()

        # Checkbox to draw ZRC and NWA
        self.draw_var = tk.IntVar()
        self.draw_checkbox = tk.Checkbutton(self.root, text="Draw ZRC and NWA", variable=self.draw_var)
        self.draw_checkbox.pack()

        # Button to start the capture
        self.start_button = tk.Button(self.root, text="Start Capture", command=self.start_capture)
        self.start_button.pack()

        # self.get_selections_button = tk.Button(self.root, text="Get Selections", command=self.get_selections)
        # self.get_selections_button.pack()

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        # time.sleep(1)
        self.video_source_1 = 0  # Default to webcam (you can change it to a video file path if needed)
        self.vid_1 = cv2.VideoCapture(self.video_source_1)
        self.set_frame_size(self.vid_1, width=800, height=600)

        self.video_source_2 = 2  # Default to webcam (you can change it to a video file path if needed)
        self.vid_2 = cv2.VideoCapture(self.video_source_2)
        self.set_frame_size(self.vid_2, width=800, height=600)

        self.video_source_3 = 4  # Default to webcam (you can change it to a video file path if needed)
        self.vid_3 = cv2.VideoCapture(self.video_source_3)
        self.set_frame_size(self.vid_3, width=800, height=600)

        # if self.get_source()[0]:
        #     self.video_source_2 = 2  # Default to webcam (you can change it to a video file path if needed)
        #     self.vid_2 = cv2.VideoCapture(self.video_source_2)
        #     self.set_frame_size(self.vid_2, width=800, height=600)
        # else:
        #     self.video_source_2 = "Video/test_workstudy_side.avi"
        #     self.vid_2 = cv2.VideoCapture(self.video_source_2)
        #     # self.set_frame_size(self.vid_2, width=800, height=600)

        # time.sleep(1)
        # self.video_source_3 = 4  # Default to webcam (you can change it to a video file path if needed)
        # self.vid_3 = cv2.VideoCapture(self.video_source_3)
        # self.set_frame_size(self.vid_3, width=800, height=600)

        if not self.vid_1.isOpened():
            print("Error: Could not open video source 1.")
            return
        elif not self.vid_2.isOpened():
            print("Error: Could not open video source 2.")
            return
        elif not self.vid_3.isOpened():
            print("Error: Could not open video source 3.")
            return
        
        # if self.get_source()[0]:
        #     self.update_thread_1 = Thread(target=self.update_1)
        #     self.update_thread_1.daemon = True
        #     self.update_thread_1.start()

        #     self.update_thread_2 = Thread(target=self.update_2)
        #     self.update_thread_2.daemon = True
        #     self.update_thread_2.start()
        # elif not self.get_source()[0]:
        #     self.update_thread_4 = Thread(target=self.update_4)
        #     self.update_thread_4.daemon = True
        #     self.update_thread_4.start()

        # self.update_thread_3 = Thread(target=self.update_3)
        # self.update_thread_3.daemon = True
        # self.update_thread_3.start()

        # self.vid_1.release()
        # self.vid_2.release()
        # self.vid_3.release()

        self.root.mainloop()

    def update_1(self):

        while True:
            if self.capture_state:
                ret_1, frame_1 = self.vid_1.read()
                if ret_1:
                    # Display the frame on the GUI
                    if self.select_view() == 0:
                        self.holistic.show_action(frame_1)
                        self.photo = self.convert_frame_to_photo(frame_1)
                        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
                    # print(self.select_view())
    
    def update_2(self):

        while True:
            if self.capture_state:
                ret_2, frame_2 = self.vid_2.read()
                if ret_2:
                    # Display the frame on the GUI
                    if self.select_view() == 2:
                        self.holistic.show_action(frame_2)
                        self.photo = self.convert_frame_to_photo(frame_2)
                        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
                    # print(self.select_view())
    
    def update_3(self):
        while True:
            if self.capture_state:
                ret_3, frame_3 = self.vid_3.read()
                if ret_3:
                    # Display the frame on the GUI
                    if self.select_view() == 4:
                        self.photo = self.convert_frame_to_photo(frame_3)
                        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
                    # print(self.select_view())
                        
    def update_4(self):

        while True:
            if self.capture_state:
                ret_1, frame_1 = self.vid_1.read()
                ret_2, frame_2 = self.vid_2.read()
                if ret_2:
                    # Display the frame on the GUI
                    if self.select_view() == 0:
                        self.holistic.show_action(frame_1)
                        self.photo = self.convert_frame_to_photo(frame_1)
                        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
                    elif self.select_view() == 2:
                        self.holistic.show_action(frame_2)
                        self.photo = self.convert_frame_to_photo(frame_2)
                        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
    
                        
    def set_frame_size(self, video_capture, width, height):
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def convert_frame_to_photo(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        return photo

    
    def start_capture(self):
        self.capture_state = not self.capture_state

        # Update the text on the button based on the capture state
        self.root.after(0, self.update_button_text)
        # print(self.wed_video())
        print(self.get_source()[0])

        # Use the capture_state variable as needed in your application
        # print(f"Capture State: {self.capture_state}")
        return self.capture_state
    
    def update_button_text(self):
        # Update the text on the button based on the capture state
        capture_text = "Stop Capture" if self.capture_state else "Start Capture"
        self.start_button.config(text=capture_text)
    
    def wed_video(self):
        wedcam, video = self.get_source()
        source = wedcam
        return source
    
    def get_wed_video(self, source):
        if source:
            return True
        else:
            return False
        
    def toggle_record(self):
        record_on, record_off = self.get_record_state()
        return record_on
    
    def select_view(self):
        view = self.get_view()
        video_source = self.get_video_source(view)
        return video_source
    
    def get_video_source(self, view):
        if view == 0:
            return 0
        elif view == 2:
            return 2
        elif view == 4:
            return 4
    
    def toggle_draw(self):
        draw_on, draw_off = self.get_draw_state()
        return draw_on

    def get_source(self):
        if self.source_var.get() == "webcam":
            return True, False  # Webcam selected
        else:
            return False, True  # Video file selected
        
    def get_record_state(self):
        if self.record_var.get() == 1:
            return True, False  # Checkbox checked (record)
        else:
            return False, True  # Checkbox unchecked (don't record)
        
    def get_view(self):
        if self.view_var.get() == "top":
            self.video_source = 0
            return self.video_source  # Top view selected
        elif self.view_var.get() == "side":
            self.video_source = 2
            return self.video_source  # Side view selected
        elif self.view_var.get() == "front":
            self.video_source = 4
            return self.video_source  # Front view selected
        
    def get_draw_state(self):
        if self.draw_var.get() == 1:
            return True, False  # Checkbox checked (draw)
        else:
            return False, True  # Checkbox unchecked (don't draw)
        
if __name__ == '__main__':
    # gui = GUI_study()
    video = GUI_video()
    # print(video.select_view())
    # while video.capture_state:
    #     print("Run!")

    # print("Stop!")