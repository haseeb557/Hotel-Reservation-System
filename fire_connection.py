import psycopg2
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate(r"C:\Users\bilal\OneDrive\Desktop\DBMS_Semester_Project\serviceAcccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://dbmssemesterproject-default-rtdb.asia-southeast1.firebasedatabase.app/'})

# Establish connection to SQL database
db_connection = psycopg2.connect(
    host="localhost",
    database="hoteldb",
    user="postgres",
    password="pgadmin4"
)

# Function to sync data from SQL database to Firebase Realtime Database
def sync_data():
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM reservation")
        reservations = cursor.fetchall()

        # Convert SQL data to Firebase format and update Firebase database
        firebase_ref = db.reference('reservations')
        for reservation in reservations:
            firebase_ref.child(str(reservation[0])).set({
                'reservationID': reservation[0],
                'reservedBy': reservation[1],
                'roomType': reservation[2],
                'reservationDate': str(reservation[3]),  # Convert date to string format
                'checkoutDate': str(reservation[4])     # Convert date to string format
            })

    except psycopg2.Error as error:
        print("Error syncing data:", error)

# Call synchronization function
sync_data()
