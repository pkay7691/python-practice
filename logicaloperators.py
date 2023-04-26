temp = int(input("what's the temp outside:"))

if not (temp >= 0 and temp <= 30): 
     print("the temp is bad today")
     print("stay inside")
elif not (temp < 0 or temp > 30): 
     print("the temp is good today")
     print("go outside")
  
