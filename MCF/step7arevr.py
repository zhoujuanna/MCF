##input -
##R = ['P1(b1,b2,x6)', 'P1(b2,x4,x6)', 'P1(b2,b1,x4)'] 
R = ['P1(b1,b2,b6)','P1(b2,b4,b6)','P1(b2,b1,b4)']

##如果字符串R中包含有x开头的参数，输出有变量，返回False，\
##否则输出没变量返回True。
##output - There are variables in the formula R    False
##
def arevr(R):
    if any('x' in param for item in R for param in item.split('(')[1].split(',')):
##        print('There are variables in the formula R')
        return False
    else:
##        print('There are no variables in the formula R')
        return True

##print('arevr(R) = ', arevr(R))



##input -
R = ['P1(x1,x4,x2)', 'P1(x2,x1,x6)', 'P1(x2,x6,x3)']
##判断列表R元素的参数是否都是以x开头的字符串，如果是, 输出True，否则输出False。
##R元素参数是R元素括号中的。比如：R第一个元素'P1(x1,x4,x2)'的参数为x1,x4,x2。
##output - True
##input - 
##R = ['P1(x1,x4,x2)', 'P1(a2,x1,x6)', 'P1(x2,x6,x3)']
##output - False
def allparam_v(R):
    for item in R:
        parameters = item[item.find("(")+1:item.find(")")].split(',')
        for param in parameters:
            if not param.startswith('x'):
                return False
    return True

result = allparam_v(R)
##print(result)
