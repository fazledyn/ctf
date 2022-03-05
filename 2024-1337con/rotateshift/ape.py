import hashlib as h
import string


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


l_flag = 40
hash_40 = "e879a6efc4dfb4ea2214e5adffb7df82109fc2d58aeaca77cd4b69cb3770314d"
print(len(hash_40))

charset = string.printable
print(charset)

flag = "flag{"
hash_test = RSH(flag, 40)
print(hash_test)


import hashpumpy
