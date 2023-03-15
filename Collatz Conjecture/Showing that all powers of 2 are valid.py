def comprobation(num, power):
    intermediate_nums = []
    while num != 1:
        if num in intermediate_nums:
            break
        intermediate_nums.append(num)
        if num % 2 == 0:
            num = num // 2
            
        else:
            num = (num * 3 * power) + power
    return f"La secuencia termina en 1 con potencia {power}."

while True:
    try:
        num = int(input("Ingrese un número entero: "))
        break
    except ValueError:
        print("Ingrese un número entero válido.")

for i in range(1, 100):
    power = 2**i
    result = comprobation(num, power)
    print(result)
