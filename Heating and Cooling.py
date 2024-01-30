def heatingand_cooling(actual_temp, desired_temp):
    if actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")
    else:
        print("Standby")
print()

heatingand_cooling(70, 72)  # print "Run heat"
heatingand_cooling(75, 70)  # print "Run A/C"
heatingand_cooling(68, 68)  # print "Standby"

users_actual_temp = float(input("Enter the actual temperature: "))
users_desired_temp = float(input("Enter the desired temperature: "))

heatingand_cooling(users_actual_temp, users_desired_temp)

def convert_temp(temp_celsius, target_unit):
    # Switch statement to handle different target units
    if target_unit == "C":
        # Celsius requires no conversion
        converted_temp = temp_celsius
    elif target_unit == "F":
        # Fahrenheit conversion: (Celsius * 9/5) + 32
        converted_temp = (temp_celsius * 9/5) + 32
    elif target_unit == "K":
        # Kelvin conversion: Celsius + 273.15
        converted_temp = temp_celsius + 273.15
    else:
        # Handle invalid target_unit
        return "Invalid target unit. Please use 'C', 'F', or 'K'."

    return converted_temp

# Example usage:
celsius_temperature = 25
converted_to_fahrenheit = convert_temp(celsius_temperature, "F")
converted_to_kelvin = convert_temp(celsius_temperature, "K")

print(f"{celsius_temperature}°C is equal to {converted_to_fahrenheit}°F")
print(f"{celsius_temperature}°C is equal to {converted_to_kelvin}K")
