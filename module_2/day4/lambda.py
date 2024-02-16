# #lambda for x
# f_x = lambda x: x**2 + 5*x + 3
# five = f_x(5)
# print(five)

# #lambda for x and y
# f_x = lambda x,y: x**2 + 5*x*y + 3
# fivee = f_x(5,2)
# print(fivee)

# # from function
# def f_x(x):
#     return x**2 + 5*x + 3

# print(f_x(5))

# #pass the list in function and store the output in list
# numbers = [1, 2, 3,4, 5, 6, 7, 8, 9, 10]
# y = [f_x(x) for x in numbers]
# print(y)
    
# map_example = list(map(lambda x: x ** 2, numbers))
# map_example1 = list(map(f_x, numbers))
# print(map_example)



# string = input("Enter a string: ")
# words = string.split()
# word_list = list(map(lambda string: string.upper(),words))
# print(word_list)

# my_string = "This is a demo that demo is demo so demo bye cye"
# # upper_string = my_string.upper()
# # upper_string_lambda = lambda x: x.upper()

# def func_upper(word):
#     if word.startswith("c"):
#         a= word.title()
#     else:
#         a = word.upper()
#     return a

# splited_list = my_string.split(" ")
# final_ans = list(map(func_upper, splited_list))
# print(final_ans)

# my_string = "This is world where we live and sleep"
# output = "THIS Is WORLD Where WE Live AND Sleep"
my_string = "This is world where we live and sleep"
def func_upper(word, index):
    if index % 2 == 0:
        result_word = word.upper()
    else:
        result_word = word.title()
    return result_word
result = " ".join([func_upper(word, index) for index, word in enumerate(my_string.split(" "))])
print(result)



