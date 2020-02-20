import re
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
    '''
    Cette fonction va prendre le texte de la notice et renvoyer 2
    listes : articles,  monographies
    '''
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
    for elt in listearticles :
        regex = "(\w+\s+\([\w\.\-]+\)),(\s+\w.+),\s\&(.+)\&"
        elementref = re.match(regex,elt)
        if elementref is not None:
            print("Auteur : " +  str(elementref.group(1)))
            print("Titre : " + str(elementref.group(2)))
            print("Revue : " + str(elementref.group(3)))



f = "aegidiusRomanus_complete.txt"
texte = readfile(f)

articles, monographies = listreferences(texte[0])
print(articles)
print("Il y a " + str(len(articles)) + " articles.")
formalisationarticle(articles)
