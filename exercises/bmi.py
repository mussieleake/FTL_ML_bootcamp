#BMI Calculator

def calculate_bmi(weight, height):
  bmi = weight/height**2
  return round(bmi, 2)
weight = float(input('Enter your weight:'))
height = float(input('Enter your height:'))
result = calculate_bmi(weight, height)
print(result)

if result < 18.5:
  print('Underweight')
elif result >= 18.5 and result <= 24.9:
  print('Normal weight')
elif result >= 25 and result <= 29.9:
  print("overweight")
elif result >= 30:
  print("obese")