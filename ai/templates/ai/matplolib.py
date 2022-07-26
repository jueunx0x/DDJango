import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib,base64

import pymongo

connect_string = 'mongodb+srv://jueun:shin7088@cluster0.chugj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

from django.conf import settings
my_client = pymongo.MongoClient(connect_string)

# First define the database name
dbname = my_client['myFirstDatabase']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["graph_info"]

# Check the count
count = collection_name.count()
print(count)
# Read the documents
graph_info = collection_name.find({})
wonjin=[]
hanil=[]
nambu=[]
anhueng=[]
kwangmeong=[]
wonjinkiup=[]
daejung=[]

for r in graph_info:
    if r["ACTING_ENTRPS_NM"] == '원진기업㈜':
        # wonjinkiup.append(r["YM"])
        wonjinkiup.append(r["MT_ACCTO_TKAWAY_QTY"])
graph_info = collection_name.find({})
for r in graph_info:
    if r["ACTING_ENTRPS_NM"] == '광명산업㈜':
        kwangmeong.append(r["YM"])
        kwangmeong.append(r["MT_ACCTO_TKAWAY_QTY"])
graph_info = collection_name.find({})
for r in graph_info:
    if r["ACTING_ENTRPS_NM"] == '㈜한일기연':
        hanil.append(r["YM"])
        hanil.append(r["MT_ACCTO_TKAWAY_QTY"])
graph_info = collection_name.find({})
for r in graph_info:
    if r["ACTING_ENTRPS_NM"] == '㈜대정':
        daejung.append(r["YM"])
        daejung.append(r["MT_ACCTO_TKAWAY_QTY"])
graph_info = collection_name.find({})
for r in graph_info:
    if r["ACTING_ENTRPS_NM"] == '원진(주)':
        wonjin.append(r["YM"])
        wonjin.append(r["MT_ACCTO_TKAWAY_QTY"])
graph_info = collection_name.find({})
for r in graph_info:
    if r["ACTING_ENTRPS_NM"] == '남부환경(주)':
        nambu.append(r["YM"])
        nambu.append(r["MT_ACCTO_TKAWAY_QTY"])
graph_info = collection_name.find({})
for r in graph_info:
    if r["ACTING_ENTRPS_NM"] == '안흥정화(주)':
        anhueng.append(r["YM"])
        anhueng.append(r["MT_ACCTO_TKAWAY_QTY"])


a=np.array(wonjinkiup["YM"])
plt.plot(a)

plt.show()