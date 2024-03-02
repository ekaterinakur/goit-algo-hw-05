import timeit
from boyer_moore import boyer_moore_search
from knuth_morris_pratt import kmp_search
from rabin_karp import rabin_karp_search

# Read the content of a file
def read_file(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()

# Measure execution time of a substring search algorithm
def measure_time(search_function, text, pattern):
    return timeit.timeit(lambda: search_function(text, pattern), number=100)

def print_results(results):
    print(f"\n{'Algorithm':^18} | {'Article 1 (existing substr)':^28} | {'Article 2 (existing substr)':^28} | {'Article 1 (fictional substr)':^28} | {'Article 2 (fictional substr)':^28}")
    print(f"{'':<18} | {'-'*121}")
    print(f"{'':<18} | {'Time':^16} | {'Idx':^9} | {'Time':^16} | {'Idx':^9} | {'Time':^16} | {'Idx':^9} | {'Time':^16} | {'Idx':^9}")
    print(f"{'-'*142}")
    for row in results:
        print("{:<18} | {:^16.6f} | {:^9} | {:^16.6f} | {:^9} | {:^16.6f} | {:^9} | {:^16.6f} | {:^9}".format(*row))
    print('\n')

if __name__ == "__main__":
    # Read the content of the text files
    article_1 = read_file("task_3/article_1.txt", encoding='cp1251')
    article_2 = read_file("task_3/article_2.txt", encoding='cp1251')

    existing_substring_1 = "Інтерполяційний пошук використовується для"
    existing_substring_2 = "Зв’язний список (linked list)"
    fictional_substring = "sergojegjkaeefwef"

    algorithms = [boyer_moore_search, kmp_search, rabin_karp_search]

    results = []

    for algorithm in algorithms:

        # Existing substring
        found_index_1 = algorithm(article_1, existing_substring_1)
        time_existing_article_1 = measure_time(algorithm, article_1, existing_substring_1)
        found_index_2 = algorithm(article_2, existing_substring_2)
        time_existing_article_2 = measure_time(algorithm, article_2, existing_substring_2)

        # Fictional substring
        found_index_3 = algorithm(article_1, fictional_substring)
        time_fictional_article_1 = measure_time(algorithm, article_1, fictional_substring)
        found_index_4 = algorithm(article_2, fictional_substring)
        time_fictional_article_2 = measure_time(algorithm, article_2, fictional_substring)

        results.append([
            ' '.join(word.capitalize() for word in algorithm.__name__.split('_')),
            time_existing_article_1,
            found_index_1,
            time_existing_article_2,
            found_index_2,
            time_fictional_article_1,
            found_index_3,
            time_fictional_article_2,
            found_index_4
        ])

    print_results(results)
