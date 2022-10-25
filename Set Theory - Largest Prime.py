import math

def main():
    count = 1
    
    while True:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime=true:
            print(count)
        
        count += 2
       
main()