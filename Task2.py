"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


max_time = 0
longest_phone_number = None
phone_dict = {}

for row in calls:
    duration = int(row[3])
    if row[0] in phone_dict:
        phone_dict[row[0]] += duration
    else:
        phone_dict[row[0]] = duration

    if row[1] in phone_dict:
        phone_dict[row[1]] += duration
    else:
        phone_dict[row[1]] = duration


for key in phone_dict:
    if phone_dict[key] > max_time:
        max_time = phone_dict[key]
        longest_phone_number = key

print(f"{longest_phone_number} spent the longest time, {max_time} seconds, on the phone during September 2016.")