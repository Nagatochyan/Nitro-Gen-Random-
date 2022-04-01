
import os
from time import sleep
import requests
import random
import string
from colorama import Fore
num = int(input("何回送りますか？"))
for i in range(num):
    a="https://discord.gift/"
    code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
    print(a +code)
