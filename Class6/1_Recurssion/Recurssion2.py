

class A:    
    """This is class A docstring"""
    pass

obj = A()
print(A)

# Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))


fibonacci_sequence = [fibonacci(i) for i in range(10)]
print(fibonacci_sequence.__doc__)





# Example of recursion with string reversal
def reverse_string(s):      
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])   
    
result = reverse_string("ricky")
print(result)  # Output: "olleh"