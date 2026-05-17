import time

sentence="hello dosto keso ho aap sabi log hope your doing good make sure have to test speed how fast you could type."

print("\typing Speed tester\n")
print(sentence)
input("\n press Enter when you are ready")

start=time.time()
typed=input("\n start typing")
end=time.time()

elapsed=end-start
wpm=(len(typed.split())/elapsed)*60

correct=sum(1 for i in range(min(len(sentence),len(typed))) if sentence[i]==typed[i])
accuracy=(correct/len(sentence))*100

print(f"time taken:{elapsed:.2f} seconds")
print(f"typing Speed: {wpm:.2f} WPM")
print(f"accuracy: {accuracy:.2f}%")
