import csv

from matplotlib import pyplot as plt

filename = "activity.csv"
with open(filename) as f:

    reader = csv.reader(f)
    header_row = next(reader)

    dictPattern = {}
    for row in reader:
        if row[0] == "NA":
            continue

        else:
            dictPattern.setdefault(row[2], [])
            dictPattern[row[2]].append(int(row[0]))


intervals = []
for keys in dictPattern:
    intervals.append(int(keys))


averageSteps = []
for interval, step in dictPattern.items():
    averageSteps.append(int(sum(step) / len(step)))


plt.plot(intervals, averageSteps)
plt.title("Daily Activity Pattern")
plt.xlabel("Intervals")
plt.ylabel("Average Steps")
plt.show()


maxValue = max(averageSteps)
maxIndex = int((averageSteps.index(maxValue)))
maxIntervals = intervals[maxIndex]

print("The 5 minute interval with the most number of steps is: " + str(maxIntervals))

