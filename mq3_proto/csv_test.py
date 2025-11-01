import csv

csv_file = open("test.csv", "w", newline="")
writer = csv.writer(csv_file)
writer.writerow(["count", "csv"])
writer.writerow([1, 2])
