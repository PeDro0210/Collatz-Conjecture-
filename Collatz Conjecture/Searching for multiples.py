def multiples_checkear(num, thenum, numerito):
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
            return multiples_checkear(thenum, thenum, numerito)
        #here is pretty explanatory, if the number is bigger that 10**1000, it means that is adding till infinity.
        
        if num in previous_nums:
            count += 1
            if count >= 20:
                thenum += 1
                numerito = 3 * thenum
                print(f"{thenum}*3, which is = {numerito}, is valid not for the conjuture")
                return multiples_checkear(thenum, thenum, numerito)
            
            #in here we check if there's a loop in other part, if that's the case, we do 20 iterations and if it's still in a loop we show that the multiple
            #is not part of the conjuture
            
        else:
            previous_nums.append(num)
            
    if num == 1:
        print(f"{thenum}*3, which is = {numerito}, is valid for the conjuture")
        thenum = 1 + thenum
        numerito = 3 * thenum
        multiples_checkear(thenum, thenum, numerito)


user_num = int(input("Enter a number: "))
thenum = 1
numerito = 3 * thenum
multiples_checkear(user_num, thenum, numerito)
