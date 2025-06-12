import sqlite3
import getpass

def sqlcon():
    try: #connection to database
        connect = sqlite3.connect("forPy.db")
        print("successfully connected to database!")
        cursor = connect.cursor()

        # user login
        for attempts in range(1, 4):
    
            txtUser = input("\nusername: ").lower()
            txtPass = getpass.getpass("password: ").lower()
            
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (txtUser, txtPass))

            if cursor.fetchone():
                print("login successfully!")
                return True
            else:
                print(f"failed to login", end = " ")
        if attempts == 3:
            print(f"{attempts} times!")
            exit()
        #validation
    except sqlite3.Error as error:
        print("failed to connect in database")
    except Exception as e:
        print(f"{e} error detected!")
    finally:
        if connect:
            connect.close()
sqlcon() #used function

