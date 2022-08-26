grocery = {

}

while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print()
        break

sorted = sorted(grocery)

for item in sorted:
    print(f"{sorted[item]} {item}")
