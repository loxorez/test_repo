"""
Записывает в новый файл все слова в алфавитном порядке из другого файла с
текстом. Каждое слово на новой строке.
* (доп.) Рядом со словом укажите сколько раз оно встречалось в тексте
"""

directory = '/home/qa/My_project/test_repo/Home6/Files to work with/'


def words_counter(filename):
    """
    Return words with counters
    :param filename: path to source_file
    :return: dict with word as key, number as value
    """
    with open(filename, 'r') as object:
        words_dict = {}
        for line in object:
            for word in line.split():
                if word not in words_dict and word.isalpha():
                    words_dict[word.lower()] = 1
                elif word in words_dict and word.isalpha():
                    words_dict[word.lower()] += 1
    return words_dict


def print_in_file(source_file, destination_file, top_counters=False):
    """
    Write words from source file in alphabetic order to destination file.
    To sort words by top count order use top_counters argument
    :param source_file: path to source_file
    :param destination_file: path to destination_file
    :param top_counters: if key is True function sorted words by top count
    """
    words_dict = words_counter(source_file)
    with open(destination_file, 'w') as subject:
        sorted_words = sorted(words_dict.keys())
        if top_counters is False:
            for word in sorted_words:
                print(f"{word}: {words_dict[word]}", file=subject)
        elif top_counters is True:
            items = sorted(words_dict.items(), key=lambda i: i[1], reverse=True)
            for word in items:
                print(f"{word[0]}: {word[1]}", file=subject)


if __name__ == "__main__":
    print_in_file(directory + 'A_Long_Goodbye-Raymond_Chandler.txt', directory + 'With_Word_counters.txt')

