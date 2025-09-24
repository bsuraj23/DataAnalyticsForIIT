try:
    result = 5 / 0
except:
    print("Error")
else:
    print("Result is", result)
finally:
    print("Execution completed")    