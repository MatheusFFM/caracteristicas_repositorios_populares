import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum


class Rows(Enum):
    AGE = 1
    TOTAL_PR_ACCEPTS = 2
    TOTAL_RELEASES = 3
    LAST_UPDATE_MINUTES = 4
    CLOSED_ISSUES_RATIO = 6


def generate_chart(filename, name, values):
    df = pd.DataFrame(values,
                      columns=[name])
    boxplot = df.boxplot(column=[name], by='X', layout=(2, 1))
    plt.savefig(f"{filename}.png")


ages = []
total_pr_accepts = []
total_releases = []
last_update_minutes = []
closed_issues_ratio = []

with open('repositories.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            line_count += 1
        elif line_count % 2 == 0:
            ages.append(int(row[Rows.AGE.value]))
            total_pr_accepts.append(int(row[Rows.TOTAL_PR_ACCEPTS.value]))
            total_releases.append(int(row[Rows.TOTAL_RELEASES.value]))
            last_update_minutes.append(float(row[Rows.LAST_UPDATE_MINUTES.value]))
            if row[Rows.CLOSED_ISSUES_RATIO.value] != '':
                closed_issues_ratio.append(float(row[Rows.CLOSED_ISSUES_RATIO.value]))
            line_count += 1
        else:
            line_count += 1
    print(f'Processed {line_count} lines.')

print("Creating charts...")
assd = max(ages)
assd = max(total_pr_accepts)
assd = max(total_releases)
assd = max(last_update_minutes)
assd = max(closed_issues_ratio)
generate_chart("Age", "Age in days", ages)
generate_chart("PR", "Total PR accepts", total_pr_accepts)
generate_chart("Releases", "Total releases", total_releases)
generate_chart("LastUpdate", "Last update in minutes", last_update_minutes)
generate_chart("ClosedIssues", "Closed issues ratio", closed_issues_ratio)
