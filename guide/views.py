from django.shortcuts import render
# import csv
# with open('static/csv/recycle_final.csv')as csv_file:
#     rows=csv.reader(csv_file,delimiter=',')
#     for row in rows:
#         print(row)
# Create your views here.
def guide(request):
    return render(request,'guide/guide.html')
def paper(request):
    return render(request, 'guide/paper.html')
def plastic(request):
    return render(request, 'guide/plastic.html')
def vinyl(request):
    return render(request, 'guide/vinyl.html')
def metal(request):
    return render(request, 'guide/metal.html')
def glass(request):
    return render(request, 'guide/glass.html')
def styrofoam(request):
    return render(request, 'guide/styrofoam.html')
def etc(request):
    return render(request, 'guide/etc.html')

#guide

import pymongo
# connect_string = 'mongodb+srv://jueun:shin7088@cluster0.chugj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
#
# from django.conf import settings
# my_client = pymongo.MongoClient(connect_string)
#
# # First define the database name
# dbname = my_client['myFirstDatabase']
#
# # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
# collection_name = dbname["recycle_guide"]
#
# # Check the count
# count = collection_name.count()
# print(count)
#
# # Read the documents
# trashcan_detail = collection_name.find({})
# # Print on the terminal
def guideinfo(request):
    connect_string = 'mongodb+srv://jueun:shin7088@cluster0.chugj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

    from django.conf import settings
    my_client = pymongo.MongoClient(connect_string)

    # First define the database name
    dbname = my_client['myFirstDatabase']

    # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
    collection_name = dbname["recycle_guide"]

    # Check the count

    # Read the documents
    recycle_detail = collection_name.find({})

    # Print on the terminal
    return render(request,'guide/guide_list.html',{'recycle_detail':recycle_detail})