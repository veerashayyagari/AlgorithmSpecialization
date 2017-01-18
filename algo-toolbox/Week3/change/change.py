# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = 0
    coins += m//10
    rem = m%10    
    if(rem > 0):
    	coins += rem//5
    	rem = rem%5
    	coins += rem

    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
