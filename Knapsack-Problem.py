#knapsack problem(greedy method)

weight = int(input("Enter the bag size:"))

w_values=input("Enter the weight of item:")
w_values = w_values.split()
w_values=[int(x) for x in w_values] #coverting into integer
print(w_values)

profit = input("enter the 50 value of item:")
profit = profit.split()

profit=[int(y) for y in profit]
#sorting it
arrr =[(w_values[i],profit[i])for i in range(0,len(profit))] #MAKING TUPLE
s_a=sorted(arrr,key=lambda x:x[1],reverse=True) #sorting on basis of profit in reverse order
print(s_a)

def knapsack(sack_size, s_a):  
    total_profit = 0 
    for item in s_a:
        if item[0]<=sack_size: #item should be less or equal to fix sack size
            total_profit=total_profit+item[1] #add profit
            sack_size=sack_size-item[0] #update by subracting size
    return total_profit
ans=knapsack(weight,s_a)
print(ans)            
   
