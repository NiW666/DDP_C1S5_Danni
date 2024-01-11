
def count_case(a):
    upper_count=0
    lower_count=0

    for i in a:
        if i.islower():
            lower_count+=1
        elif i.isupper():
            upper_count+=1
    
    return f"Uppercase letters: {upper_count}, Lowercase letters: {lower_count}"

a=input()

print(count_case(a))
