import csv

# Finds the average after computing the sum of all
# values divided by the length of n
def find_mean(filtered_list):
    return sum(filtered_list) / len(filtered_list)

# Finds
def find_std_dev(f_list):
    if len(f_list) < 2: return 0.0

    m = find_mean(f_list)
    squared_diffs = [(x - m) ** 2 for x in f_list]
    divisor = len(f_list) - 1 if len(f_list) != 0 else 1
    res = (sum(squared_diffs) / divisor) ** 0.5

    return res

def column_stats(emp_list, column_name):
    if emp_list is {}: return "Employee list is empty or corrupted"

    # converts the value from string to float if the column exist in the dictionary
    # and if the number is convertable into float after
    # removing the first '.' and if isdigit() returns True
    filtered_list = [
        float(emp_info[column_name])
        for emp_info in emp_list.values()
        if column_name in emp_info and emp_info[column_name]
            .replace(".", "", 1).isdigit()
    ]

    # call the mean method with filtered_list as argument
    mean_val = find_mean(filtered_list)

    # call the std_dev method and return the value
    std_dev_val = find_std_dev(filtered_list)

    return mean_val, std_dev_val


def load_csv_file():
    emp_list = {}

    try:
        with open("utils/csv/employees.csv", mode="r", encoding="utf_8") as file:
            # DirectReader automatically consider the first line as headers and skip it
            lines = csv.DictReader(file)

            for row in lines:
                # Removes the id column and make it as key main dict
                emp_id = row.pop("id")

                # Saves the line to emp_list with the emp_id as index
                emp_list[emp_id] = row

        #print(emp_list)
        return emp_list

    except FileNotFoundError:
        return "File is either missing or corrupted."


def main():
    print("Welcome to Database")
    print("What would you like to do?")
    print("1. Read the Database")
    print("2. Write into the Database")
    print("3. Exit")

    db_data = load_csv_file()

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            print(db_data)
        elif choice == 2:
            print("\nAvailable Numeric Columns:")
            print("- Age\n- Years of EXP\n- Salary\n- Performance Score")

            while True:
                column = input("\nWhat column would you like to get: ").strip().lower()
                if column.isdigit() or column == "":
                    print("Invalid Input")
                    continue

                mean, std_dev = column_stats(db_data, column)
                print(f"\n--- Stats for {column} ---")
                print(f"Peak (Mean): {mean:.2f}")
                print(f"Spread (Std Dev): {std_dev:.2f}")

        elif choice == 3:
            print("RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()