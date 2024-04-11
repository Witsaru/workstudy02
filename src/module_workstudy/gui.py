import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('Agg')
import threading
import cv2

class GUI_study():

    def __init__(self):
        self.symbol_data = {
            "Operation": 0,
            "Transportation": 0.5,
            "Delay": 1,
            "Inspection": 1.5,
            "Storage":2
        }
        self.fig, self.ax = plt.subplots(figsize=(10,6))
        self.data = {}
        self.axis_y = 13

        self.root = tk.Tk()
        self.root.title("Flow process")

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        self.key_label = tk.Label(self.input_frame, text="Process:")
        self.key_label.grid(row=0, column=0, padx=5, pady=5)
        self.key_entry = tk.Entry(self.input_frame)
        self.key_entry.grid(row=0, column=1, padx=5, pady=5)

        self.symbol_label = tk.Label(self.input_frame, text="Select Symbol:")
        self.symbol_label.grid(row=1, column=0, padx=5, pady=5)

        self.symbols = list(self.symbol_data.keys())
        self.symbol_var = tk.StringVar()
        self.symbol_var.set(self.symbols[0])
        self.symbol_option = tk.OptionMenu(self.input_frame, self.symbol_var, *self.symbols)
        self.symbol_option.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.input_frame, text="Add", command=self.add_data)
        self.add_button.grid(row=1, column=2, padx=5, pady=5)

        self.key_delete_label = tk.Label(self.input_frame, text="Key to Delete:")
        self.key_delete_label.grid(row=3, column=0, padx=5, pady=5)
        self.key_delete_entry = tk.Entry(self.input_frame)
        self.key_delete_entry.grid(row=3, column=1, padx=5, pady=5)

        self.delete_last_button = tk.Button(self.input_frame, text="Delete Last Added", command=self.delete_last_added)
        self.delete_last_button.grid(row=4, columnspan=4, padx=5, pady=5)

        self.display = tk.Text(self.root, height=10, width=50)
        self.display.pack(padx=10, pady=10)
        self.display.config(state=tk.DISABLED)

    def Flow_process_ui(self):
        # Create and configure the Matplotlib plot
        steps = self.data
        stepsN = {}
        self.plot_process_chart_main()
        self.root.after(100, self.Flow_process_ui)

        # Draw Two-handed Process Chart
        for step, symbol in steps.items():
            self.plot_process_chart(symbol, self.axis_y)
            stepsN[step] = (symbol, self.axis_y)
            self.axis_y -= 1

        # Connect the lines in the Two-handed Process Chart horizontally
        for i in range(len(steps) - 1):
            self.ax.plot([stepsN[list(stepsN.keys())[i]][0], stepsN[list(stepsN.keys())[i + 1]][0]],
                         [stepsN[list(stepsN.keys())[i]][1], stepsN[list(stepsN.keys())[i + 1]][1]], 'k-', lw=1)

        # Adjust the details of the plot
        self.ax.set_xlim(-1, 3)
        if stepsN:
            self.ax.set_ylim(0, max([pos[1] for pos in stepsN.values()]) + 3)
        self.ax.axis('off')

        # Show the Two-handed Process Chart

        self.root.mainloop()

    def add_data(self):
        key = self.key_entry.get()
        symbol = self.symbol_var.get()
        value = self.symbol_data[symbol]
        self.data[key] = value
        self.update_display()

    def delete_last_added(self):
        if self.data:
            last_key = list(self.data.keys())[-1]
            del self.data[last_key]
            self.update_display()

    def update_display(self):
        self.display.config(state=tk.NORMAL)
        self.display.delete('1.0', tk.END)
        for key, value in self.data.items():
            self.display.insert(tk.END, f"{key}: {value}\n")
        self.display.config(state=tk.DISABLED)

    def plot_process_chart(self, x, y):
        self.ax.scatter(x, y, s=50, marker='o', color='black')

    def plot_process_chart_main(self):
        self.ax.scatter(0, 15, s=500, marker='o', color='darkblue')
        self.ax.scatter(0.5, 15, s=500, marker='>', color='darkblue')
        self.ax.scatter(1, 15, s=500, marker='H', color='darkblue')
        self.ax.scatter(1.5, 15, s=500, marker='s', color='darkblue')
        self.ax.scatter(2, 15, s=500, marker='v', color='darkblue')

class GUI_video():
    def __init__(self, master=None, **kwargs):
        self.capture_state = False
        self.root = tk.Tk()
        self.root.title("Video Capture")

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

    
    def start_capture(self):
        self.capture_state = not self.capture_state

        # Update the text on the button based on the capture state
        self.root.after(0, self.update_button_text)

        # Use the capture_state variable as needed in your application
        # print(f"Capture State: {self.capture_state}")
        return self.capture_state
    
    def update_button_text(self):
        # Update the text on the button based on the capture state
        capture_text = "Stop Capture" if self.capture_state else "Start Capture"
        self.start_button.config(text=capture_text)
        
    def toggle_record(self):
        record_on, record_off = self.get_record_state()
        return record_on
    
    def select_view(self):
        view = self.get_view()
        return view
    
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
            return 1  # Top view selected
        elif self.view_var.get() == "side":
            return 2  # Side view selected
        else:
            return 3  # Front view selected
        
    def get_draw_state(self):
        if self.draw_var.get() == 1:
            return True, False  # Checkbox checked (draw)
        else:
            return False, True  # Checkbox unchecked (don't draw)

# class OpenCVThread(threading.Thread):
#     # def __init__(self,gui):
#     #     threading.Thread.__init__(self)
#     #     self.gui = gui
#     def run(self):
#         cap = cv2.VideoCapture(0)
#         while True:
#             _, img = cap.read()
#             cv2.imshow("d", img)
#             if cv2.waitKey(5) & 0xFF == 27:
#                 break
#         cap.release()
#         cv2.destroyAllWindows()
        
def capture_loop(video_instance):
    while video_instance.start_capture():
        print("Run!")

    print('Stop!')

if __name__ == '__main__':
    # gui = GUI_study()
    video = GUI_video()
    gui_thread = threading.Thread(target=video.root.mainloop)
    gui_thread.start()

    # gui.Flow_process_ui()

    capture_thread =threading.Thread(target=capture_loop, args=(video,))
    capture_thread.start()
    
    # capture_loop(video)
    gui_thread.join()
    capture_thread.join()