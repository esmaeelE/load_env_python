import os
from dotenv import load_dotenv

load_dotenv()


my_db_user = os.environ.get('DB_USER')
my_db_password = os.environ.get('DB_PASS')

print("Username: ", my_db_user, "Type: ", type(my_db_user))
print("Password: ", my_db_password, "Type:", type(my_db_password))


