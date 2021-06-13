name = input("Enter Your name: ")
print(f"Welcome " + name)

# Collect Age Data
print(" You Can Write First Litter Or Full Name Of The Time Unit ".center(80, '#'))

age = input("What's your age? ").strip()

# Collect Time Unit Data
unit = input("Choose Time Unit: Months 'm', Weeks 'w', Days 'd': ").strip().lower()

# Get Time Units
months = int(age) * 12
Weeks = months * 4 
days = int(age) * 365

if unit == 'months' or unit == 'm':

    print("You choosed The Unit Month")
    print(f"{name} lived For {months:,} Months.")

elif unit == 'weeks' or unit == 'w':

    print("You choosed The Unit Weeks")
    print(f"{name} lived For {Weeks:,} Weeks.")

elif unit == 'days' or unit == 'd':

    print("You choosed The Unit Days")
    print(f"{name} lived For {days:,} Days.")

else:
    print("Invalid Unit Time !")
