def find_last_index(lst, element):
    return len(lst) - 1 - lst[::-1].index(element)

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
print(find_last_index(num_list, 10))
print(find_last_index(num_list, 30))
print(find_last_index(word_list, 'ruby'))
print(find_last_index(word_list, 'perl'))