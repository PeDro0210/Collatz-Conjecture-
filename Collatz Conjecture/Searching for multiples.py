def collatz(num, thenum, numerito):
    count = 0
    previous_nums = []    
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            print(num)
        else:
            num = num * numerito + thenum
            print(num)
        if num > 10**1000:
            thenum += 1
            numerito = 3 * thenum
            print(f"{thenum}*3, which is = {numerito}, is valid not for the conjuture")
            return collatz(thenum, thenum, numerito)
        if num in previous_nums:
            count += 1
            if count >= 20:
                thenum += 1
                numerito = 3 * thenum
                print(f"{thenum}*3, which is = {numerito}, is valid not for the conjuture")
                return collatz(thenum, thenum, numerito)
        else:
            previous_nums.append(num)
    if num == 1:
        print(f"{thenum}*3, which is = {numerito}, is valid for the conjuture")
        thenum = 1 + thenum
        numerito = 3 * thenum
        collatz(thenum, thenum, numerito)


user_num = int(input("Enter a number: "))
thenum = 1
numerito = 3 * thenum
collatz(user_num, thenum, numerito)
