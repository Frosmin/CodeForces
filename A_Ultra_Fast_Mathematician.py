num1 = input()
num2 = input()
nuevo = []


for i in range(len(num1)):
    if num1[i] == num2[i] and num1[i] == '1':
        nuevo.append('0')
    elif num1[i] == '1' or num2[i] == '1':
        nuevo.append('1')
    else:
        nuevo.append('0')
print("".join(nuevo))