import csv

with open ('Aquin_bibliography.txt', 'r') as file:
    stripped = (line.strip() for line in file)
    lines = (line.split(",") for line in stripped if line)
    with open ('Aquin_bibliography.csv', 'w') as csv_file:
        writer=csv.writer(csv_file)
        witer.writerow(('xml-ref','Author', 'Article_title', 'Periodic_title', 'Volume', 'DateOfPrintPublication', 'pages'))
