def distance_converter():
    print("\n--- Distance Converter ---")
    print("1. Kilometers → Miles")
    print("2. Miles → Kilometers")
    print("3. Meters → Feet")
    print("4. Feet → Meters")
    choice = input("Choose conversion: ")
    value = float(input("Enter value: "))
    if choice=="1":
        print(f"{value} km = {value * 0.621371:.4f} miles")
    elif choice=="2":
        print(f"{value} miles = {value * 1.60934:.4f} km")
    elif choice=="3":
        print(f"{value} meters = {value * 3.28084:.4f} feet")
    elif choice=="4":
        print(f"{value} feet = {value / 3.28084:.4f} meters")
    else:
        print("Invalid choice!")


def mass_converter():
    print("\n--- Mass Converter ---")
    print("1. Kilograms → Pounds")
    print("2. Pounds → Kilograms")
    print("3. Grams → Kilograms")
    print("4. Kilograms → Grams")

    choice = input("Choose conversion: ")

    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value} kg = {value * 2.20462:.4f} lb")
    elif choice == "2":
        print(f"{value} lb = {value / 2.20462:.4f} kg")
    elif choice == "3":
        print(f"{value} g = {value / 1000:.4f} kg")
    elif choice == "4":
        print(f"{value} kg = {value * 1000:.4f} g")
    else:
        print("Invalid choice!")

def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")

    choice = input("Choose conversion: ")
    value = float(input("Enter temperature: "))

    if choice == "1":
        print(f"{value}°C = {(value * 9/5) + 32:.2f}°F")
    elif choice == "2":
        print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
    elif choice == "3":
        print(f"{value}°C = {value + 273.15:.2f} K")
    elif choice == "4":
        print(f"{value} K = {value - 273.15:.2f}°C")
    else:
        print("Invalid choice!")
def volume_converter():
    print("\n--- Volume Converter ---")
    print("1. Liters → Milliliters")
    print("2. Milliliters → Liters")
    print("3. Liters → Gallons")
    print("4. Gallons → Liters")

    choice = input("Choose conversion: ")

    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value} L = {value * 1000:.2f} mL")
    elif choice == "2":
        print(f"{value} mL = {value / 1000:.4f} L")
    elif choice == "3":
        print(f"{value} L = {value * 0.264172:.4f} gallons")
    elif choice == "4":
        print(f"{value} gallons = {value * 3.78541:.4f} L")
    else:
        print("Invalid choice!")
def speed_converter():
    print("\n--- Speed Converter ---")
    print("1. km/h → mph")
    print("2. mph → km/h")
    print("3. m/s → km/h")
    print("4. km/h → m/s")

    choice = input("Choose conversion: ")
    value = float(input("Enter speed: "))

    if choice == "1":
        print(f"{value} km/h = {value * 0.621371:.4f} mph")
    elif choice == "2":
        print(f"{value} mph = {value * 1.60934:.4f} km/h")
    elif choice == "3":
        print(f"{value} m/s = {value * 3.6:.4f} km/h")
    elif choice == "4":
        print(f"{value} km/h = {value / 3.6:.4f} m/s")
    else:
        print("Invalid choice!")
def main():
    while True:
        print("\n" + "=" * 45)
        print("        UNIT CONVERTER")
        print("=" * 45)
        print("1. Distance Converter")
        print("2. Mass Converter")
        print("3. Temperature Converter")
        print("4. Volume Converter")
        print("5. Speed Converter")
        print("6. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            distance_converter()
        elif choice == "2":
            mass_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            volume_converter()
        elif choice == "5":
            speed_converter()
        elif choice == "6":
            print("\nThank you for using the Unit Converter!")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()