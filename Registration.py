import mysql.connector
from getpass import getpass
# Set up database connection
config = {
     'user': 'root',
     'password': '$Sh@dow040221',
     'host': 'localhost',
     'database': 'reg'
}

def register_user():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Get user input
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        email = input("Enter your email: ")
        Pass = input("Enter your password: ")

        # Insert user into database
        query = "INSERT INTO details (firstname, lastname, email, Pass) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (firstname, lastname, email, Pass))

        # Commit changes and close connection
        cnx.commit()
        cursor.close()
        cnx.close()

        print("User registered successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    register_user()