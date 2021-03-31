def dsa1_reverse(s, n):
    list1 = [0]*len(s)
    sout = ""
    for i in range(len(s)):
        if i + n < len(s):
            list1[i + n] = s[i]
        else:
            list1[i + n - 4] = s[i]
    for i in list1:
        sout += i
    return sout

def dsa1_factorialSum(n):
    cout = 0
    middlecout = 0
    for i in range(1, n+1):
        middlecout *= i
        cout += middlecout
    return cout

def dsa1_generateDict(keys, values):
    dict1 = {}
    for i in len(keys):
        dict1[keys[i]] = values[i]
    return dict1

def dsa1_en2num(s):
    outstring = ""
    num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3",
                "four": "4", "five": "5", "six": "6", "seven": "7",
                "eight": "8", "nine": "9"}
    list1 = s.split("-")
    for i in list1:
        outstring +=num_dict[i]
    return outstring

def dsa1_getUnion(s1,s2):
    set1 = set(s1)
    set2 = set(s2)
    return set1 & set2

def dsa1_getDays(y,m):
    y = int(y)
    m = int(m)
    date = {1: 31, 3: 31, 5: 31,6: 30, 7: 31, 8: 31,9: 30, 10: 31,11: 30, 12: 31}
    if y % 4 == 0 and y % 400 != 0:
        if m == 2:
            return 29
        else:
            return date[m]
    elif m == 2:
        return 28
    else:
        return date[m]

def dsa1_isNarcNum(n):
    n_string = str(n)
    cout = 0
    for i in n_string:
        cout += int(i) ** len(n_string)
    return cout == int(n)

def dsa1_writeNarcNum(max):
    fi = open("./narcissistic.txt", mode="w")
    for i in range(100, max + 1):
        if dsa1_isNarcNum(i):
            output = str(i) + "\n"
            _ = fi.write(output)
            fi.flush()
    fi.close()
    return None

def dsa1_readNarcNum():
    file = open("./narcissistic.txt", mode="r")
    list1 = []
    for i in file.readlines():
        list1.append(int(i))
    return list1

def dsa1_printTri(n):
    list1 = [[1]]
    for i in range(2, n+1):
        list2 = [0]*i
        for j in range(i):
            if j != 0 and j != i - 1:
                list2[j] = list1[i-2][j-1] + list1[i-2][j]
            else:
                list2[j] = 1
        list1.append(list2)
    for i in list1:
        for j in range(len(i)):
            if j != len(i) - 1:
                print(i[j], end=" ")
            else:
                print(i[j])



