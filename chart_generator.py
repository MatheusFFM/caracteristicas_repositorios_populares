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


def generate_chart_by_language(origin, column, filename, group):
    origin.boxplot(column=column,
                   by=[group],
                   rot=90,
                   grid=False,
                   fontsize=5,)
    plt.savefig(f"{filename}.png")
    plt.close()


data = pd.read_csv("repositories.csv")
for row in Rows:
    print(f"Creating {row.value} boxplot")
    generate_chart(data, row.value, row.value.replace(" ", ""))

print("Creating boxplot for each language")
generate_chart_by_language(data, Rows.LAST_UPDATE_MINUTES.value, "popularLanguagesUpdates", "Language")
generate_chart_by_language(data, Rows.TOTAL_RELEASES.value, "popularLanguagesReleases", "Language")
generate_chart_by_language(data, Rows.TOTAL_PR_ACCEPTS.value, "popularLanguagesPR", "Language")
