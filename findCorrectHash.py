import hashlib

HASH = "5e2a0c62c40b2cb4879b0081ec6db149"
FILE_NAME = "WiFiQRCode"
EXTENSION = ".jpg"


for i in range(1, 6+1):
    hasher = hashlib.md5()

    with open(FILE_NAME + str(i) + EXTENSION, "rb") as imgfile:
        buf = imgfile.read()
        hasher.update(buf)
    
    if hasher.hexdigest() == HASH:
        print(FILE_NAME + str(i) + EXTENSION)
        break
