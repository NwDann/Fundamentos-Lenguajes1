
def guessing():
    global sequence, prev_correctBits
    for i in range(N):
        sequence[i] = 1 - sequence[i]  # Changing from 0 to 1 and from 1 to 0
        outPut = "Q " + " ".join(map(str, sequence))
        print(outPut)
        sys.stdout.flush()
        correctBits = int(input())
        
        if correctBits == N:
            return True  # Correct sequence
            
        elif correctBits < N and correctBits > prev_correctBits:
            prev_correctBits = correctBits
            
        else:
            sequence[i] = 1 - sequence[i]  # Reversing the change
            
    return False

import sys

N = int(input())
sequence = [0] * N
prev_correctBits = 0

flag = guessing()

if flag:
    outPut = "A " + " ".join(map(str, sequence))
    print(outPut)
    sys.stdout.flush()
else:
    print("Sequence not guessed")
