while True:
    try:
        date = input("Date: ")
        month, day, year = date.split("/" or "," or " ")
        break
    except ValueError:
        pass

print(month)
print(day)
print(year)


# might need to do multipule if statements under try before spliting (if "/" in date, then split on "/")