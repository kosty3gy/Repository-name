numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_1 = 0

for i in numbers:
    if type(i) == int:
        sum_1 += i

for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = sum_1/len(numbers)

print("Измененный список:", numbers)
