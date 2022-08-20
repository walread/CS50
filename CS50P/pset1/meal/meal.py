def main():
    answer = input("What time is it? ")

    time = convert(answer)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    time = float(hour) + float(minute)/60
    return time


if __name__ == "__main__":
    main()