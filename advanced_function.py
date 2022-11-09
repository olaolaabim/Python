from functools import reduce


def title(name):
    print(name)  # Press Ctrl+F8 to toggle the breakpoint.
if __name__ == '__main__':
    title("Advanced Funtion")

    #map
    my_list = [1, 2, 3]
    def multiply_by2(item):
        return item * 2
    print(list(map(multiply_by2, my_list)))
    print(my_list)

    #filter
    def only_odd(item):
        return item % 2 != 0
    print(list(filter(only_odd, my_list)))

    #zip
    your_list = (10, 20, 30)
    their_list = (5, 4, 3)
    print(list(zip(my_list, your_list, their_list)))


    #reduce
    def accumulator(acc, item):
        print(acc, item)
        return acc + item
    print(reduce(accumulator, my_list, 0))

    #lambda
    print(reduce(lambda acc, item: acc + item, my_list))

    #Tasks
    print(list(map(lambda item: item ** 2, my_list)))#calculating square
    a = [(0, 2), (4, 3), (10, -1), (9, 9)]##   list sorting
    a.sort(key=lambda x: x[1])
    print(a)

    #List Comprehension
    my_list2 = [char for char in 'hello']
    my_list3 = [num for num in range(0, 100)]
    my_list4 = [num ** 2 for num in range(100)]
    my_list5 = [num for num in my_list4 if num % 2 == 0]
    print(my_list2)
    print(my_list3)
    print(my_list4)
    print(my_list5)

    #Dictionary
    simple_dict = {
        'a': 1,
        'b': 2
    }
    my_dict = {key: value ** 2 for key, value in simple_dict.items()}
    my_dict_1 = {num: num ** 2 for num in [1, 2, 3]}
    print(my_dict)
    print(my_dict_1)

    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    some_list1 = list(set([num for num in some_list if some_list.count(num) > 1]))
    print(some_list1)