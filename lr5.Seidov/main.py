from strings import *
if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4]))
    print(modify_list([1, 2, 3, 4], 2, 10))
    print(compare_lists([1, 2, 3], [1, 2, 3]))
    print(select_range([1, 2, 3, 4, 5, 6, 7], 1, 5, 2))
    print(create_list(1, 2, 3, 4))
    print(insert_element([1, 2, 3], 1, 10))
    print(merge_and_sort_lists(len, [3, 2], [1, 4]))
    create_and_check_list()
    print(merge_with_limit([1, 2], [3, 4], [5, 6], limit=5))

    print(sort_ascending([3, 1, 2]))  # [1, 2, 3]
    print(sort_descending([3, 1, 2]))

    print(extract_min([3, 1, 4, 1, 5]))
    print(sum_tuples((1, 2), (3, 4)))  # (1, 2, 3, 4)
    print(count_occurrences((1, 2, 3, 1, 2), 1))
    print(tuple_types(1, "hello", 3.5, True))
    print(check_in_tuple((1, 2, 3), 2))
    print(create_2d_list(3, 2, 0))
    print(get_keys({"a": 1, "b": 2}))  # dict_keys(['a', 'b'])
    print(get_values({"a": 1, "b": 2}))  # dict_values([1, 2])
    print(get_item({"a": 1, "b": 2}, "a"))  # 1
    print(count_key_occurrences({"a": 1}, {"b": 2}, {"a": 3}, key="a"))
    complex_dict = {"a": {"b": {"c": 5}}}
    print(find_element(complex_dict))


