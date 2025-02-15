import re

# input输入的字符串
input_str = 'P1(b1,b2,x6)&P1(b2,x4,x6)&P1(b2,b1,x4)'
##输出该字符串中R所有的参数。
##把x开头不重复的参数放到一个列表中，
##a或者b开头不重复的参数放到另外一个列表中。
##output - constants_R =  ['b2', 'b1']
##variables_R =  ['x4', 'x6']


def get_cn_vr(input_str):
    # 提取参数
    params = re.findall(r'\b\w+\d*\b', input_str)
    ##print('params = ', params)
    all_params = []

    # 提取所有参数并分类
    x_params = set()
    ab_params = set()

    for param in params:
        all_params.append(param)
        if param.startswith('x'):
            x_params.add(param)
        elif param.startswith('a') or param.startswith('b'):
            ab_params.add(param)

    variables_R = list(x_params)
    constants_R = list(ab_params)

##    print("variables_R = ", variables_R)
##    print("constants_R = ", constants_R)
    variables_R.sort()
    constants_R.sort()
##    print("variables_R = ", variables_R)
##    print("constants_R = ", constants_R)    
    return constants_R, variables_R 

##print(get_cn_vr(input_str))
