number = int(input("lot adad mosbat vared koned: "))


if number <= 0:
    print("lotfan adad mosbat vared koned .")
else:
    while number > 0:
        digit = number % 10
        print(digit)
        number //= 10
