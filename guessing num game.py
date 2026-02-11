def guess(srange, erange):
    if srange>erange:
        return True

    mid=(srange+erange)//2

    print(f"Is the number {mid}? (Y/N):",end="")
    user = input().strip()

    if user in ("Y", "y"):
        print("Successfully guessed number")
        return False

    elif user in ("N", "n"):
        print(f"Is your number greater than {mid}? (Y/N):",end="")
        user = input().strip()

        if user in ("Y","y"):
            return guess(mid+1,erange)
        
        elif user in ("N","n"):
            return guess(srange,mid - 1)
        
        else:
            print("Invalid input")
            return guess(srange, erange)
    else:
        print("Invalid input")
        return guess(srange,erange)


if __name__ == "__main__":
    print("guess a number")
    
    srange= int(input("enter start range:"))
    erange = int(input("enter end range:")) 

    print("think of a number between")

    out = guess(srange,erange)

    if out:
        print("Couldn't guess it")
