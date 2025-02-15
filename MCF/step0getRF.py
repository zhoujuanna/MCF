import npt

def getRF(F1, F2):
##    F1, F2 = npt.input()
    print('Initial data: \nF1 = {} \nF2 = {}'.format(F1, F2))
##    print(len(F1.split('&')))
##    print(len(F2.split('&')))

##如果F1的文字数大于F2，那么交换。
    if len(F1.split('&')) > len(F2.split('&')):
        F1, F2 = F2, F1
##        print('F1 = {} \nF2 = {}'.format(F1, F2))
    
##把短公式中的所有的字母a(或者b)换成x。
    R = F1.replace('a', 'x').replace('b', 'x')
    F = F2
##    print('R = {} \nF = {} '.format(R, F))    
    return R, F


##input 
##input_string = 'P1(x1,x2,x3)&P1(x1,x2,x6)&P1(x2,x4,x6)&P1(x3,x2,x1)&P1(x2,x1,x4)'
##求出字符串input_string括号中以x开头的不重复的参数(所有参数放在一个集合中)\
##和参数个数。
##output - ({'x4', 'x2', 'x1', 'x3', 'x6'}, 5)  共5个参数，为 'x4', 'x2', 'x1', 'x3', 'x6'
def count_unique_x_parameters(input_string):
    parameters = set()
    for part in input_string.split('&'):
##        print('part = ', part)
        x_params = [x_param.strip(')') for x_param in part.split('(')[1].split(',')]
##        print('x_params = ',x_params)
        parameters.update(x_params)
##        print('parameters = ', parameters)
    count = len(parameters)
    return parameters, count
##input_string = "P1(x1,x2,x3)&P1(x1,x2,x6)&P1(x2,x4,x6)&P1(x3,x2,x1)&P1(x2,x1,x4)"
##result = count_unique_x_parameters(input_string)
##print(result)  # 输出括号中以x开头的不重复的参数个数


##获取一个文字中参数的个数。
####input - 
##s = 'P1(a1,a4,a2)'
##output - 3
def get_t(s):
    return len(s.split('(')[1].split(')')[0].split(','))
