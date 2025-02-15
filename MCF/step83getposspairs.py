def get_parameter_indexes(param_string):
    return {param: index for index, param in enumerate(param_string.split(','))}

##对于第1个列表lits_tR中的每一个元素er，\
##如果列表F的元素ef有2个与元素er相同且下标的参数，\
##那么把元素er和元素ef添加到新的列表poss_pairs中并且输出。\
##参数是圆括号中的用逗号隔开的以字母a开头，以数字结尾的字符串。\
##元素e的参数下标按照以下方式计算：\
##把元素e的圆括号中用逗号隔开的字符串转列表，\
##列表中元素的下标即为参数下标。比如， 元素'P1(a1,a3,a2)'中有三个参数，
##参数分别为a1，a3，a2， a1的下标为0，a3的下标为1，a2的下标为2。

def find_matching_pairs(lits_tR, F, t):
    poss_pairs = []

    for er in lits_tR:  # 时间复杂度 O(n)
        er_params = er.split('(')[1][:-1]
        er_param_indexes = get_parameter_indexes(er_params)

        for ef in F:  # 时间复杂度 O(k)
            ef_params = ef.split('(')[1][:-1]
            ef_param_indexes = get_parameter_indexes(ef_params)

            common_params = set(er_param_indexes.keys()) & set(ef_param_indexes.keys())  # 时间复杂度 O(min(m,p))

            matching_index_count = 0
            for param in common_params:  # 时间复杂度 O(min(m,p))
                if er_param_indexes[param] == ef_param_indexes[param]:
                    matching_index_count += 1  # O(1)

            if matching_index_count == t:  # O(1)
                poss_pairs.append((er, ef))  # O(1)
        
    return poss_pairs  # O(1)

lits_tR =  ['P1(a3,a4,x1)', 'P1(a3,a9,x6)', 'P1(a3,a9,x1)', 'P1(a4,a9,x6)', 'P1(a9,x8,a4)', 'P1(a9,x8,a3)']

##lits_tR = ['P1(a4,a3,x2)', 'P1(a3,x5,a4)', 'P1(a3,x6,a4)', 'P1(a3,a9,x5)', 'P1(a3,a9,x6)', 'P1(x5,a3,a9)', 'P1(a9,x5,a3)', 'P1(a9,x8,a3)']
F = ['P1(a1,a3,a2)', 'P1(a2,a1,a5)', 'P1(a2,a5,a8)', 'P1(a2,a1,a8)', 'P1(a3,a4,a1)', 'P1(a3,a5,a1)', \
     'P1(a3,a9,a5)', 'P1(a3,a9,a1)', 'P1(a4,a3,a6)', 'P1(a4,a6,a5)', 'P1(a5,a2,a3)', 'P1(a5,a2,a4)', \
     'P1(a5,a3,a7)', 'P1(a5,a3,a10)', 'P1(a5,a4,a7)', 'P1(a5,a4,a10)', 'P1(a5,a7,a2)', 'P1(a5,a10,a2)', \
     'P1(a6,a4,a9)', 'P1(a6,a7,a4)', 'P1(a6,a9,a7)', 'P1(a7,a5,a6)', 'P1(a7,a6,a10)', 'P1(a8,a2,a10)',\
     'P1(a9,a6,a3)', 'P1(a9,a10,a6)', 'P1(a9,a10,a3)', 'P1(a10,a7,a9)', 'P1(a10,a5,a9)', 'P1(a10,a8,a7)', \
     'P1(a10,a8,a5)', 'P1(a10,a8,a9)']

##poss_pairs = find_matching_pairs(lits_tR, F, 2)
##print('poss_pairs = {} \t len(poss_pairs) = {}'.format( poss_pairs, len(poss_pairs)))
