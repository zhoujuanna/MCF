##对于列表R_isom_p中的每一个元素e, \
##在字典partial_lambda的值v中找元素e中圆括号内用逗号隔开的字符串，\
##如果能找到, 那么用字典partial_lambda中对应的键k替换值v，输出替换后的列表R_isom_p。

def replace_values(dictionary, lst):
    new_lst = []
    for item in lst:
        for key, value in dictionary.items():
            item = item.replace(value, key)
        new_lst.append(item)
    return new_lst


partial_lambda = {'x3': 'a8', 'x2': 'a2', 'x8': 'a10', 'x1': 'a1', 'x6': 'a5', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}
R_isom_p = ['P1(a3,a9,a4)', 'P1(a3,a4,a1)', 'P1(a3,a5,a1)', 'P1(a3,a9,a5)', 'P1(a3,a9,a1)', \
            'P1(a5,a4,a10)', 'P1(a5,a3,a10)', 'P1(a9,a10,a3)', 'P1(a10,a5,a9)', 'P1(a1,a3,a2)', \
            'P1(a2,a1,a5)', 'P1(a2,a5,a8)', 'P1(a2,a1,a8)', 'P1(a8,a2,a10)', 'P1(a5,a2,a4)', \
            'P1(a5,a2,a3)', 'P1(a5,a10,a2)', 'P1(a10,a8,a5)', 'P1(a10,a8,a9)']

replaced_list = replace_values(partial_lambda, R_isom_p)
##print(replaced_list)
