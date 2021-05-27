import random


def prime_generate():
    print("PRIME NUMBER FINDER")
    num_start = int(input("Input Start Number : "))
    num_end = int(input("Input End Number   : "))
    list_num = [i for i in range(num_start, num_end + 1)]
    prime_num = []
    for i in list_num:
        if (i == 2 or i == 3 or i == 5 or i == 7) or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
            prime_num.append(i)
    print(prime_num)

    #Random bilangan
    conf = input("Choice Random Prime Number [y/n]? ")
    if conf.lower() in ['y', 'yes']:
        print("\nTHE RANDOM PRIME NUMBER\n")
        rand_num1 = random.choice(prime_num)  
        print("Random Number 1 :", rand_num1)
        rand_num2 = random.choice(prime_num)  
        print("Random Number 2 :", rand_num2)
    elif conf.lower() in ['n', 'no']:
        print('End!')


def main():
    prime_generate()


main()
