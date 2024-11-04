m = 57983
p = int(open("p.txt").read().strip())

def find_modular_multiplicative_inverse(a, m):
    """Find modular multiplicative inverse of a under modulo m"""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    _, x, _ = extended_gcd(a, m)
    return (x % m + m) % m

def unpop(s):
    """Reverse the pop operation: x^42 = x^42 (XOR is its own inverse)"""
    return map(lambda x: chr(x^42), s)

def unbutter(s):
    """Reverse the butter operation using modular multiplicative inverse"""
    p_inverse = find_modular_multiplicative_inverse(p, m)
    return map(lambda x: x*p_inverse%m, s)

def unchurn(s):
    """Reverse the churn operation"""
    # Convert space-separated hex strings to integers and right-shift by 3
    nums = [int(x, 16) >> 3 for x in s.split()]
    # Rotate right by 16 positions
    rotated = nums[-16:] + nums[:-16]
    return rotated

def main():
    # Read the encoded message
    with open("message.txt", "r") as f:
        encoded = f.read().strip()
    
    # Reverse the encoding process
    # 1. First unchurn (converts from hex string to numbers)
    unchurned = unchurn(encoded)
    # 2. Then unbutter (applies modular multiplicative inverse)
    unbuttered = unbutter(unchurned)
    # 3. Finally unpop (XOR with 42)
    decoded = "".join(unpop(unbuttered))
    
    print(f"Decoded flag: {decoded}")

if __name__ == "__main__":
    main()
