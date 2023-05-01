rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


for i in range(int(6)):
    for j in range(int(5)):
        print("%", end='')
    print()
