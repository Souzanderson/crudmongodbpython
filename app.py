from library.dbmongo import DbMongo

db = DbMongo("mongodb+srv://anderson:159248@cluster0.7j0tz.mongodb.net/test","bancoteste", 27017)
res = db.select("users")

print(res)

#para selecionar
res = db.select("users", {"email":'teste@malbizer.com.br'})
print(res)