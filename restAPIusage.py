#!/usr/bin/python
import json
from bson import json_util
from flask import Flask, request
from pymongo import MongoClient
import datetime
import string
from collections import OrderedDict
import bottle
from bottle import request, route, run, abort, response, post

# set up URI paths for REST service
@route('/currentTime', method='GET')
def get_currentTime():
 dateString=datetime.datetime.now().strftime("%Y-%m-%d")
 timeString=datetime.datetime.now().strftime("%H:%M:%S")
 string="{\"date\":"+dateString+",\"time\":"+timeString+"}"
 return json.loads(json.dumps(string, indent=4, default=json_util.default))

@route('/hello', method='GET')
def hello_world():
  try: 
    request.query.name
    name=request.query.name
    if name:
      string="{\"hello\": \""+request.query.name+"\"}"
      print(' [{0}] OK'.format(response.status_code))
    else:
      string="{\"404 Not Found\"}"
      print(' [400] Not Found'.format(response.status_code))
  except NameError:
    abort(404, 'Not Found')
      
  return json.loads(json.dumps(string, indent=4, default=json_util.default))

@route('/strings', method='POST')
def hello_world():
  try: 
    first = request.json.get("string1")
    second = request.json.get("string2")
    string = "{{first: \"{first}\", second: \"{second}\"}}".format(first=first, second=second)
  except NameError:
    abort(404, 'Not Found')
      
  return json.loads(json.dumps(string, indent=4, default=json_util.default))

@route('/create', method='POST')
def insert_document():
  try:
    sector = request.json.get("sector")
    result = request.json.get("result")
    date = request.json.get("date")
    business_name = request.json.get("business_name")
    certificate_number = request.json.get("certificate_number")
    id_ = request.json.get("id")
    document = "{{\"id\": \"{id_}\", \"certificate_number\": \"{certificate_number}\", \"business_name\": \"{business_name}\", \"date\": \"{date}\", \"result\": \"{result}\", \"sector\": \"{sector}\"}}".format(id_=id_, certificate_number=certificate_number, business_name=business_name, date=date, result=result, sector=sector)
    document = json.loads(document)
    connection = MongoClient('localhost', 27017)
    db = connection['city']
    collection = db['inspections']
    result=collection.save(document)
  except NameError as e:
    abort(400, str(e))
  return json.loads(json.dumps(document, indent=4, default=json_util.default))

@route('/read', method='GET')
def read_document():
  try:
    request.query.business_name
    business_name=request.query.business_name
    connection = MongoClient('localhost', 27017)
    db = connection['city']
    collection = db['inspections']
    document = {"business_name" : business_name}
    result=collection.find_one(document)
  except ValidationError as ve:
		abort(400, str(ve))
  return json.loads(json.dumps(result, indent=4, default=json_util.default))

#app = Flask(__name__)

@route('/update')
def update():
  try:
    id_ = request.query.id
    result = request.query.result 
    connection = MongoClient('localhost', 27017)
    db = connection['city']
    collection = db['inspections']
    document = {"id" : id_}
    result=collection.update_one(document, {"$set" : {"result" : result}})
  except :
    abort(400)
  return id_

@route('/delete')
def delete_document():
  try:
    id_ = request.query.id
    document = {"id" : id_}
    connection = MongoClient('localhost', 27017)
    db = connection['city']
    collection = db['inspections']
    result=collection.delete_one(document)
  except ValidationError as ve:
    abort(400, str(ve))
  return result;

if __name__ == "__main__":
 #app.run(host='localhost', port=8080, debug=True)
 run(host='localhost', port=8080)
 
 