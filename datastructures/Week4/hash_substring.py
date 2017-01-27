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
    H[textLength - patternLength] = find_hash(text[textLength-patternLength-1:textLength-1],prime,x)
    

def get_occurrences(pattern, text):
    prime = 1000000007
    x = 263
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

