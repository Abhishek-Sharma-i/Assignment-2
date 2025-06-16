def average(array):
    distinct_elements = set(array)
    return sum(distinct_elements) / len(distinct_elements)

if __name__ == '__main__':
    n = int(input("Enter the size of set:"))
    arr = list(map(int, input("Enter the elements:").split()))
    result = average(arr)
    print(result)