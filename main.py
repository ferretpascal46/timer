import time

# Scrypt wrote 05/19/21 by Paf
# Choose how many rounds we want to time

rounds = int(input("How many rounds ?"))
waitingTime = int(input("How long to wait ?(sec)"))

while rounds > 0:
    restingTime = waitingTime
    while restingTime > 0:
        print(restingTime)
        restingTime -= 1
        time.sleep(1)
    rounds -= 1
    input(("Finish", "Go")[rounds])
