import mysql.connector

username = input("Enter your username: ")
password = input("Enter your password: ")

# Connexion à la base de données
cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='testdb')
cursor = cnx.cursor()

# Requête SQL dangereuse avec injection
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
cursor.execute(query)

# Affichage des résultats
print(cursor.fetchall())

cursor.close()
cnx.close()
