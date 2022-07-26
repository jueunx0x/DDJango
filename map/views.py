from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
#mongodb

import pymongo
# connect_string = 'mongodb+srv://jueun:shin7088@cluster0.chugj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# from django.conf import settings
# my_client = pymongo.MongoClient(connect_string)
#
# # First define the database name
# dbname = my_client['myFirstDatabase']
#
# # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
# collection_name = dbname["trashcanlocation"]
#
# # Check the count
# count = collection_name.count()
# print(count)
#
# # Read the documents
# trashcan_detail = collection_name.find({})
# #Print on the terminal
# a=[]
# for r in trashcan_detail:
#     print(r["detail"])
#     a.append(r["detail"])
def detail(request):
    connect_string = 'mongodb+srv://jueun:shin7088@cluster0.chugj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    from django.conf import settings
    my_client = pymongo.MongoClient(connect_string)

    # First define the database name
    dbname = my_client['myFirstDatabase']

    # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
    collection_name = dbname["trashcanlocation"]

    # Check the count
    count = collection_name.count()

    # Read the documents
    trashcan_detail = collection_name.find({})
    a=[]
    for r in trashcan_detail:
        a.append(r["detail"])
    # for r in trashcan_detail:
    #     r["detail"]
    # Print on the terminal

    return render(request,'map/map.html', {'a': a })
def map(request):
    return render(request,'map/map.html')
def marker(request):
    return render(request,'map/marker.html')

