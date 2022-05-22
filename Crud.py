from pymongo import MongoClient
client = MongoClient('localhost',27017)  # 27017 is the default port number for mongodb
db = client.Space

col = db.Expeditions
#Create 

#Insert One
db.Expeditions.insert_one({
    name: "Voyager 1",
    date: "6/10/2021",
    agency: "NASA"
})
#Insert Many
#db.Expeditions.insert_many([{},
#     {}])

#READ

#db.Expeditions.find()

#db.Space.find_one({query}, {projection})
#db.SalesDB.find({"orderdate":"8/10/2021"})

#Update

#db.Space.update_one({name: "Voyager 1"}, {$set:{agency:"NASA,ESA"}})

#db.SalesDB.update_many({species:"Dog"}, {$set: {age: "5"}})

#Replace

#db.Space.replace_one({name: "Voyager 1"}, {name: "Space 1"})

#DELETE

#db.Space.delete_one({name:"Voyager 1"})

#db.Space.delete_many({agency:"NASA"})