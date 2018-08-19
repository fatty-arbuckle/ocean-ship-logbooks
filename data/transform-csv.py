import csv

with open("CLIWOC15.csv", 'r') as csvIN:
    with open('ship-data.csv', 'wb') as csvOUT:
        writer = csv.writer(csvOUT, delimiter=',', quoting=csv.QUOTE_ALL)
        for line in csv.reader(csvIN, delimiter=','):
            line = [str(x).replace('\n', '').encode('utf-8') for x in line]
            for y in line:
                print(type(line))
            writer.writerow(line)
