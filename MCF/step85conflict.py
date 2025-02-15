
##input - 
##values_mmp =  [[{'x2': 'a10'}], [{'x3': 'a9'}], [{'x3': 'a4'}]]
# 合并具有相同键的元素到同一个字典中
##output - 
##[[{'x2': 'a10'}], [{'x3': 'a9'}, {'x3': 'a4'}]]

def merge_elements_same_key(values_mmp):
    # 创建一个空字典
    result_dict = {}

    # 合并具有相同键的元素到同一个字典中
    for sublist in values_mmp:
    ##    print('sublist = ', sublist)
        for subdict in sublist:
    ##        print('subdict = ', subdict)
            for key, value in subdict.items():
    ##            print('key, value = ', key, value)
                if key in result_dict:
                    result_dict[key].append({key: value})
    ##                print('result_dict = ', result_dict)
                else:
                    result_dict[key] = [{key: value}]
    ##                print('result_dict = ', result_dict)

    # 将字典转换为列表
    result_list = [list(val) for val in result_dict.values()]
##    print(result_list)
    return result_list

##-------------------------------

##partial_lambda =  {'x4': 'a2', 'x7': 'a1', 'x5': 'a5'}
##cr_rl2arg =  [{'x6': 'a8'}, {'x8': 'a3'}, {'x3': 'a5'}, {'x4': 'a7'}, {'x1': 'a8'}]
##对于列表cr_rl2arg中的每一个字典元素，判断该元素的键和值是否在字典partial_lambda中出现。\
##   如果列表cr_rl2arg中的每一个字典元素的键和值没有出现在字典中，那么返回True。
##检查新得到的可能的合一子与上一层的一个结点的冲突性。
##即，新得到的合一子的键和值都没有在已有的键值对中出现，则没有冲突。
##output - chkup =  [True, True, False, False, True]
def check_partial_lambda(partial_lambda, cr_rl2arg):
    result = []
    for d in cr_rl2arg:
        for key, value in d.items():
##            print(key, value)
            if key not in partial_lambda.keys() and value not in partial_lambda.values():
                result.append(True)
            else:
                result.append(False)
    return result


##------------

##有两个列表
##cr_rl2arg = [{'x6': 'a8'}, {'x8': 'a3'}, {'x1': 'a8'},{'x4': 'a8'},{'x1': 'a1'}] ,
##chkup = [True, True, True, False, False]
##按照以下方式生成一个新的列表：\
##如果chkup元素的值为True ， 那么将第1个列表cr_rl2arg中下标相同的元素保留。
##与上层的键值对检测冲突。
##output -  [{'x6': 'a8'}, {'x8': 'a3'}, {'x1': 'a8'}] 
def generate_new_list(lst1, lst2):
    new_list = [lst1[i] for i in range(len(lst1)) if lst2[i]]    
    return new_list


##------------
from itertools import product

##input -  cr_rl2arg = [{'x6': 'a8'}, {'x8': 'a3'}, {'x1': 'a8'}, {'x2': 'a8'}, {'x9': 'a3'}]
##对于该列表的每个元素，把字典元素值相同的若个个键值对分别移动一个列表中。
##output - mmp =  {'a8': [{'x6': 'a8'}, {'x1': 'a8'}, {'x2': 'a8'}], 'a3': [{'x8': 'a3'}, {'x9': 'a3'}]}
def move_matching_pairs(lst):
    matching_pairs = {}
    for d in lst:
##        print('\nd = ', d)
        for key, value in d.items():
##            print(key, value)
##            print('matching_pairs = ', matching_pairs)
            if value not in matching_pairs:
                matching_pairs[value] = []
            matching_pairs[value].append({key: value})
##            print('matching_pairs = ', matching_pairs)    
    return matching_pairs

##------------

##input - i =  {'x6': 'a8'} j =  {'x8': 'a3'}
##把两个字典合成一个
##output - {'x6': 'a8', 'x8': 'a3'}
def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}  # 使用字典解包来合并两个字典    
    return merged_dict


##-----------

def get_chd2(values_mmp):
    res = []
    ##以下if代码只涉及部分情况，其他的情况可能需要补
    if len(values_mmp[0]) == 1 and len(values_mmp[1]) == 1:
        if list(values_mmp[0][0].keys()) == list(values_mmp[1][0].keys()):
            values_mmp = merge_elements_same_key(values_mmp)
            print('values_mmp = ', values_mmp)
        
    else:
        for i, j in product(values_mmp[0], values_mmp[1]):
    ##        print('i = ', i, 'j = ',j)
            result = merge_dicts(i, j)
    ##        print('result = ', result)
            if len(result) == len(i) + len(j):
                res.append(result)
    ##    print('res = ', res)            
    ##            删除values_mmp的第一和第二个元素，用res代替（）            
        del values_mmp[0]
        del values_mmp[0]
    ##        print('values_mmp = ', values_mmp)
        values_mmp.insert(0, res)
    ##    print('values_mmp = ', values_mmp)
    return values_mmp
    
def get_chd(values_mmp):
    if len(values_mmp) == 2:
        values_mmp = get_chd2(values_mmp)
    else:
##        长度为2，函数get_chd2(values_mmp)运行1次；\
##        长度为3，运行2次；长度为4，运行3次，以此类推。
        for k in range(len(values_mmp) -1):
            values_mmp = get_chd2(values_mmp)            
    return values_mmp

##-----------

def get_groups(cr_rl2arg):
    ##将本层有冲突的键值对分到不同组
    ##input - cr_rl2arg =  [{'x6': 'a8'}, {'x8': 'a3'}, {'x1': 'a8'}]
    ##output - children = [{'x6': 'a8', x8': 'a3'}, {'x1': 'a8', x8': 'a3'}]

    mmp = move_matching_pairs(cr_rl2arg)
##    print('mmp = ', mmp)
    values_mmp = list(mmp.values())
##    print('values_mmp = ', values_mmp)

    children = get_chd(values_mmp)
    
    return children

##---------

##input - 
##new_pairs = [{'x8': 'a3'}, {'x1': 'a8'}, {'x6': 'a8'}, {'x1': 'a8'}]
##列表字典的每个元素（字典）中只包含一个键值对。 如果有重复的元素，那么去重。
##output - unique_pairs =  [{'x1': 'a8'}, {'x6': 'a8'}, {'x8': 'a3'}]

def deduplicate_list_dict(new_pairs):
    unique_pairs = [dict(t) for t in {tuple(d.items()) for d in new_pairs}]
##    print('unique_pairs = ', unique_pairs)
    return unique_pairs
##print('deduplicate_list_dict = ', deduplicate_list_dict(new_pairs))

##---------

##新得到的可能的合一子变成上一层的一个结点的若干子节点。
##input  - 
##partial_lambda = {'x4': 'a2', 'x7': 'a1', 'x5': 'a5'}
##    cr_rl2arg = [{'x6': 'a8'}, {'x8': 'a3'}, {'x1': 'a8'},{'x4': 'a7'},{'x3': 'a5'},{'x1': 'a8'}]
##output - children =  [{'x8': 'a3', 'x6': 'a8'}, {'x8': 'a3', 'x1': 'a8'}]
def get_children(partial_lambda, cr_rl2arg):

    ##去重
    cr_rl2arg = deduplicate_list_dict(cr_rl2arg)
##    print('cr_rl2arg = ', cr_rl2arg)
    
    ##检测冲突
    chkup = check_partial_lambda(partial_lambda, cr_rl2arg)
##    print('chkup = ', chkup)

    ##删除有冲突的键值对
    cr_rl2arg = generate_new_list(cr_rl2arg, chkup)
##    print('cr_rl2arg = ', cr_rl2arg)

##有冲突的置换分组
    children  = get_groups(cr_rl2arg)
##    print('children = ', children)

    return children




def main():
    partial_lambda = {'x4': 'a2', 'x7': 'a1', 'x5': 'a5'}
    cr_rl2arg = [{'x6': 'a8'}, {'x8': 'a3'}, {'x1': 'a8'},{'x4': 'a7'},{'x3': 'a5'},{'x1': 'a8'}]
    print('chileren = ', get_children(partial_lambda, cr_rl2arg))
    
    


if __name__ == '__main__':
    main()
