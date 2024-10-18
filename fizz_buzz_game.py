print("Welcome to FizzBuzz Game")


num = input('write "start" to start the game :')
if num == "start":
    number= int(input("Enter the range of number you want to calculate :"))
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
else:
    print("wrong input try again")