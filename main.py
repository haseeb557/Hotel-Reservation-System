from flask import Flask, render_template, request, redirect
import psycopg2
from configparser import ConfigParser

app = Flask(_name_)

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def User1(email, name, password):
    try:
        connection = psycopg2.connect(**config('database.ini'))
        cursor = connection.cursor()
        cursor.execute("INSERT INTO User1 (email, name, password) VALUES (%s, %s, %s)",
                       (email, name, password))
        connection.commit()
        cursor.close()
        connection.close()
        
        return True, "User added successfully."
    except (psycopg2.Error, ValueError) as error:
        return False, f"Error while adding user: {error}"
    

def add_reservation(reservationID, reservedBy, roomType, reservationDate, checkoutDate):
    try:
        connection = psycopg2.connect(**config('database.ini'))
        cursor = connection.cursor()
        cursor.execute("INSERT INTO reservation (reservationID, reservedBy, roomType, reservationDate, checkoutDate) VALUES (%s, %s, %s, %s, %s)",
                       (reservationID, reservedBy, roomType, reservationDate, checkoutDate))
        connection.commit()
        cursor.close()
        connection.close()
        
        return True, "Reservation added successfully."
    except (psycopg2.Error, ValueError) as error:
        return False, f"Error while adding reservation: {error}"

def get_reservation_details(reservation_id):
    try:
        connection = psycopg2.connect(**config('database.ini'))
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reservation WHERE reservationID = %s", (reservation_id,))
        reservation_details = cursor.fetchone()
        cursor.close()
        connection.close()
        
        return reservation_details
    except (psycopg2.Error, ValueError) as error:
        return None
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    
    success, message = User1(email, name, password)
    if success:
        return redirect('/', code=302)
    else:
        return message
    

@app.route('/add_reservation', methods=['POST'])
def add_reservation_route():
    reservationID = request.form['reservationID']
    reservedBy = request.form['reservedBy']
    roomType = request.form['roomType']
    reservationDate = request.form['reservationDate']
    checkoutDate = request.form['checkoutDate']
    
    success, message = add_reservation(reservationID, reservedBy, roomType, reservationDate, checkoutDate)
    if success:
        return redirect('/', code=302)
    else:
        return message

@app.route('/reservation_details', methods=['POST'])
def reservation_details():
    reservation_id = request.form['reservation_id']
    reservation_details = get_reservation_details(reservation_id)
    if reservation_details:
        return render_template('reservation_details.html', reservation=reservation_details)
    else:
        return "Reservation not found."

if _name_ == '_main_':
    app.run(debug=True)
