# Roman Numbers

def get_value(s, rtn):
    t = 0
    ls = len(s)
    for i, j in enumerate(s):
        if i+1 < ls:
            if rtn[j] >= rtn[s[i+1]]:
                t += rtn[j]
            elif rtn[j] < rtn[s[i+1]]:
                t -= rtn[j]
        else:
            t += rtn[j]
    return t


if __name__ == "__main__":
    string_to_check = str(input())
    roman_to_integer = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = get_value(string_to_check, roman_to_integer)
    print(result)
