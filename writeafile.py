text = 'have a nice day'
# write
with open('test.txt', 'w') as file:
    file.write(text)
# append
with open('test.txt', 'a') as file:
    file.write(text)
