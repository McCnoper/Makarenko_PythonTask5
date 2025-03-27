print("Task 1")
t = int(input("Enter temperature in °C"))
h = int(input("Enter humidity in percents"))
if t > 30 and h > 70:
    print("Activation of the cooling system")
else: print("Conditions are normal")
#-------------------------------------------------------
print("Task 2")
x = int(input("Enter number"))
if x>=1 and x<=100:
    print("Number is in between 1-100")
else: print("Number isn`t in between 1-100")
#-------------------------------------------------------
print("Task 3")
age = int(input("Enter your age"))
exp = int(input("Enter your years of experience"))
qual = input("Do you have any special qualifications? t/f")
if qual == "t":
    qual = True
else:
    qual = False
if 25 <= age <= 50 and (exp >= 3 or qual):
    print("The candidate meets the requirements")
else:
    print("The candidate doesn`t meet the requirements")
