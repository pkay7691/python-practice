# str.format() = optional method that gives users more control when displaying output


animal = 'cow'
item = 'moon'

print("The " + animal + " jumped over the moon")
print("The {} jumped over the {}".format(animal, item))
# postional argument
print("The {0} jumped over the {1}".format(animal, item)) 

print("The {animal} jumped over the {item}".format(animal='cow', item='moon')) 

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Bro"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}.  Nice to meet you".format(name))
print("Hello my name is {:<10}.  Nice to meet you".format(name))
print("Hello my name is {:>10}.  Nice to meet you".format(name))
print("Hello my name is {:^10}.  Nice to meet you".format(name))


number = 1000

print("The number pi is {:.2f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:E}".format(number))


