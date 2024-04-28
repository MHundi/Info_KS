import math as ma

def calculate_pi(n: int)-> float:
    sum = 0
    for i in range(n):
        sum = sum + 1/(i**2)
    return ma.sqrt(sum*6)
    
def main():
    a = input("Insert the accuracy: ")
    a = int(a)
    result = calculate_pi(a)
    print(result)
       
if __name__ == '__main__':
    main()