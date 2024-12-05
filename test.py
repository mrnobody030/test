import time
import os

file1 = open("file1.txt", "r").read()

file1 = int(file1)

file1 = file1 + 1

print(file1)

file2 =open("file1.txt", "w").write(f"{file1}")


