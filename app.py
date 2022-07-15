from library.dbmongo import DbMongo

db = DbMongo("localhost","bancoteste", 27017)
res = db.select("users")

print(res)

#para selecionar
res = db.select("users", {"email":'teste@malbizer.com.br'})
print(res)