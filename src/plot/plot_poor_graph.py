import csv
import matplotlib.pyplot as plt
import os

class plot_poor_():
    def __init__(self) -> None:
        self.waiting_times = []

        self.seating_times_n = []
        self.waiting_times_n = []
        self.all_times = []
        self.alert_times = []
        self.alert_times_n = []
        self.alert_times_re = []

        self.checek=0
        self.range_value=0

    def plotgraph(self, file_alltime, file_alert, file_poor):
        name = file_poor
        file_name = os.path.basename(name)

        with open(file_alltime, newline='')as csvfile:
            reader=csv.reader(csvfile)
            next(reader)
            for row in reader:
                self.all_times.append(float(row[1]))

        with open(file_alert,  newline='')as csvfile:
            reader=csv.reader(csvfile)
            next(reader)
            for row in reader:
                value = float(row[1])
                if value > self.checek:
                    self.alert_times.append(value)
                    self.checek = value
                else:
                    self.alert_times_n.append(self.alert_times)
                    self.alert_times = []
                    self.alert_times.append(value)
                    self.checek = value

            self.alert_times_n.append(self.alert_times)

        with open(file_poor,  newline='')as csvfile:
            reader=csv.reader(csvfile)
            next(reader)
            for row in reader:
                self.waiting_times.append(float(row[1]))

        solu = len(self.all_times)
        for i in range(solu):
            if i > 0:
                for j in self.alert_times_n[i]:
                    re_value = round(j + sum(self.all_times[0:i]),3)
                    self.alert_times_re.append(re_value)

            else:
                for j in self.alert_times_n[i]:
                    self.alert_times_re.append(j)

        if len(self.alert_times_re) == len(self.alert_times_re):   
            range_value = len(self.alert_times_re)
            for i in range(range_value):
                if self.waiting_times[i] > 10:
                    self.seating_times_n.append(self.alert_times_re[i])
                    self.waiting_times_n.append(self.waiting_times[i])

        bar_times = [(self.seating_times_n[i],self.seating_times_n[i] + self.waiting_times_n[i]) for i in range(len(self.seating_times_n))]

        plt.figure(figsize=(10, 6))
        for i, (start, end) in enumerate(bar_times):
            # print(start,end)
            plt.plot([start, end], [i+1, i+1], color='red')
            plt.scatter(start, i+1, color='blue', s=1)  # กำหนดขนาดของจุดเล็กลงเป็น 5
            plt.scatter(end, i+1, color='blue', s=1)    # กำหนดขนาดของจุดเล็กลงเป็น 5
        plt.xlabel('Time(s)')
        plt.ylabel('Event Index')
        plt.title(file_name)
        plt.grid(True)
        plt.show()