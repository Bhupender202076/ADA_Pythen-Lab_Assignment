#fermate primality test
#function for finding power
def expo(a,n):
    if n == 0:
        return 1
        # for finding power of even no
    if n%2 == 0:
        res = expo(a, n // 2) #dividing value in half = res 
        res = res*res
        #odd no
    else:
        res = expo(a, n//2)
        res = a*res*res
    return res

# for primality test of n
def primality(n):
    m = n-1     # formula = a^n-1 % n = 1
    for a in range(2,n):
        r = expo(a,m)
        if r%n == 1: #find reminder
          print(f'{n} is prime')
          break
        else:
            print(f'{n} is composite')
            break  

num = int(input("The no. to be checked : "))
if num == 1 or num ==2:
    print("It is prime")
else:    
    primality(num)  # calling fun


