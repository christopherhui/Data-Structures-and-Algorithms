from pythonds.basic.stack import Stack

def postFixEvaluator(postfixexpr):
  aList = postfixexpr.split()
  aStack = Stack()
  for val in aList:
    if val == '+':
      num1 = int(aStack.pop())
      num2 = int(aStack.pop())
      aStack.push(num2 + num1)
    elif val == '-':
      num1 = int(aStack.pop())
      num2 = int(aStack.pop())
      aStack.push(num2 - num1)
    elif val == '*':
      num1 = int(aStack.pop())
      num2 = int(aStack.pop())
      aStack.push(num2 * num1)
    elif val == '/':
      num1 = int(aStack.pop())
      num2 = int(aStack.pop())
      aStack.push(int(num2 / num1))
    else:
      aStack.push(val)
  return aStack.pop()

print(postFixEvaluator("7 8 + 3 2 + /"))
print(postFixEvaluator("17 10 + 3 * 9 /"))
