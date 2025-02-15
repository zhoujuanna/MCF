##input - 
partial_lambda =  {'x1': 'b1', 'x2': 'b2', 'x3': 'b3'}
new_pl =  {'b2': 'b2', 'x4': 'b4', 'x6': 'b6'}

##把这两个字典合并为一个, 如果合并后的字典包含键和值相等的键值对，则删除
##output - {'x1': 'b1', 'x2': 'b2', 'x3': 'b3', 'x4': 'b4', 'x6': 'b6'}

def merg_lambda(partial_lambda, new_pl):

    ##字典解包操作符**， 用于将字典解包成关键字参数。支持一次性输入多个参数
    ##例
    ##def print_kwargs(a, b, c):
    ##    print(a, b, c)
    ##kwargs = {'a': 1, 'b': 2, 'c': 3}
    ##print_kwargs(**kwargs)
    ##上述代码会输出：
    ##1 2 3
    merged_dict = {**partial_lambda, **new_pl}
    ##print('merged_dict = ', merged_dict)

    # 检查并删除键和值相等的键值对
    merged_dict = {k: v for k, v in merged_dict.items() if k != v}

##    print(merged_dict)
    return merged_dict

##print(merg_lambda(partial_lambda, new_pl))
