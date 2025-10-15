# a-z
# 0-9
# . _ time 1
# @ time 1
# . 2,3

import re                           #rejeks
m1 ="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"                         #? it means 0 or 1 time exist
m2 =input("Enter You Email : ")              #\w means dhundna


if re.search(m1,m2):
    print("Ringht Email")
else:
    print("wrong email")
