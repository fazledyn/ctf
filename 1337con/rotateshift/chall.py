import hashlib as h

FLAG = "flag{fake_flag}"
def RSH(df, n):
    while n > len(df):
        n -= len(df)
    ans = ["#"] * len(df)

    for i in range (len(df)):
        try:
            ans[i] = chr(ord(df[i-n])+13)
        except:
            pass
    return h.sha256("".join (ans).encode("utf-8")).hexdigest()


def banner():
    print("\n[+] Welcome to the Rotate Shift and Hashing service!")
    print("1: RSH on your own String")
    print("2: RSH on the flag")

while True:
    banner()
    try:
        choice = int(input("> "))
    except:
        print("Choice must be an integer")
        continue
    if choice == 1:
        custom = input("Enter your string: ")
        try:
            rsh = int(input("RSH: "))
        except:
            print("RSH must be an integer")
            continue
        print("[~] Result: " + RSH(custom, rsh))
    elif choice == 2:
        try:
            rsh = int(input("RSH: "))
        except:
            print("RSH must be an integer")
            continue
        print("[~] Result: " + RSH(FLAG, rsh))
    else:
        print('Invalid choice')

