
##input - 
##lr = 'P1(b1,b2,x6)'
lr = 'P1(x1,x2,x6)'
##lf = 'P1(b1,b3,b5)'
cn_lr = ['b1', 'b2']
##output  -  {'b1': 1, 'b2': 2}
##计算列表cn_lr中的每个元素在字符串lr中的参数位置param_positions。\
##注意：lr中的参数共有3个位置，b1的位置为1，b2的位置为2 ,x6的位置为3.
##如果字符串lr中不包含cn_lr中的参数, 那么输出空字典。
def get_param_positions(lr, cn_lr):
    param_positions = {}
    for param in cn_lr:
    ##    print('param = ', param)
        if param in lr:
            position = lr.split(param, 1)[0].count(',') + 1
    ##        print('lr.split(param, 1) = ', lr.split(param, 1))
            param_positions[param] = position

##    print(param_positions)
    return param_positions

##print(get_param_positions(lr, cn_lr))
##print(get_param_positions(lf, cn_lr))



##----------------------------

##input -
##partial_lambda =  {'x4': 'a2', 'x7': 'a1', 'x5': 'a5'}
##new_pl =  {'x1': 'a5', 'a2': 'a2', 'x2': 'a3'}
##先在字典new_pl中删除键值对相等的键值对。
##如果字典new_pl某个键值对中的值已经出现在partial_lambda中，\
##那么输出False，否则输出True
##output  - False

def is_contrad(used, new_pl):

    # 删除键值对相等的键值对
    new_pl = {k: v for k, v in new_pl.items() if k != v}

    # 检查值是否出现在used中
##    result = all(value not in partial_lambda.values() for value in new_pl.values())
    result = all(value not in used for value in new_pl.values())
##    print(result)
    return result

##print(is_contrad(partial_lambda, new_pl))

