# tip_calculator.py - Calculate tips easily
# Author: jhosmar
# Date: 2026-04-14

print ("===tip calculator===")

bill = float(input("Total bill amout: $"))
# clasic menu
print ("\nTip percentage:")
print ("1, 10%")
print ("2, 15%")
print ("3, 20%")
print ("4, custom")

# Author: jhosmar

choise = input("Choose an option 1-4: ")

if choise == "1":
    tip_percent = 10
elif choise == "2":
    tip_percent = 15
elif choise == "3":
    tip_percent = 20
elif choise == "4":
    tip_percent = float(input("Enter custom percentage: "))
else:
    print ("Invalid option. using 15%")
    tip_percent = 15

# Author: jhosmar

tip = bill * (tip_percent / 100)
total = bill + tip

print(f"\nBill: ${bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip:.2f}")
print(f"Total: ${total:.2f}")

# Author: jhosmar
