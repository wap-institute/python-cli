import random
class GenerateSecret : 
    def __init__(self) : 
        secret = ''
        pattern = 'W&&FIW&&FI#2J09-2#73**R9E#7d@sf(ksd$kfm2^37NMNJSJNDFUWUIDQBI'
        choice = int(input("Enter length for your secret\n"))
        for data in range(choice) : 
            limit = len(pattern)-1
            index = random.randint(0,limit)
            secret = secret+pattern[index]
        print(secret,'\n')