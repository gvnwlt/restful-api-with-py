import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def read_document(document):
	try:
		result=collection.find_one(document)
	except ValidationError as ve:
		abort(400, str(ve))
	return result;

def main():

	findDocument = { "keyName" : "test value data"}

	print read_document(findDocument)
    

main()
