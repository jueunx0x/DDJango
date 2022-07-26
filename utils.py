import pymongo
connect_string = 'mongodb+srv://jueun:shin7088@cluster0.chugj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

from django.conf import settings
my_client = pymongo.MongoClient(connect_string)

# First define the database name
dbname = my_client['myFirstDatabase']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["trashcanlocation"]

# Check the count
count = collection_name.count()
print(count)

# Read the documents
trashcan_detail = collection_name.find({})
# Print on the terminal
for r in trashcan_detail:
    print(r["detail"])
