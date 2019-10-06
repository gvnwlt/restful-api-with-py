import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def delete_document(document):
	try:
		result=collection.delete_one(document)
	except ValidationError as ve:
		abort(400, str(ve))
	return result;

def main():

	deleteDoc = { "keyName" : "test value data"}

	print delete_document(deleteDoc)
    

main()
