def temperature_alert(temp_celsius):
    if temp_celsius < 15:
        return "Cold (below 15°C)"
    elif 15 <= temp_celsius <= 30:
        return "Normal (15°C to 30°C)"
    else:
        return "Hot (above 30°C)"

# Example usage:
# temp = float(input("Enter temperature in Celsius: "))
# print(temperature_alert(temp))
