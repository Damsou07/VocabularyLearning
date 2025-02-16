# init database
database = {
    "word" : [],
    "translation" : [],
}

# ouverture du ficier
with open("extractData/brutData_html.txt", 'r', encoding="utf-8") as file:
    data_html = file.readlines()


# il faut batch les données car une il y a une récurance des <td> de 4 en 4 pour les données qui nous intéressent;
# à condition de suprimer les balises <td></td> vide et de corriger des problemes qui viens casser l'algorithme

# init loop settings
batch_count = 0
batch_data = []

# traitement des données
for i in range(len(data_html)):
    if ("<td>" in data_html[i] and "<td></td>" not in data_html[i]):
        # print(data_html[i])  # -test

        # correction du bug pour le batch du mot mm-hmm
        if ("mm-hmm" in data_html[i]):
            batch_data.append(data_html[i])
            batch_data.append('none')
            batch_count += 2

        # correction du bug pour le batch many ou munch
        elif ("many-ou-much" in data_html[i]):
            batch_data.append("<td>many/much</td>")
            batch_count += 1

        else:
            batch_data.append(data_html[i])
            batch_count += 1


        if batch_count == 4:
            # print(batch_data) # -test 

            # remplir la base de données
            database["word"].append(batch_data[0])
            database["translation"].append(batch_data[2])
                
            # reset loop settings
            batch_data = []
            batch_count = 0


print(database)