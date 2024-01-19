#test prime number
def check_prime(number):
    count = 0 
    prime = False
    for i in range(1, number+1):
        if(number % i == 0):
            count += 1

    if(count == 2):
        prime = True
    
    return prime

number = int(input("Enter a number to be checked: "))    
value_of_check_prime = check_prime(number)
print(value_of_check_prime)

if value_of_check_prime:
    print("Prime number")

def multiplicationtable(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number*i}")

multiplicationtable(number)

# #odd_even test
# def check_odd_even(num):
#     if(num % 2 == 0):
#         print("Even number")
#     else:
#         print("Odd number")

# num = int(input("Enter a number: "))
# check_odd_even(num)

