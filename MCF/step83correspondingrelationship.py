import step4plambda as s4

##input - 
##new_pairs = [{'x8': 'a3'}, {'x1': 'a8'}, {'x6': 'a8'}, {'x1': 'a8'}]
##列表字典的每个元素（字典）中只包含一个键值对。 如果有重复的元素，那么去重。
##output - unique_pairs =  [{'x1': 'a8'}, {'x6': 'a8'}, {'x8': 'a3'}]

def deduplicate_list_dict(new_pairs):
    unique_pairs = [dict(t) for t in {tuple(d.items()) for d in new_pairs}]
##    print('unique_pairs = ', unique_pairs)
    return unique_pairs



##input -
pairs_2arg = [['P1(a1,x8,a2)', 'P1(a1,a3,a2)'], ['P1(a2,a5,x1)', 'P1(a2,a5,a8)'], ['P1(a2,a1,x6)', 'P1(a2,a1,a8)'], ['P1(a2,a1,x1)', 'P1(a2,a1,a8)']]
##输出列表pairs_2arg中每个元素的第1个元素和第2个元素所有参数（3个）一一对应的结果，\
##形成新字典，例如,对第一个元素，得:{ a1: a1, x8: a3, a2:a2}。 \
##删除键等于值的键值对，得{ x8:a3}。
##output  -  new_pairs =  [{'x8': 'a3'}, {'x1': 'a8'}, {'x6': 'a8'}, {'x1': 'a8'}]

def get_cr_rl(pairs_2arg): ##corresponding relationship
    new_pairs = []
    for p2 in pairs_2arg:
        t = s4.find_partial_lambda(p2[0], p2[1])
    ##    print(t)
        t = {k: v for k, v in t.items() if k != v}
    ##    print(t)
        new_pairs.append(t)
##    print('new_pairs = ', new_pairs)
    new_pairs = deduplicate_list_dict(new_pairs)
    return new_pairs

##print(get_cr_rl(pairs_2arg))
