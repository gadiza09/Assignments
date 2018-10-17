import csv

from datetime import datetime

import pygal

filename = "activity.csv"
with open(filename) as f:

    reader = csv.reader(f)
    header_row = next(reader)

    steps = []
    stepping = 0
    current_date = 0
    for row in reader:
        current_dates = datetime.strptime(row[1], "%Y-%m-%d")
        if current_dates == current_date:
            if row[0] != "NA":
                step = int(row[0])
                stepping += step

        else:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            steps.append(stepping)
            stepping = 0
            if row[0] != "NA":
                step = int(row[0])
                stepping += step

    steps.append(stepping)

del steps[0]
print(steps)


hist = pygal.Bar()
hist.title = "Number of Steps"
hist.x_title = "Days"
hist.y_title = "Steps"
hist.add("Steps", steps)
hist.render_to_file("histogram.svg")


mean = sum(steps) // len(steps)
print("The mean is: " + str(mean))

sortedSteps = sorted(steps)
median = (sortedSteps[30])
print("The median is: " + str(median))


