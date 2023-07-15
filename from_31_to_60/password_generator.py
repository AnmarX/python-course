import random

lower="qwertyuiopasdfghjhklzxcvbnm"
upper="QWERTYUIOPASDFGHJKLMNBVCXZ"
numer="12334567890"
char="@#$%^&*()[].,!/"
all=lower+upper+numer+char

ran="".join(random.sample(all,16))

print(ran)