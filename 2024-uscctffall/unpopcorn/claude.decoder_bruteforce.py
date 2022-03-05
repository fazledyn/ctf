m = 57983

def try_decode(encoded_hex, p_value):

    def find_modular_multiplicative_inverse(a, m):
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
        return map(lambda x: chr(x^42), s)

    def unbutter(s):
        p_inverse = find_modular_multiplicative_inverse(p_value, m)
        return map(lambda x: x*p_inverse%m, s)

    def unchurn(s):
        nums = [int(x, 16) >> 3 for x in s.split()]
        rotated = nums[-16:] + nums[:-16]
        return rotated

    try:
        # Unchurn
        unchurned = unchurn(encoded_hex)
        # Unbutter
        unbuttered = unbutter(unchurned)
        # Unpop
        decoded = "".join(unpop(unbuttered))
        
        # Check if result contains mostly printable ASCII
        if all(32 <= ord(c) <= 126 for c in decoded):
            return decoded
    except:
        pass
    return None

def main():
    encoded = "3FB60 4F510 42930 31058 DEA8 4A818 DEA8 1AA88 65AE0 1C590 17898 1C590 29170 3FB60 55D10 29170 42930 6A7D8 4C320 4F510 5FC0 193A0 4F510 2E288 29170 643F8 31058 6A7D8 4A818 1AA88 1AA88"
    
    # Try values of p that are likely to produce valid results
    for p in range(1, m):
        if p % 1000 == 0:  # Progress indicator
            print(f"Trying p = {p}...")
        
        result = try_decode(encoded, p)
        if result:
            print(f"\nPossible decode found with p={p}:")
            print(result)
            # Break if we find something that looks like a flag
            if "flag{" in result.lower() or "}" in result:
                break

if __name__ == "__main__":
    main()
