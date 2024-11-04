def max_sum_submatrix(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def solve_case(N, A):
    max_sum = max_sum_submatrix(A)
    
    for i in range(0, N, 2):
        modified = A[:]
        modified[i] *= -1
        modified[i + 1] *= -1
        current_max = max_sum_submatrix(modified)
        max_sum = max(max_sum, current_max)
    
    return max_sum

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0]) 
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])  
        A = list(map(int, data[index + 1].split()))  
        results.append(solve_case(N, A))
        index += 2
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()
