def divide_two_numbers(num1,num2):
  try :
    result = num1 / num2
    return result
  
  except ZeroDivisionError:
      return "error : division by zero is not allowed"


number1 = int(input("enter first number :"))
number2 = int(input("enter first number :"))

result = divide_two_numbers(number1,number2)
print(result)