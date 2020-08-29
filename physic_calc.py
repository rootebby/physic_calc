# Cross Product
from math import sqrt
import time
def Logo():
    print("""
                 _    ____       _     _
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                  |___/     

    """)
    time.sleep(1)   
    print("Hypotenuse - Cross Product Calculator")
    time.sleep(0.5)
    print("Coded by root@ebby:~#")
def Cross(x,y):
    answer_is = x ** 2 + y ** 2
    print("""
    X :             {}
    Y :             {}
    Cross_Product : {}
    """.format(x,y,sqrt(answer_is)))

# __main__
Logo()
while True:
    x = int(
        input("X : ")
    )
    
    y = int(
        input("Y : ")
    )

    print("Calculating ...")
    time.sleep(1)
   
    Cross(x,y)

