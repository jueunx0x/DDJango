import pymongo
from django.shortcuts import render

from ai.run_trash_classifier import prediction
from ai.models import Image
from ai.forms import ImageForm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib,base64
# Create your views here.
connect_string = 'mongodb+srv://jueun:shin7088@cluster0.chugj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

from django.conf import settings

my_client = pymongo.MongoClient(connect_string)

# First define the database name
dbname = my_client['myFirstDatabase']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["seoul_graph"]
seoul_graph = collection_name.find({})
string_amount = []
gu = []
for i in seoul_graph:
    string_amount.append(i["Amount"])
    gu.append(i["Gu"])
string_amount.pop()
string_amount.pop()
int_list = list(map(float, string_amount))
print(int_list)
print(gu)
#
#
# a=np.array(wonjinkiup)
# b=np.array(kwangmeong)
# c=np.array(hanil)
# d=np.array(daejung)
# e=np.array(wonjin)
# f=np.array(nambu)
# g=np.array(anhueng)
# plt.plot(a)
# plt.plot(b,'b')
# plt.plot(c,'g')
# plt.plot(d,'c')
# plt.plot(e,'m')
# plt.plot(f,'y')
# plt.plot(g,'k')
# plt.show()

def graphinfo(request):
    connect_string = 'mongodb+srv://jueun:shin7088@cluster0.chugj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

    from django.conf import settings
    my_client = pymongo.MongoClient(connect_string)

    # First define the database name
    dbname = my_client['myFirstDatabase']

    # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
    collection_name = dbname["graph_info"]

    # Check the count

    # Read the documents
    graph_info = collection_name.find({})
    wonjin = []
    hanil = []
    nambu = []
    anhueng = []
    kwangmeong = []
    wonjinkiup = []
    daejung = []
    monthly=[]

    for r in graph_info:
        if r["ACTING_ENTRPS_NM"] == '원진기업㈜':
            monthly.append(r["YM"])

            wonjinkiup.append(r["MT_ACCTO_TKAWAY_QTY"])
    graph_info = collection_name.find({})
    for r in graph_info:
        if r["ACTING_ENTRPS_NM"] == '광명산업㈜':
            # kwangmeong.append(r["YM"])
            kwangmeong.append(r["MT_ACCTO_TKAWAY_QTY"])
    graph_info = collection_name.find({})
    for r in graph_info:
        if r["ACTING_ENTRPS_NM"] == '㈜한일기연':
            # hanil.append(r["YM"])
            hanil.append(r["MT_ACCTO_TKAWAY_QTY"])
    graph_info = collection_name.find({})
    for r in graph_info:
        if r["ACTING_ENTRPS_NM"] == '㈜대정':
            # daejung.append(r["YM"])
            daejung.append(r["MT_ACCTO_TKAWAY_QTY"])
    graph_info = collection_name.find({})
    for r in graph_info:
        if r["ACTING_ENTRPS_NM"] == '원진(주)':
            # wonjin.append(r["YM"])
            wonjin.append(r["MT_ACCTO_TKAWAY_QTY"])
    graph_info = collection_name.find({})
    for r in graph_info:
        if r["ACTING_ENTRPS_NM"] == '남부환경(주)':
            monthly.append(r["YM"])
            nambu.append(r["MT_ACCTO_TKAWAY_QTY"])
    graph_info = collection_name.find({})
    for r in graph_info:
        if r["ACTING_ENTRPS_NM"] == '안흥정화(주)':
            # anhueng.append(r["YM"])
            anhueng.append(r["MT_ACCTO_TKAWAY_QTY"])
    wonjin = list(reversed(wonjin))
    wonjinkiup = list(reversed(wonjinkiup))
    hanil = list(reversed(hanil))
    daejung = list(reversed(daejung))
    kwangmeong = list(reversed(kwangmeong))
    nambu = list(reversed(nambu))
    anhueng = list(reversed(anhueng))
    monthly = list(reversed(monthly))
    # print(wonjin)
    # print(monthly)

    a = np.array(wonjinkiup)
    b = np.array(kwangmeong)
    c = np.array(hanil)
    d = np.array(daejung)
    e = np.array(wonjin)
    f = np.array(nambu)
    g = np.array(anhueng)
    # plt.plot(a)
    # plt.plot(b, 'b')
    # plt.plot(c, 'g')
    # plt.plot(d, 'c')
    # plt.plot(e, 'm')
    # plt.plot(f, 'y')
    # plt.plot(g, 'k')
    # Print on the terminal
    return render(request,'ai/ai.html',{'monthly':monthly,'wonjin': wonjin ,'hanil':hanil,'nambu':nambu,'anhueng': anhueng,'kwangmeong': kwangmeong,'wonjinkiup': wonjinkiup,'daejung': daejung})

def seoul_graph(request):
    connect_string = 'mongodb+srv://jueun:shin7088@cluster0.chugj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

    from django.conf import settings
    my_client = pymongo.MongoClient(connect_string)

    # First define the database name
    dbname = my_client['myFirstDatabase']

    # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
    collection_name = dbname["seoul_graph"]
    seoul_graph = collection_name.find({})
    string_amount = []
    gu = []
    for i in seoul_graph:
        string_amount.append(i["Amount"])
        gu.append(i["Gu"])
    string_amount.pop()
    string_amount.pop()
    int_list = list(map(float, string_amount))


    return render(request,'ai/seoul_graph.html',{'int_list':int_list,'gu':gu} )
def AI(request):
    # global result
    # if request.method=='POST':
    #     form=ImageForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         imagetitle = request.POST["imagename"]
    #         image = request.FILES["image"]
    #         imgs = Image(title=imagetitle, imagefile=image)
    #         imgs.save()
    #         result = prediction(image_path='./image/imagetitle.jpg')
    # return render(request,'ai/ai.html',{'x': x})
    return render(request,'ai/ai.html')
