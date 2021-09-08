from calculator_art import logo
import os

def clear():
  if os.name == "nt":
    _ = os.system('cls')

#Functions
def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

#Dictionaries
operators = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
} 

def calculator():
  print(logo)
  num1 = float(input("What's the first number?\n"))
  for key in operators:
    print(key)
  should_continue = True
  while should_continue:
    operators_symbol = input("Choose an operator.\n")
    num2 = float(input("What's the next number?\n"))
    calculation_functions = operators[operators_symbol]
    answer = calculation_functions(num1,num2)
    print(f"{num1} {operators_symbol} {num2} = {answer}")

    res = input(f"Type 'y' to continue with {answer} while type 'n' to start new calculator.")
    if res == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()
        
calculator()
        


