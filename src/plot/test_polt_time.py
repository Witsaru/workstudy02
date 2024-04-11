import csv
import matplotlib.pyplot as plt
import numpy as np

# อ่านข้อมูลจากไฟล์ CSV
all_times = []
alert_times = []
alert_times_n = []
alert_times_re = []

chcek = 0

with open('csv_data/Witsarut_Butdee/all_Time_Witsarut_Butdee_9.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # ข้ามหัวข้อของตาราง
    for row in reader:
        all_times.append(float(row[1]))

with open('csv_data/Witsarut_Butdee/time_poor_alert_Witsarut_Butdee_9.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # ข้ามหัวข้อของตาราง
    for row in reader:
        value = float(row[1])
        # alert_times.append(value)
        if value > chcek:
            alert_times.append(value)
            chcek = value

        else:
            # print(alert_times)
            # print()
            alert_times_n.append(alert_times)
            alert_times = []
            alert_times.append(value)
            chcek = value

alert_times_n.append(alert_times)
# print(all_times)
# print()
# print(len(alert_times_n))

solu = len(all_times)
# print(solu)
for i in range(solu):
    if i > 0:
        for j in alert_times_n[i]:
            # print(j)
            re_value = round(j + sum(all_times[0:i]),3)
            alert_times_re.append(re_value)
    
    else:
        for j in alert_times_n[i]:
            alert_times_re.append(j)

print(alert_times_re)