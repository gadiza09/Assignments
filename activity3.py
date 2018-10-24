import csv

import pygal

from datetime import datetime

filename = "activity.csv"
with open(filename) as f:

    reader = csv.reader(f)
    header_row = next(reader)

    missing = 0
    for row in reader:
        if row[0] == "NA":
            missing +=1

    print("The number of missing values is: " + str(missing))

filename = "activity.csv"
with open(filename) as f1:

    reader1 = csv.reader(f1)
    header_row = next(reader1)

    newSteps = []
    stepping = 0
    current_date = 0
    for row in reader1:
        current_dates = datetime.strptime(row[1], "%Y-%m-%d")
        if current_dates == current_date:
            if row[0] != "NA":
                step = int(row[0])
                stepping += step

        else:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            newSteps.append(stepping)
            stepping = 0
            if row[0] != "NA":
                step = int(row[0])
                stepping += step

    newSteps.append(stepping)

hist = pygal.Bar()
hist.title = "Number of Steps"
hist.x_title = "Days"
hist.y_title = "Steps"
hist.add("Steps", newSteps)
hist.render_to_file("histogramTotalSteps2.svg")


mean = sum(newSteps) // len(newSteps)
print("The mean is: " + str(mean))

sortedSteps = sorted(newSteps)
median = (sortedSteps[30])
print("The median is: " + str(median))
