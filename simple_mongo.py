import pymongo

uri = "mongodb://127.0.0.1:27017"  # DB server address
client = pymongo.MongoClient(uri)  # Reference to the DB client
database = client['udemypyweb']   # Rerefence to the specific DB we want to use
collection = database['students'] # Reference to the specific collection we want to use

students = [student for student in collection.find({})]  # Put all student objects from collection to students list

# For each student in collection, find mark, put in a list
student_marks = [student['mark'] for student in collection.find({})]

# This list queries DB with a condition
student_marks_2 = [student['mark'] for student in collection.find({}) if student['mark'] == 100]

print(students)
print(student_marks)
