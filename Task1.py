"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

nums_set = set()

for row in texts:
    nums_set.add(row[0])
    nums_set.add(row[1])

for row in calls:
    nums_set.add(row[0])
    nums_set.add(row[1])

print(f"There are {len(nums_set)} different telephone numbers in the records.")

# 570

