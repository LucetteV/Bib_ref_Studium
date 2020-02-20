import csv
import json

csvAquin = open('Articles_Persee.csv', 'r')
jsonAquin = open('Articles_Persee.json', 'w')

rowfields = ("URL", "Titre_Article", "keyWords", "Print_Date", "Author_name", "Author_givenName", "Periodic_title")
reader = csv.DictReader(csvAquin, rowfields)
out = json.dumps([row for row in reader])
jsonAquin.write(out)
