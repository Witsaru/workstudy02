import math
import csv

def calcu_stantime(file_,ratfac,allowa):

    with open(file_, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

        x = []
        y = []

    for row in data[1:]:
        index = int(row[0])
        value = float(row[1])
        if value < 100:  # Filter out values greater than 100 (adjust threshold as needed)
            x.append(index)
            y.append(value)

    aver = round(sum(y)/len(y),3)
    nor = round(aver*(ratfac/100),3)
    sta = round(nor * (1-(allowa/100)),3)

    return [aver, nor, sta]

if __name__ == "__main__":
    st = calcu_stantime('csv_data/Witsarut_Butdee/real_Right_Witsarut_Butdee_9.csv',95,5)
    print(st)