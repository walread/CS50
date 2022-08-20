file = input("File name: ").lower().strip()

if ".jpg" in file or ".jpeg" in file:
    print("image/jpeg")
else:
    print("applicaton/octet-stream")