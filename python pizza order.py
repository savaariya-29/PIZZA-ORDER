#python pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill=0
# first want to create a bill variable after add price for the pizza according to size(using multiple if/elif/else statement)
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25
else:
    print("you have typed wrong info")
#using nested statement
if pepperoni =="Y":
    if size== "S":
        bill+=2
    else:
        bill+=3
# multiple if stament
if extra_cheese =="Y":
    bill+=1

print(f"Your final bill is: ${bill}.")