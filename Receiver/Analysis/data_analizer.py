from tinydb import TinyDB
from datetime import datetime
import csv

db = TinyDB('local_save.json')

previous = 0
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Date timestamp", "Diff with previous"])
    for item in db:
        date_string = item["output"]["sent_time"]
        date_timestamp = datetime.strptime(date_string, "%m/%d/%Y, %H:%M:%S").timestamp()
        diff = 0 if previous == 0 else date_timestamp - previous
        writer.writerow([date_string, date_timestamp, diff])
        previous = date_timestamp
