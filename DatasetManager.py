def filter_rows(data, predicate):
    result = list(filter(predicate, data))
    return result


def select_columns(data, columns):
    result = [{col: row[col] for col in columns} for row in data]
    return result


def column_average(data, col):
    if not data:
        print("Error: dataset is empty.")
        return None

    try:
        return sum(row[col] for row in data) / len(data)
    except KeyError:
        print(f"Error: column '{col}' does not exist.")
        return None
    except TypeError:
        print(f"Error: column '{col}' is not numeric.")
        return None


def print_table(rows):
    print(f"{'Name':<10} {'Department':<15} {'Age':<6} {'Salary':<10}")
    print("-" * 52)
    for x in rows:
        print(f"{x['name']:<10} | {x['department']:<15} | {x['age']:<6} | {x['salary']:<10}")


def main():
    print_table(dataset)
    print("\nDataset Manager")

    while True:
        print("\n1. Filter by department")
        print("2. Filter by min salary")
        print("3. Column average")
        print("4. Exit")

        try:
            choice = int(input("Your Choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 4:
            return
        elif choice == 1:
            dept = input("Department: ")
            result = filter_rows(dataset, lambda row: row["department"] == dept)
            print_table(result)
        elif choice == 2:
            try:
                min_sal = int(input("Minimum salary: "))
            except ValueError:
                print("Invalid salary. Please enter a number.")
                continue
            result = filter_rows(dataset, lambda row: row["salary"] >= min_sal)
            print_table(result)
        elif choice == 3:
            col = input("Column (age/salary): ")
            avg = column_average(dataset, col)
            if avg is not None:
                print(f"Average {col}: {avg}")
        else:
            print("Invalid choice.")


dataset = [
    {"name": "Ana",    "department": "Engineering", "age": 29, "salary": 72000},
    {"name": "Ben",    "department": "Sales",       "age": 34, "salary": 58000},
    {"name": "Chloe",  "department": "Engineering", "age": 41, "salary": 95000},
    {"name": "Dane",   "department": "Marketing",   "age": 26, "salary": 51000},
    {"name": "Elena",  "department": "Sales",       "age": 38, "salary": 63000},
    {"name": "Farid",  "department": "Engineering", "age": 31, "salary": 81000},
    {"name": "Grace",  "department": "Marketing",   "age": 45, "salary": 67000},
    {"name": "Hugo",   "department": "Sales",       "age": 23, "salary": 47000},
]


if __name__ == "__main__":
    main()