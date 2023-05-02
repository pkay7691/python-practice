from car import Car

corvette = Car("Chevy", "Corvette", 2021, "blue")
mustang = Car("Ford", "Mustang", 1999, "red")


print(corvette.make)
print(corvette.model)
print(corvette.year)
print(corvette.color)

# Car.wheels = 2

corvette.drive()
corvette.stop()
mustang.drive()
print(mustang.wheels)
