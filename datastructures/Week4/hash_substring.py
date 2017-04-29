# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def find_hash(text,prime,x):	
	ans = 0
	for c in reversed(text):
		ans = ans * x + ord(c)
		
	return ans%prime

def precompute_hashes(text,patternLength,prime,x):
    textLength = len(text)
    H = [0]*(textLength - patternLength + 1)
    H[textLength - patternLength] = find_hash(text[textLength-patternLength:textLength],prime,x)
    y = 1 #x**patternLength
    for i in range((textLength - patternLength - 1),-1,-1):
        out = x*H[i+1] + ord(text[i]) - y*ord(text[i + patternLength])
        # python returns a positive integer on mod negative, but just for the best practice
        # in many language (-3%5) != (2%5) -> so using ((a%p) + p)%p instead of a%p
        H[i] = ((out%prime) + prime)%prime

    return H

def get_occurrences(pattern, text):
    prime = 1000000007
    x = 1
    
    result = []
    # Precompute all the hashes of the string for pattern length
    H = precompute_hashes(text,len(pattern),prime,x)

    # compute hash of the pattern
    h = find_hash(pattern,prime,x)

    #iterate through all precomputed hashes and compare
    for idx,patternHash in enumerate(H):
        # if equal then do a string comparison
        if (patternHash == h and text[idx : idx+len(pattern)] == pattern):
            result.append(idx)

    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

