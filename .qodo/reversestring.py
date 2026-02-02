string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)


reverse = "" 
for chr in string:
    reverse = chr + reverse
    print("Reversed string:", reverse)
    