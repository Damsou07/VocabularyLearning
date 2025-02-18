import re
import json

# init database
database = []

# ouverture du ficier
with open("public/extractData/brutData_html.txt", 'r', encoding="utf-8") as file:
    data_html = file.readlines()


# il faut batch les données car une il y a une récurance des <td> de 4 en 4 pour les données qui nous intéressent;
# à condition de suprimer les balises <td></td> vide et de corriger des problemes qui viens casser l'algorithme

# init loop settings
batch_count = 0
batch_data = []

# Supprime <td> et </td> et les ()
def cleaningData(data):
    cleaned_data = re.sub(r"</?td>", "", data)
    cleaned_data = re.sub(r"\n", "", cleaned_data)
    cleaned_data = re.sub(r"\s*\(.*?\)\s*", "", cleaned_data)

    # Vérifie si une virgule est présente, si oui, split et retourne un tableau
    if "," in cleaned_data:
        return [item.strip() for item in cleaned_data.split(",")]

    return [cleaned_data]


# traitement des données
for i in range(len(data_html)):
    if ("<td>" in data_html[i] and "<td></td>" not in data_html[i]):
        # print(data_html[i])  # -test

        # correction du bug pour le batch many ou munch
        if ("many-ou-much" in data_html[i]):
            batch_data.append("<td>many/much</td>")
            batch_count += 1

        # correction de it
        elif ("chose inanimée" in data_html[i]):
            batch_data.append("<td>il</td>")
            batch_count += 1

        # quelques ajouts apres test de l'applis mais je ne peux pas gerer tout les cas ou il manquerait des traductions pertinantes !
        elif ("marrant" in data_html[i]):
            batch_data.append("<td>marrant, drôle</td>")
            batch_count += 1

        elif ("entreprise" in data_html[i]):
            batch_data.append("<td>entreprise, compagnie</td>")
            batch_count += 1

        elif ("recevoir" in data_html[i]):
            batch_data.append("<td>recevoir, obtenir</td>")
            batch_count += 1

        elif ("cœur" in data_html[i]):
            batch_data.append("<td>cœur, coeur</td>")
            batch_count += 1

        # retirer les mots non valides
        elif ("fuck" in data_html[i] or '<td>s</td>\n' == data_html[i] or '<td>to</td>\n' == data_html[i]):
            # print(data_html[i])  # -test
            batch_data.append("<td>****</td>")
            batch_count += 1

        else:
            batch_data.append(data_html[i])
            batch_count += 1


        if batch_count == 4:
            # print(batch_data) # -test 

            # remplir la base de données
            if ("****" in batch_data[0]):
                True # ne rien faire

            else:
                database.append({"en" : cleaningData(batch_data[0]), "fr" : cleaningData(batch_data[2])})

            # reset loop settings
            batch_data = []
            batch_count = 0


# print(database) # -test

# Sauvegarde les données nettoyées dans un fichier JSON
with open("public/extractData/cleanData.json", "w", encoding="utf-8") as json_file:
    json.dump(database, json_file, ensure_ascii=False, indent=4)

print("✅ Données exportées dans cleanData.json")