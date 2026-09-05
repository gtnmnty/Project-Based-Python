import time

# a = [1, 2, 3]
# b = [10, 20, 30]
# c = []
# new_list = [a + b for a, b in zip(a, b)]
# print(new_list)

# for i in range(len(a)):
#     c.append(a[i] + b[i])

# test = list(zip(a, b))
# print(test)

def add_by_index(a, b):
    if check_list(a, b) == 0: return

    start = time.perf_counter()
    new_list = [a + b for a, b in zip(a, b)]
    end = time.perf_counter()
    zip_speed = end - start

#   ———————————— for loop ver ————————————
    c = []
    length = max(len(a), len(b))
    start = time.perf_counter()
    for i in range(length):
        c.append(a[i] + b[i])
    end = time.perf_counter()
    loop_speed = end - start

    if len(new_list) <= 10:
        print(f"Zip Version: {new_list}")
        print(f"For Loop Version: {c}")

    print(f"\n[Addition Speed]")
    print(f"Zip/Comprehension: {zip_speed:.6f} seconds")
    print(f"Standard For Loop: {loop_speed:.6f} seconds")


def scale(a, b):
    if check_list(a, b) == 0: return

    # Skip manual factor input if running the huge benchmark
    if len(a) > 10 and len(b) > 10: factor = 2
    else:
        while True:
            factor = int(input("Enter the value of a factor: "))
            if factor != 0: break

    start = time.perf_counter()
    scaled_a = [x * factor for x in a]
    scaled_b = [x * factor for x in b]
    end = time.perf_counter()
    time_comp = end - start

#   ———————————— for loop ver ————————————
    start = time.perf_counter()
    c = []
    length = min(len(a), len(b))
    for i in range(length):
        c.append(a[i] * factor)

    d = []
    for i in range(length):
        d.append(b[i] * factor)
    end = time.perf_counter()
    time_loop = end - start

    if len(scaled_a) <= 10:
        print(f"Scaled A: {scaled_a}")
        print(f"Scaled B: {scaled_b}")
        print(f"For Loop Version A: {c}")
        print(f"For Loop Version B: {d}")

    print(f"\n[Scaling Speed]")
    print(f"List Comprehension: {time_comp:.6f} seconds")
    print(f"Standard For Loop : {time_loop:.6f} seconds")


def dot_product(a, b):
    if check_list(a, b) == 0: return

    start = time.perf_counter()
    sum_of_prod = sum(x * y for x, y in zip(a, b))
    end = time.perf_counter()
    time_gen = end - start

#   ———————————— for loop ver ————————————
    start = time.perf_counter()
    product = []
    length = min(len(a), len(b))
    for i in range(length):
        product.append(a[i] * b[i])
    sumof_prod = sum(product)
    end = time.perf_counter()
    time_loop = end - start

    print(f"Sum of products: {sum_of_prod}")
    print(f"For Loop Sum of products: {sumof_prod}")

    print(f"\n[Dot Product Speed]")
    print(f"Generator + Sum  : {time_gen:.6f} seconds")
    print(f"Loop + Append+Sum: {time_loop:.6f} seconds")


def check_list(a, b):
    if not a or not b:
        print("Error: One or both lists are empty!")
        return 0

    return 1


def enter_input():
    # 1. Asks for a raw string input
    # 2. Split the spaces AND convert each
    #    piece to an int all at once
    raw_a = input("\nEnter the values for list A: ")
    list_a = [int(x) for x in raw_a.split()]

    raw_b = input("Enter the values for list B: ")
    list_b = [int(x) for x in raw_b.split()]

    return list_a, list_b


def main():
    print("Welcome to Vectorization")
    print("1. Add values alternatively")
    print("2. Scale by Multiplication")
    print("3. Product and Sum")
    print("4. Speed Test")
    print("5. Exit")

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            a, b = enter_input()
            add_by_index(a, b)

        elif choice == 2:
            # Scaling usually only requires
            # one list, so we grab 'a'
            a, b = enter_input()
            scale(a, b)

        elif choice == 3:
            a, b = enter_input()
            dot_product(a, b)

        elif choice == 4:
            print("\nGenerating 100,000 elements for testing...")
            large_list_a = list(range(100000))
            large_list_b = list(range(100000))

            print("--- Running Benchmarks ---")
            add_by_index(large_list_a, large_list_b)
            scale(large_list_a, large_list_b)
            dot_product(large_list_a, large_list_b)

        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# This runs the main function when you start the script
if __name__ == "__main__":
    main()