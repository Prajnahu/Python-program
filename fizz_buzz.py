def fizz_buzz(n: int) -> str:
    """ the number 'n' should be an integer value
    should return fizz,buzz,fizzbuzz according tothe input
    """
    if n%3==0 and n%5==0:
        return "fizz buzz"
    elif n%3==0:
        return "fizz"
    elif n%5==0:
        return "buzz"
    else:
        return str(n)

for i in range(1, 101):
    print(fizz_buzz(i))