# try:
#     [1, 2, 3][10]
# except IndexError:
#     print("IndexError occurred")


try:
    int("xyxyx")
except ValueError:
    print("ValueError occurred")
else:
    print("Conversion successful")
