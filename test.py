import time
import os

i = os.getenv("test")

i = int(i)

i = i +1 

print(i)

with open(".env", "w") as file:
  file.write(f'test="{i}"\n')


