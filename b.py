from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import shutil
import zipfile
from zipfile import ZipFile

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

try: os.mkdir("images")
except FileExistsError: pass
with ZipFile("wifi.zip") as zip_file:
    zip_file.extractall(path="images", pwd=bytes("1234qwer", "utf-8")) 

for filename in os.listdir("/images"):
    if filename.endswith(".asm") or filename.endswith(".py") or filename.endswith(".jpg"): 
        print(os.path.join("/images", filename))
        continue
    else:
        continue