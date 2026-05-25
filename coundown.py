import time
seconds = int(input("enter countdown time in seconds: "))
while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    timer = f"{mins:02}:{secs:02}"
    print(timer)
    time.sleep(1)
    seconds -= 1
print("Time's up")
