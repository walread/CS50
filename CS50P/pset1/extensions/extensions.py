file = input("File name: ").lower().strip()

if ".gif" in file:
    print("image/gif")
elif ".jpg" in file or ".jpeg" in file:
    print("image/jpeg")
elif ".png" in file:
    print("image/png")
elif ".pdf" in file:
    print("application/pdf")
elif ".txt" in file:
    print("application/txt")
elif ".zip" in file:
    print("application/zip")
else:
    print("applicaton/octet-stream")