from collections import Counter

def calculate_total_earnings():
    n = int(input("Enter the number of shoes:"))
    shoe_sizes = list(map(int, input("List of shoe sizes:").split()))
    inventory = Counter(shoe_sizes)
    customers = int(input("Enter the number of customers:"))
    total = 0

    for _ in range(customers):
        size, price = map(int, input("The price of the shoes:").split())
        if inventory[size] > 0:
            total += price
            inventory[size] -= 1

    print(total)

if __name__ == '__main__':
    calculate_total_earnings()
