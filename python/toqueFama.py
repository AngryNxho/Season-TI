from random import randint

number_length = int(input("Set the length of your code: "))
secret_number = []


def random_number():
    return randint(1, 9)

def check_number():
    for x in range(number_length):
        if random_number() not in secret_number:
            secret_number.append(random_number())
    return secret_number

        
print(check_number())



