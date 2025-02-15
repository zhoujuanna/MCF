##import re

##input - qR = P1(x1,x2,x3)   qF = P1(b1,b2,b3)
##找部分lambda , 字典的键是字符串qR中的参数, 字典的值是与qR参数位置对应的qF中的参数
##output - {'x1': 'b1', 'x2': 'b2', 'x3': 'b3'}
def find_partial_lambda(qR, qF):
##    pattern = r'P1\(([\w,]+)\)'  # 匹配P1函数中的参数
####    print('pattern = ', pattern)
##    match_qR = re.match(pattern, qR)
##    match_qF = re.match(pattern, qF)
##    print('match_qR = {} \nmatch_qF = {}'.format(match_qR, match_qF))

    if qR and qF:
##        qR_params = match_qR.group(1).split(',')  # 提取qR中的参数并转为列表
##        qF_params = match_qF.group(1).split(',')  # 提取qF中的参数并转为列表
##        print('qR_params = {} \nqF_params = {}'.format(qR_params, qF_params))
        qR_params = qR.split('(')[1].split(')')[0].split(',')
        qF_params =  qF.split('(')[1].split(')')[0].split(',')
        parameter_mapping = dict(zip(qR_params, qF_params))  # 将qR和qF的参数以字典形式进行映射

        return parameter_mapping
    else:
        return None


# 示例输入
qR = "P1(x1,x2,x3)"
qF = "P1(b1,b2,b3)"
##print(qR.split('(')[1].split(')')[0].split(','))

result = find_partial_lambda(qR, qF)
##print(result)
