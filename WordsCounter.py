
# This function runs to count every word in out input
# passed down. We can use Counter from collections, but
# as a practice, we won't.

# words.lower().split() converts the string into lower case
# and use the spaces in the string as seperator.
# if we don't save it into a var, it will scan
# through the input char by char.
def count_words(text):
    counts = {}
    words = text.lower().split()


    # Iterates to the words list one by one with the values
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # list(counts.values()) return a standard format list of the counts per word
    # counts returns {"key/word", value/count}
    return counts

def top_n(texts):
    if not texts: return

    words_list = count_words(texts)
    if not words_list: return

    print("\nAsc or Desc? Pick 1 or 2 only")
    print("1. Low to High")
    print("2. High to Low")
    print("3. Exit")

    is_reverse = True
    try:
        while True:
            choice = int( input("What is your choice: ") )
            if choice == 3:
                print("Bye bye")
                return
            elif choice == 2:
                is_reverse = True
                break
            elif choice == 1:
                is_reverse = False
                break
            else:
                print("Invalid number. Please pick 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    ranked_list = sorted(words_list.items(), key= lambda item: item[1], reverse=is_reverse)

    # enumerate returns an object where
    # the starts serve as a key for each value
    print("\n ——————— Ranked List ———————")
    for rank, (word, count) in enumerate(ranked_list, start=1):
        print(f"{rank}. {word}: {count}")


def input_text():
    txt_input = str(input("Please type the word(s): "))

    return txt_input

def main():
    print("Words Counter")

    print("1. Count Words")
    print("2. Rank by count (ASC / DESC)")
    print("3. Exit")

    while True:
        try:
            choice = int(input("\nPick your choice between the menu: "))
            if choice == 3:
                print("Bye bye")
                return
            elif choice == 1:
                text = input_text()
                print(count_words(text))
            elif choice == 2:
                text = input_text()
                top_n(text)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Input a valid option")


if __name__ == "__main__":
    main()