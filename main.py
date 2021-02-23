from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import shutil
import zipfile
from zipfile import ZipFile
import hashlib


url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

# print(text)

print("\n moving to phase 2\n")

passwords = text.split("\n")

# with open("pass.txt") as passwords_file:
#     passwords = [pwd.strip() for pwd in passwords_file.readlines()]

try: os.mkdir("images")
except FileExistsError: pass

with ZipFile("wifi.zip") as zip_file:
    for pwd in passwords:
        try:
            zip_file.extractall(path="images", pwd=bytes(pwd, "utf-8"))
            print(f"{pwd} did work")
            break
        except:
            print(f"{pwd} didn't work")
            pass

print("\n moving to phase 3\n")

HASH = "5e2a0c62c40b2cb4879b0081ec6db149"
FILE_NAME = "WiFiQRCode"
EXTENSION = ".jpg"

for filename in os.listdir("/images"):
    print(os.path.join("/images", filename))
    hasher = hashlib.md5()

    with open(filename, "rb") as imgfile:
        buf = imgfile.read()
        hasher.update(buf)

    if hasher.hexdigest() == HASH:
        print(f"\nthe correct filename is {filename}")
        break



