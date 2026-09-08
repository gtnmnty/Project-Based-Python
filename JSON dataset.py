from tabulate import tabulate
import json

def print_dataset(dataset):
    if dataset is None: return

    #for book in dataset:
    #   print(f"Title: {book['title']} | Author: {book['author']} | Rating: {book['rating']}")
    print(tabulate(dataset, headers="keys", tablefmt="grid"))

def apply_filter(dataset, config):
    # Checks if either dataset or config is empty.
    if not dataset or not config:
        print("Error: Missing dataset or configuration filters.")
        return

    filtered_list = []

    # Loop through each book dictionary in the dataset
    for book in dataset:
        # Check if ALL filter criteria match this book
        # book.get(k) avoids KeyError if a filter key doesn't exist in the book
        if all(book.get(k) == v for k, v in config.items()):
            filtered_list.append(book)

    if filtered_list:
        print(tabulate(filtered_list, headers="keys", tablefmt="github"))
    else:
        # Converts config items into a readable string for the error message
        filter_str = ", ".join([f"{v}" for v in config.values()])
        print(f"No books found matching the criteria: {filter_str}")


def load_dataset():
    try:
        with open("utils/json/books.json", "r") as file:
            dataset = json.load(file)
            if dataset is not None:
                return dataset
    except FileNotFoundError:
        print("Can't find the file to begin with")

    return {}

def load_config():
    try:
        with open("utils/json/config.json", "r") as config:
            j_son = json.load(config)
            config_dict = dict(j_son)
            return config_dict
    except FileNotFoundError:
        print("config.json can not be found")
        return {}


def main():
    print("Welcome to JSON Dataset")
    print("What would you like to retrieve?")
    print("1. All the books")
    print("2. Get books by filter")
    print("3. Exit")

    # Loads the dataset to ensure every method can use it.
    dataset = load_dataset()

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            print(tabulate(load_dataset(), headers="keys", tablefmt="github"))
        elif choice == 2:   # Choice 2 uses config JSON as an input.
            apply_filter(dataset, load_config())
        elif choice == 3:
            print("RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()