"""
Клас datetime.timedelta – різниця між двома моментами часу, з точністю до мікросекунд.
"""

from datetime import datetime, timedelta

d = datetime.now()

interval = timedelta(days=4)
finish_date = d - interval
print(finish_date)


# birth_date = datetime(1988, 5, 20)
# uptime = datetime.now() - birth_date
# print(uptime)