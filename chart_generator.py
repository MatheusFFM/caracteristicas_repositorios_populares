import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum


class Rows(Enum):
    AGE = "Age"
    TOTAL_PR_ACCEPTS = "Total PR Accepts"
    TOTAL_RELEASES = "Total Releases"
    LAST_UPDATE_MINUTES = "Last Updated Interval in Minutes"
    CLOSED_ISSUES_RATIO = "Closed Issues Ratio"


def generate_chart(origin, column, filename):
    origin.boxplot(column=column)
    plt.savefig(f"{filename}.png")
    plt.close()


data = pd.read_csv("repositories.csv")
for row in Rows:
    print(f"Creating {row.value} boxplot")
    generate_chart(data, row.value, row.value.replace(" ", ""))
