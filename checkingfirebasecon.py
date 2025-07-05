import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

try:
    # Initialize Firebase Admin SDK with service account credentials
    cred = credentials.Certificate(r"C:\Users\bilal\OneDrive\Desktop\DBMS_Semester_Project\serviceAcccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://dbmssemesterproject-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
    print("Firebase initialization successful.")
except Exception as e:
    print("Firebase initialization failed:", e)

try:
    # Write data to Firebase
    firebase_ref = db.reference('test_data')
    firebase_ref.set({'message': 'Connection successful!'})
    print("Data written to Firebase successfully.")

    # Read data from Firebase
    data = firebase_ref.get()
    print("Data read from Firebase:", data)
except Exception as e:
    print("Firebase data operation failed:", e)
