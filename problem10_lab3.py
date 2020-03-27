import string
def validity(str1):
    if len(str1)>=6 and len(str1)<= 18:
        if any([i in string.punctuation for i in str1]) and any([i in string.ascii_lowercase for i in str1]) and any([i in string.ascii_uppercase for i in str1]) and any([i in string.digits for i in str1]):
            return True
    return False
print(validity("yaya"))