def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path}")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document \n")
    letters = count_letters(text)
    sorted_letters = sort_dict(letters)
    for letter in sorted_letters:
        if letter['name'].isalpha():
            print(
                f"The '{letter['name']}' character was found {letter['count']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_dict(dict):
    list = []
    for key in dict:
        list.append({"name": key, "count": dict[key]})

    def sort_on(dict):
        return dict["count"]

    list.sort(reverse=True, key=sort_on)
    return list


def count_letters(string):
    string = string.lower()
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


main()
