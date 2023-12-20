from arango import ArangoClient

# Initialise the ArangoDB Client
client = ArangoClient(hosts="http://localhost:8529/")

sys_db = client.db('_system', username='root', password='arango')

# Create a new database named "test" if it does not exist.
if not sys_db.has_database('test'):
    sys_db.create_database('test')

# Connect to "test" database as root user.
# This returns an API wrapper for "test" database.
db = client.db('test', username='root', password='arango')

# Create a new collection named "students" if it does not exist.
# This returns an API wrapper for "students" collection.
if db.has_collection('students'):
    students = db.collection('students')
else:
    students = db.create_collection('students')

# Add a hash index to the collection.
students.add_hash_index(fields=['name'], unique=False)

# Truncate the collection.
students.truncate()

# Insert new documents into the collection.
students.insert({'name': 'jane', 'age': 19})
students.insert({'name': 'josh', 'age': 18})
students.insert({'name': 'jake', 'age': 21})

# Execute an AQL query. This returns a result cursor.
cursor = db.aql.execute('FOR doc IN students RETURN doc')

# Iterate through the cursor to retrieve the documents.
student_names = [document['name'] for document in cursor]
student_names
