import csv

nombre= input("como quieres que se llame el documento: ")

def collatz_variant(num, power):
    intermediate_nums = []
    while num != 1:
        if num in intermediate_nums:
            break
        intermediate_nums.append(num)
        if num % 2 == 0:
            num2 = num // 2
            with open(f"{nombre}.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([num, num2])
            num = num2
        else:
            num1 = (num * 3 * power) + power
            with open(f"{nombre}.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([num, num1])
            num = num1

while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Enter a valid integer.")
        
for i in range(1, 100):
    power = 2**i
    result = collatz_variant(num, power)
    

print(f"Los resultados se han escrito en el archivo {nombre}.csv")