import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alpha[size-1:i:-1]
        center = alpha[i]
        right = alpha[i+1:size]
        line = '-'.join(left + center + right)
        line = line.center(4*size - 3, '-')
        lines.append(line)

    full_pattern = lines[::-1] + lines[1:]
    for line in full_pattern:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)