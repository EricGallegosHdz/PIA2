import hashlib

def Hash(file):
    #file = input("Digitar el nombre del archivo: ")
    with open(file, "rb") as f:
        byte = f.read()
        hash_text = hashlib.sha256(byte).hexdigest()
        print(hash_text)
