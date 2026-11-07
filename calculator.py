import numpy as np

print("Welcome to the Python Calculator!")

print("Note: Use 'np' for numpy functions, e.g, 'np.sqrt(16)' or 'np.sin(np.pi/2)'.")

calculation = input("Enter the calculation you want to perform (e.g, '2 + 2', 'sqrt(16)', 'sin(pi/2)': ")

result = eval(calculation)
print(f"The result of {calculation} is {result}")
print("Do you want to perform another calculation (yes/no)")

if input().lower() == 'yes':
  calculation = input("Enter the calculation you want to perform: ")
  result = eval(calculation)
  print(f"The result of {calculation} is {result}")
