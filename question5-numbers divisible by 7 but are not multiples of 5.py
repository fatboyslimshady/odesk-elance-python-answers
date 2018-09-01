"""5. (5min)
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma separated sequence on a single line."""
# type(x)==int:


for x in range(2000, 3200):
    if (x % 7) == 0:
        if (x % 5) != 0:
            print(str(x) + ",", end=' ')  # coz u cant concat an int+a string, so convert int to str then concat
