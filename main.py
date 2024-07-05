
def count_words(file_content):
    words = file_content.split()
    return len(words)


def char_freq(file_content):
    freq = {}
    
    for char in file_content.lower():
        if char not in 'abcdefghijklmnopqrstuvwxyz':
            continue
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    return freq


def main():
    with open('./books/frankenstein.txt', 'r') as f:
        file_contents = f.read()


    word_count = count_words(file_contents)
    char_count = char_freq(file_contents)

    print( "--- Begin report of books/frankenstein.txt ---")
    print(f'{word_count} words found in the document\n')

    sorted_char_count = dict(sorted(char_count.items()))
    for key, item in sorted_char_count.items():
        print(f"The '{key}' character was found {item} times")

    print('-- End report ---')

main()