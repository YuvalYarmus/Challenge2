from zipfile import ZipFile

passwords = []

with open("pass.txt") as passwords_file:
    passwords = [pwd.strip() for pwd in passwords_file.readlines()]

with ZipFile("wifi.zip") as zip_file:
    for pwd in passwords:
        try:
            zip_file.extractall(pwd=bytes(pwd, "utf-8"))
            print(f"{pwd} did work")
            break
        except:
            print(f"{pwd} didn't work")
