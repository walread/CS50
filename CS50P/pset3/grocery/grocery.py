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

for item in grocery:
    print(f"{grocery[item]} {item}")
