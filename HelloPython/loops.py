while True:
    user_input = input("Enter something (or 'exit' to quit): ")
    if user_input == "exit":
        break
    print("You entered:", user_input)

for i in range(5):
    print("Iteration:", i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
