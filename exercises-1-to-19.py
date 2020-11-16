# Problem 1
def sum_two():
    l = [int(s) for s in input().split()]

    import numpy as np
    return np.sum(l)

# Problem 2
def sum_loop():
    import numpy as np

    i = int(input())
    l = np.array([int(s) for s in input().split()])

    return np.sum(l[:i])

# Problem 3
def sum_pairs():

    i = int(input())
    l = []

    for i in range(i):
        import numpy as np
        l.append(np.sum([int(s) for s in input().split()]))
    return str(l).replace(',','').replace('[','').replace(']','')

# Problem 4
def min_two():
    import numpy as np

    index = int(input())
    lst = np.array([int(s) for s in input().split()])
    lst = np.reshape(lst, (index,2))
    lst = np.min(lst, axis=1)

    return str(lst).replace(',','').replace('[','').replace(']','').replace('\n', '').replace('  ',' ')

# Problem 5
def min_three():
    raw_lst = [int(s) for s in input().split()]
    split_lst = [raw_lst[i:i+3] for  i in range(0, len(raw_lst),3)]
    result_lst = [min(x) for x in split_lst]

    return str(result_lst).replace(',','').replace('[','').replace(']','').replace('\n', '').replace('  ',' ')

# Problem 6
def rounding():
    raw_lst = [int(s) for s in input().split()]
    split_lst = [raw_lst[i:i+2] for  i in range(0, len(raw_lst),2)]
    result_lst = [str(round(a/b)) for a,b in split_lst]

    return " ".join(result_lst)

# Problem 7
def far_cel():
    fahrTemps = [int(s) for s in input().split()]
    index = fahrTemps[0]
    cels = [round((f-32)*(5/9)) for f in fahrTemps[1:index+1]]
    return str(cels).replace(',','').replace('[','').replace(']','').replace('\n', '').replace('  ',' ')

# Problem 8
def arith_progr():
    import numpy as np
    index = int(input())
    lst = np.array([int(s) for s in input().split()])
    lst = np.reshape(lst, (index,3))

    result = []

    for arr in lst:
        a,d,n = arr
        Sn = int((n*(2*a+(n-1)*d))/2)
        result.append(Sn)

    return str(result).replace(',','').replace('[','').replace(']','')

# Problem 9
def triangles():
    raw_lst = [int(s) for s in input().split()]
    split_lst = [raw_lst[i:i+3] for i in range(0, len(raw_lst)-2,3)]
    outputs = []

    for t in split_lst:
        a,b,c = t
        if a+b>c and b+c>a and c+a>b:
            outputs.append(1)
        else:
            outputs.append(0)
    return str(outputs).replace(',','').replace('[','').replace(']','')

# Problem 10
def lin_function():
    from scipy.stats import linregress
    raw_lst = [int(s) for s in input().split()]
    split_lst = [raw_lst[i:i+4] for i in range(0, len(raw_lst)-3,4)]
    outputs = []

    for v in split_lst:
        x1, y1, x2, y2 = v
        slope, intercept, r_value, p_value, std_err = linregress([x1,x2],[y1,y2])
        outputs.append(f"({int(slope)} {int(intercept)})")

    return " ".join(outputs)

# Problem 11
def sum_digits():
    raw_lst = [int(s) for s in input().split()]
    split_lst = [raw_lst[i:i+3] for i in range(0, len(raw_lst)-2,3)]
    outputs = []

    for arr in split_lst:
        a,b,c = arr
        finalNumber = a*b+c
        sum = 0

        while finalNumber > 0:
            sum += finalNumber%10
            finalNumber = finalNumber // 10

        outputs.append(sum)

    return str(outputs).replace(',','').replace('[','').replace(']','')

# Problem 13
def weighted_sum():
    import numpy as np
    rawLst = [int(s) for s in input().split()]
    output = []

    for n in rawLst:
        numArr = np.array([int(i) for i in str(n)])
        enumArr = np.arange(1,np.shape(numArr)[0]+1)
        multArr = enumArr * numArr
        output.append(int(np.sum(multArr)))

    return str(output).replace(',','').replace('[','').replace(']','')

# Problem 15
def extremes():
    import numpy as np

    ext = []
    rawLst = np.array([int(i) for i in input().split()])

    ext.append(str(np.max(rawLst)))
    ext.append(str(np.min(rawLst)))

    return " ".join(ext)

# Problem 16
def average():
    import statistics as st

    limit = int(input())
    ctr = 1
    ext = []

    while ctr <= limit:
        rawLst = [int(i) for i in input().split()]
        rawLst = rawLst[0:-1]
        ext.append(str(round(st.mean(rawLst))))
        ctr += 1
    return " ".join(ext)

# Problem 17
def checksum():
    arr = [int(n) for n in input().split()]
    result = 0

    for n in arr:
        result = ((n + result) * 113) % 10000007
    return result

# Problem 18
def squareRoot():
    rawArr = [int(n) for n in input().split()]
    arr = [rawArr[i:i+2] for i in range(0,len(rawArr)-1,2)]
    results = []

    for a in arr:
        x,n = a
        r = 1.0
        for i in range(0,n):
            r = (r + x / r) / 2
        if r.is_integer():
            results.append(str(int(r)))
        else:
            results.append(str(r))
    return " ".join(results)

# Problem 19
def matchingBrackets(ctr):
    answer = []
    for c in range(ctr):
        string = input()
        data = ''.join([c for c in string if c in '()[]{}<>'])

        lengthPlus = len(data) + 1

        while len(data) < lengthPlus:
            lengthPlus = len(data)
            data = data.replace('()','').replace('[]','').replace('{}','').replace('<>','')

        if len(data) > 0:
            answer.append('0')
        else:
            answer.append('1')

    return " ".join(answer)
matchingBrackets(int(input()))
# 1. Create a list for the answers
# 2. Get all pair brackets from the string
# 3. Use string.replace to eliminate all bracket pairs until there are no more pairs
# 4. While loop until len(data) eventually turns to 0, if it's 0, they are all matching brackets
# 5. Even when they're not all matching brackets, lengthPlus and len(data) will turn equal sometime
# Credits to @ValueWasTaken on github
