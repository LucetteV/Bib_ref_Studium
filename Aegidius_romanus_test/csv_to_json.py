import csv
import json

csv_file = open('aegidius_bibliography_articles.csv', 'r')
json_file = open('aegidius_bibliography_articles.json', 'w')

rowfields = ("id", "Author_name", "Titre_Article", "Periodic_title", "Print_Date", "pages")
reader = csv.DictReader(csv_file, rowfields)
out = json.dumps([row for row in reader])
json_file.write(out)
