from functools import reduce

def run():
    #-----------filter---------------------
    # my_list = [1,4,5,6,9,13,19,21]
    # print(my_list)

    #list comprehension solution
    # odd = [i for i in my_list if i%2 != 0]
    # print(odd)

    #filter solution
    # odd = list(filter(lambda x: x%2 !=0,my_list))
    # print(odd)
    # ---------------------map------------
    # my_list = [1,2,3,4,5]
    # print(my_list)

    #list comprehension solution
    # squares = [i**2 for i in my_list]
    # print(squares)

    #map solution
    # squares = list(map(lambda x:x**2, my_list))
    # print(squares)

    #--------------------reduce-----------------
    my_list = [2,2,2,2,2]
    # all_multiplied = 1

    #for loop solution
    # for i in my_list:
    #     all_multiplied = all_multiplied * i
    # print(all_multiplied)

    #reduce solution
    all_multiplied = reduce(lambda a,b: a*b,my_list)
    print(all_multiplied)

if __name__ == '__main__':
    run()