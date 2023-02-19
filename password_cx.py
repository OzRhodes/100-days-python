import getpass
# normally these details are hashed and stored in a dbm or alternatve file
database = {"Tom": "123456", "Dick": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
	if username == i:
		while password != database.get(i):
			password = getpass.getpass("Enter Your Password Again : ")
			break
print("Verified")
