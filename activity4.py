import csv
import matplotlib.pyplot as plt
filename = "activity.csv"


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    interval = []
    i = 0
    weekdayTotal = 0
    weekendTotal = 0
    weekdayCount = 0
    weekendCount = 0
    weekendAvg = []
    weekdayAvg = []
    day = 0
    while i < 2360:
        interval.append(i)
        i += 5

    for x in range (0,len(interval)):
        f.seek(0)
        next(f)
        for row in reader:
            if int(row[2]) == int(interval[x]):
                if day % 7 < 5:
                    try:
                        numStep = int(row[0])
                    except ValueError:
                        day += 1
                        continue
                    else:
                        weekdayTotal += numStep
                        weekdayCount += 1
                        day += 1
                else:
                    try:
                        numStep = int(row[0])
                    except ValueError:
                        day += 1
                        continue
                    else:
                        weekendTotal += numStep
                        weekendCount += 1
                        day += 1
        try:
            weekendAvg.append(weekendTotal/weekendCount)
        except ZeroDivisionError:
            weekendAvg.append(0)
        try:
            weekdayAvg.append(weekdayTotal/weekdayCount)
        except ZeroDivisionError:
            weekdayAvg.append(0)
        day = 0
        weekdayTotal = 0
        weekendTotal = 0
        weekdayCount = 0
        weekendCount = 0

plt.scatter(interval,weekendAvg,cmap = plt.cm.Blues,s=40)
plt.scatter(interval,weekdayAvg,cmap = plt.cm.Greens,s=40)
plt.legend(["weekend step avg","weekday step avg"])
plt.xlabel("interval",fontsize = 15)
plt.ylabel("Average steps",fontsize = 14)
plt.axis([0,2400,0,300])
plt.show()