try: 
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print('you cant divide by zero idiot')
except ValueError as e:
    print(e)
    print("Enter only number plz")
except Exception as e:
    print(e)
    print("Something went wrong")
else: 
    print(result)
finally: 
    print('This will always execute')

