import tkinter as tk


window = tk.Tk()

def get_mode_video():
    value = modes.get()
    return value

window.rowconfigure(0, minsize=50, weight=1)

window.columnconfigure([0, 1, 2], minsize=50, weight=1)


btn_Wedcam = tk.Button(master=window, text="Wedcam", command=0)

btn_Wedcam.grid(row=0, column=0, sticky="nsew")

btn_Video = tk.Button(master=window, text="Video", command=1)

btn_Video.grid(row=0, column=1, sticky="nsew")


window.mainloop()