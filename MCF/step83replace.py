##input - 
##partial_lambda = {'x2': 'a6', 'x3': 'a7', 'x6': 'a1', 'x8': 'a10', 'x1': 'a5', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}
##R_isom_p = ['P1(a9,a10,a3)', 'P1(a10,a7,a9)', 'P1(a7,a6,a10)', 'P1(a3,a9,a5)', 'P1(a3,a9,a1)']

##用字典partial_lambda的键替换列表R_isom_p中存在于字典的值。、
##注意字典中的值和列表R_isom_p中的值必须完全相等。|
##比如：字典partial_lambda中有键值对 'x8': 'a10'和 'x6': 'a1'，、
##R中有P1(a9,a10,a3)，那么应该用x8代替a10, 结果为 P1(x7,x8,x4)，而不是P1(x7,x60,x4)。
##output -  ['P1(x7,x8,x4)', 'P1(x8,x3,x7)', 'P1(x3,x2,x8)', 'P1(x4,x7,x1)', 'P1(x4,x7,x6)']

def replace(R_isom_p, partial_lambda):

    # 反转 partial_lambda 字典
    inverse_partial_lambda = {v: k for k, v in partial_lambda.items()}

    # 用于存储结果的列表
    result = []

    # 遍历列表中的每个字符串
    for s in R_isom_p:
        # 去除 P1( 和 )，并分割得到元组参数
##        params = s[3:-1].split(',')
        params = s.split('(')[1].split(')')[0].split(',')

        prefix = s.split('(')[0] + '('
        
        # 遍历每个参数，如果在反转字典中有对应的键，则替换
        new_params = [inverse_partial_lambda.get(param, param) for param in params]
        
        # 拼接回字符串格式
        new_s = prefix + ','.join(new_params) + ')'

        # 向结果列表中添加新字符串
        result.append(new_s)

    # 打印结果
##    print(result)

    return result


##print(replace(R_isom_p, partial_lambda))
