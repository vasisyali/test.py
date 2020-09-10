# калькулятор v0.1

print("( + = плюс),( - = минус),( ** = возведение в степень),\n( * = умножить),( / = разделить),( % = деление по модулю)\n")
g=str(input(" + , - , ** , * , / , %  : что выбираем? \n:"))

a=float(input("первое число:"))
b=float(input("второе число:"))

if g == "+":
    c = a + b
    print("Ответ: " + str(c))

elif g == "-":
    c = a - b
    print("Ответ: " + str(c))

elif g == "**":
    c = a ** b
    print("Ответ: " + str(c))

elif g == "%":
    c = a % b
    print("Ответ: " + str(c))

elif g == "*":
    c = a * b
    print("Ответ: " + str(c))

elif g == "/":
    c = a / b
    print("Ответ: " + str(c))

else:
    print("не верная операция!")
print()
