def pali(string:str) ->bool:
    reverse_word=string[::-1]
    if reverse_word==string:
        return string

word=input("enter your word")
if pali(word):

    print("paliendrome")
else:
    print("not a paliendrome")
