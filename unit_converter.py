def length_converter():
    print("\n-- Length Converter --")
    print("Available units: meters, kilometers, inches, feet")
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()
    value = float(input("Enter value: "))

    # Conversion rates to meters
    to_meters = {
        "meters": 1,
        "kilometers": 1000,
        "inches": 0.0254,
        "feet": 0.3048
    }

    if from_unit in to_meters and to_unit in to_meters:
        value_in_meters = value * to_meters[from_unit]
        converted = value_in_meters / to_meters[to_unit]
        print(f"{value} {from_unit} = {converted:.4f} {to_unit}")
    else:
        print("Invalid units.")

def weight_converter():
    print("\n-- Weight Converter --")
    print("Available units: grams, kilograms, pounds, ounces")
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()
    value = float(input("Enter value: "))

    to_grams = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    }

    if from_unit in to_grams and to_unit in to_grams:
        value_in_grams = value * to_grams[from_unit]
        converted = value_in_grams / to_grams[to_unit]
        print(f"{value} {from_unit} = {converted:.4f} {to_unit}")
    else:
        print("Invalid units.")

def temperature_converter():
    print("\n-- Temperature Converter --")
    print("Available units: celsius, fahrenheit, kelvin")
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()
    value = float(input("Enter value: "))

    def to_celsius(val, unit):
        if unit == "celsius":
            return val
        elif unit == "fahrenheit":
            return (val - 32) * 5/9
        elif unit == "kelvin":
            return val - 273.15

    def from_celsius(celsius_val, target_unit):
        if target_unit == "celsius":
            return celsius_val
        elif target_unit == "fahrenheit":
            return (celsius_val * 9/5) + 32
        elif target_unit == "kelvin":
            return celsius_val + 273.15

    if from_unit in ["celsius", "fahrenheit", "kelvin"] and to_unit in ["celsius", "fahrenheit", "kelvin"]:
        celsius = to_celsius(value, from_unit)
        converted = from_celsius(celsius, to_unit)
        print(f"{value} {from_unit} = {converted:.2f} {to_unit}")
    else:
        print("Invalid units.")

def speed_converter():
    print("\n-- Speed Converter --")
    print("Available units: m/s, km/h, mph")
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()
    value = float(input("Enter value: "))

    to_mps = {
        "m/s": 1,
        "km/h": 1000/3600,
        "mph": 1609.34/3600
    }

    if from_unit in to_mps and to_unit in to_mps:
        value_in_mps = value * to_mps[from_unit]
        converted = value_in_mps / to_mps[to_unit]
        print(f"{value} {from_unit} = {converted:.4f} {to_unit}")
    else:
        print("Invalid units.")

def main():
    while True:
        print("\n=== UNIT CONVERTER ===")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Speed")
        print("5. Exit")

        choice = input("Choose category (1-5): ")

        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            speed_converter()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
