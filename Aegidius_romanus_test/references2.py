import re
import csv
import codecs


def readfile(filename):
    manuscrits = []
    ref = []
    with codecs.open(filename, 'rb', "utf-8") as txt:
        for ligne in txt:
            lgn = re.sub(r"[\"\n]+",r"", ligne)
            if re.match(r"^[\t\s]+<99b>.+",lgn):
                lgn = re.sub(r"^[\t\s]+(<99)","\\1",lgn)
                ref.append(lgn)
            elif re.match(r"^[\t\s]+<99c>.+",lgn):
                lgn = re.sub(r"^[\t\s]+(<99)","\\1",lgn)
                manuscrits.append(lgn)
    return ref,manuscrits


def listreferences(texte):
    articles = []
    monographies = []
    for element in texte:
        elt = re.sub(r"<99b>\s+", r"", element)
        regex = "\w+\s+\([\w\.\-]+\),\s+\w.*"
        if re.match(regex, elt):
            articles.append(elt)
        else:
            monographies.append(elt)
    return articles, monographies

def formalisationarticle(listearticles):
    res = []
    for elt in listearticles :
        regex = "^(\w+\s*\([\w\.\-]+\)),\s*(\w.+),\s*[dans|in]*\s*\&(.+)\&(.+)"
        elementref = re.match(regex,elt)
        if elementref is not None:
            date = re.sub(r"[A-Za-z0-9èïöüûôêëé,\s\(\)\-'\.\/;]+\s*(\d{4})\)*,*.*", r"\1", elementref.group(4))
            page = re.sub(r".*(\d+\-\d+).*", r"\1", elementref.group(4))
            if len(date) != 4 :
                date = ""
            if not re.match(r"\d+\-\d+",page):
                page = ""
            res.append(['?', str(elementref.group(1)),str(elementref.group(2)),  str(elementref.group(3)), str(date), str(page)])
        else:
#            print(elt)
            pass
    return res

def enregistrer(outfile, data):
    with open (outfile, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["xml-ref","Author_name", "Titre_Article", "Periodic_title", "Print_Date", "pages"])
        writer.writerows(data)




articleoutfile="aegidius_bibliography_articles.csv"
f = "aegidiusRomanus_complete.txt"
texte = readfile(f)
articles, monographies = listreferences(texte[0])
print("Il y a " + str(len(articles)) + " articles.")
print("Il y a " + str(len(monographies)) + " monographies.")

res = formalisationarticle(articles)
enregistrer(articleoutfile, res)
