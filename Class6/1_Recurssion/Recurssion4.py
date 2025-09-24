# Reverse string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]
print(reverse_string("python"))

print("python"[::-1])  #reverse a string using slicing
