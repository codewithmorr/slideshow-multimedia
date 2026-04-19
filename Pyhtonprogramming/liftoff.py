import time

for i in range(10,0, -1):
    print(f"{i}..")
    time.sleep(1)  # delays for 1 second between each loop iteration
print("Liftoff!")  # This will count down from 10 to 1 and then print "Liftoff!"