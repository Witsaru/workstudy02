import csv
import matplotlib.pyplot as plt

# อ่านข้อมูลจากไฟล์ CSV
waiting_times = []

seating_times_n = []
waiting_times_n = []
all_times = []
alert_times = []
alert_times_n = []
alert_times_re = []

chcek = 0
range_value = 0

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
solu = len(all_times)

for i in range(solu):
    if i > 0:
        for j in alert_times_n[i]:
            # print(j)
            re_value = round(j + sum(all_times[0:i]),3)
            alert_times_re.append(re_value)
    
    else:
        for j in alert_times_n[i]:
            alert_times_re.append(j)

with open('csv_data/Witsarut_Butdee/time_poor_Witsarut_Butdee_9.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # ข้ามหัวข้อของตาราง
    for row in reader:
        waiting_times.append(float(row[1]))

if len(alert_times_re) == len(alert_times_re):   
    range_value = len(alert_times_re)
    for i in range(range_value):
        if waiting_times[i] > 10:
            seating_times_n.append(alert_times_re[i])
            waiting_times_n.append(waiting_times[i])

print(f"{len(alert_times_re)} || {len(alert_times_re)}")

bar_times = [(seating_times_n[i],seating_times_n[i] + waiting_times_n[i]) for i in range(len(seating_times_n))]

plt.figure(figsize=(10, 6))
for i, (start, end) in enumerate(bar_times):
    print(start,end)
    plt.plot([start, end], [i+1, i+1], color='red')
    plt.scatter(start, i+1, color='blue', s=1)  # กำหนดขนาดของจุดเล็กลงเป็น 5
    plt.scatter(end, i+1, color='blue', s=1)    # กำหนดขนาดของจุดเล็กลงเป็น 5

# สร้างกราฟ
# print(seating_times_n)
# print()
# print(len(waiting_times_n))
# plt.figure(figsize=(10, 6))
# plt.plot(seating_times_n, waiting_times_n, marker='o', linestyle='-', color='b')
# plt.title('เวลาที่นั่ง vs. ระยะเวลาที่อยู่ในท่า')
# plt.xlabel('เวลาที่นั่ง (วินาที)')
# plt.ylabel('ระยะเวลาที่อยู่ในท่า (วินาที)')
# plt.grid(True)

# # แสดงกราฟ
# plt.show()
plt.xlabel('Time')
plt.ylabel('Event Index')
plt.title('time_poor_Toey>10s')
plt.grid(True)
plt.show()