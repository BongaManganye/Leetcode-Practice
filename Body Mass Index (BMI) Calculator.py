#Body Mass Index (BMI) Calculator

#Calculate BMI given weight in kilograms and height in meters. Formula: BMI = weight / ( height ** 2 )
#  Categorize the result into Underweight, Normal, Overweight, or Obese

def calc_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5 : cat = "Underweight"
    elif bmi < 25: cat = "Normal"
    elif bmi < 30: cat = "Overweight"
    else: cat = "Obese"
    return bmi, cat
