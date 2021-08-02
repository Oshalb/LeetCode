# Two sums

def check_sums(a, t):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if abs(a[i] + a[j]) == t:
                return [i, j]


def check_sum_hash_optimized(a, t):
    d = {}
    for i, j in enumerate(a):
        diff = t - a
        if diff in d:
            return [d[diff], i]
        d[j] = i


if __name__ == "__main__":
    number_to_check = input()  # list(map(int, input().rstrip().split()))
    target_to_compare = int(input())
    result = check_sums(number_to_check, target_to_compare)
    print(result)
