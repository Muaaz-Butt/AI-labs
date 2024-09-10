import array

def sort_dict_by_value(d):
    print("1. Sorting dictionary by value:")
    print("Ascending:", dict(sorted(d.items(), key=lambda x: x[1])))
    print("Descending:", dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))

def check_key_exists(d, key):
    print(f"\n2. Checking if key '{key}' exists in dictionary:")
    print("Key exists" if key in d else "Key does not exist")

def merge_dicts(d1, d2):
    print("\n3. Merging two dictionaries:")
    merged = d1.copy()
    merged.update(d2)
    print(merged)

def add_item_to_tuple(t, item):
    print("\n4. Adding an item to a tuple:")
    new_tuple = t + (item,)
    print(new_tuple)

def create_tuple_different_types():
    print("\n5. Creating a tuple with different data types:")
    mixed_tuple = (1, "hello", 3.14, True)
    print(mixed_tuple)

def sum_list_items(lst):
    print("\n6. Sum of all items in a list:")
    print(sum(lst))

def get_largest_number(lst):
    print("\n7. Largest number from a list:")
    print(max(lst))

def add_members_to_set(s, members):
    print("\n8. Adding member(s) to a set:")
    s.update(members)
    print(s)

def reverse_array(arr):
    print("\n9. Reversing the order of items in the array:")
    arr.reverse()
    print(arr)

def create_and_access_array():
    print("\n10. Creating an array of 5 integers and accessing elements:")
    arr = array.array('i', [1, 2, 3, 4, 5])
    print("Array:", arr)
    print("First element:", arr[0])
    print("Last element:", arr[-1])

def main():
    # Task 1
    d = {'apple': 5, 'banana': 2, 'orange': 8, 'pear': 1}
    sort_dict_by_value(d)

    # Task 2
    check_key_exists(d, 'banana')
    check_key_exists(d, 'grape')

    # Task 3
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    merge_dicts(d1, d2)

    # Task 4
    t = (1, 2, 3)
    add_item_to_tuple(t, 4)

    # Task 5
    create_tuple_different_types()

    # Task 6
    lst = [1, 2, 3, 4, 5]
    sum_list_items(lst)

    # Task 7
    get_largest_number(lst)

    # Task 8
    s = {1, 2, 3}
    add_members_to_set(s, {4, 5})

    # Task 9
    arr = array.array('i', [1, 2, 3, 4, 5])
    reverse_array(arr)

    # Task 10
    create_and_access_array()

if __name__ == "__main__":
    main()