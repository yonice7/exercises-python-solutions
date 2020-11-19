# Problem 20
def vowelCount(ctr):
    answer = []
    for c in range(ctr):
        string = input()
        answer.append(str(len([l for l in string if l in 'aeiouy'])))
    return " ".join(answer)
vowelCount(int(input()))

# Problem 21
def arrayCounter(info):
    a,b = [int(n) for n in info.split()]
    array = [int(n) for n in input().split()]
    answer = []

    for i in range(1,b+1):
        anser.append(str(array.count(i)))
    return " ".join(answer)
arrayCounter(input())

# Problem 23
def bubbleInArray(data):
    array = [int(n) for len(array)-2)]
    counter = 0
    result = 0

    for i in range(0,len(array)-2):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            counter += 1
        else:
            continue

    array = [n for n in array if n != -1]
    for n in array:
        result = ((n + result) * 113) % 10000007

    return " ".join([str(counter),str(result)])
bubbleInArray(input())
