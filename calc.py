def add(first_term, second_term):
    return first_term + second_term

def subtract(first_term, second_term):
    return first_term - second_term

def multiply(first_term, second_term):
    return first_term * second_term

def divide(first_term, second_term):
    if second_term == 0:
        raise Exception("Sorry, denominator can't be zero")
    return first_term / second_term

def mod(first_term, second_term):
    if second_term == 0:
        raise Exception("Sorry, denominator can't be zero")
    return first_term % second_term

def quotient(first_term, second_term):
    if second_term == 0:
        raise Exception("Sorry, denominator can't be zero")
    return first_term // second_term