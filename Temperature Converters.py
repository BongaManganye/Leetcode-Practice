#Write a program that  prompts the user for a temperature in Celsius, converts it to Fahrenheit using the formula F = ( C * 9/5) + 32, and prints the results rounded to decimal places

Temperature = int(input("Please enter the temperature in Celsius"))

F = (Temperature * 9/5) + 32

print(f"Fahrenheit {F}")
