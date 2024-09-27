print("What would you like to calculate?")
print("1. Voltage (V)")
print("2. Current (I)")
print("3. Resistance (R)")
choice = input("Enter 1, 2, or 3: ")


if choice == '1':  
    current = float(input("Enter the current (I) in amperes: "))
    resistance = float(input("Enter the resistance (R) in ohms: "))
    voltage = current * resistance
    print(f"The voltage (V) is: {voltage} volts")
    
elif choice == '2':  
    voltage = float(input("Enter the voltage (V) in volts: "))
    resistance = float(input("Enter the resistance (R) in ohms: "))
    if resistance == 0: 
        print("Error: Resistance cannot be zero.")
    else:
        current = voltage / resistance
        print(f"The current (I) is: {current} amperes")
    
elif choice == '3':  
    voltage = float(input("Enter the voltage (V) in volts: "))
    current = float(input("Enter the current (I) in amperes: "))
    if current == 0:  
        print("Error: Current cannot be zero.")
    else:
        resistance = voltage / current
        print(f"The resistance (R) is: {resistance} ohms")
    
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
