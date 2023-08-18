number = int(input("Enter a positive number: "))


if number <= 0:
    print("Please enter a positive number.")
else:
    while number > 0:
        digit = number % 10
        print(digit)
        number //= 10
