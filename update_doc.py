import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def update_document(document):
	try:
		result=collection.update_one(document, {"$set" : {"keyName" : "test value data updated"}})
	except ValidationError as ve:
		abort(400, str(ve))
	return result;

def main():

	updateDoc = { "keyName" : "test value data"}

	print update_document(updateDoc)
    

main()
