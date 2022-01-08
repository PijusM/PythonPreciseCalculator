#Created by @PijusM

from decimal import * 
from time import sleep

def main():

  input1 = input("Input the 1st number > ")
  input2 = input("Input the 2nd number (leave blank if there is none) > ")
  input3 = input("Input the function you wanna do > ")


  def addition(a, b):
    getcontext().prec = 1000
    answer = Decimal(a) + Decimal(b)
    return (f'The answer is: {answer}')
  def root(a):
    getcontext().prec = 100
    answer = Decimal(a) ** Decimal(0.5)
    return (f'The answer is: {answer}')
  def multiply(a, b):
    getcontext().prec = 1000
    answer = Decimal(a) * Decimal(b)
    return (f'The answer is: {answer}')
  def divide(a, b):
    getcontext().prec = 1000
    answer = Decimal(a) / Decimal(b)
    return (f'The answer is: {answer}')
  def subtraction(a, b):
    getcontext().prec = 1000
    answer = Decimal(a) - Decimal(b)
    return (f'The answer is: {answer}')
  def square(a):
    getcontext().prec = 1000
    answer = Decimal(a) ** Decimal(2)
    return (f'The answer is: {answer}')
  

  if input2 == "":
   pass
  if input3 == "+":
   add = addition(input1, input2)
   print(add)
  if input3 == "root":
   root = root(input1)
   print(root)
  if input3 == "**":
   square = square(input1)
   print(square)
  if input3 == "-":
   sub = subtraction(input1,input2)
   print(sub)
  if input3 == "*":
   mult = multiply(input1, input2)
   print(mult)
  if input3 == "/":
   div = divide(input1, input2)
   print(div)
  input4 = input("Do you want to try again? > ")
  input4 = input4.lower()
  if input4 == "yes":
    main()
  elif input4 == "no":
    print("The program is closing..")
    sleep(3)
    exit()
main()