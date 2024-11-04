import sys
import string

import periodictable



f = sys.argv[1]
ct = open(f).read()

upper = string.ascii_uppercase

formatted = ""

for each in ct:
    if each in upper:
        formatted += " " + each
    else:
        formatted += each


print(formatted)

