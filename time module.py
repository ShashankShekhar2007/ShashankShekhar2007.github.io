import time
i = time.time()
v = 0
while v < 1000:
    print("Hello")
    v= v+1
print(f"Time Taken {i-time.time()} ")

i2 = time.time()
for x in range(1000):
    print("Hello")
print(f"Time Taken {i2-time.time()} ")


i3 = time.time()
for z in range(5):
    print("Hello")
    time.sleep(2)
print(f"Time Taken {i3-time.time()} ")


l = time.asctime(time.localtime(time.time()))
print(l)

