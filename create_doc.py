import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def insert_document(document):

	try:
		result=collection.save(document)
	except ValidationError as ve:
		abort(400, str(ve))
	return result, True;

def main():

	myDocument = { "keyName" : "test value data"}

	print insert_document(myDocument)
    

main()
