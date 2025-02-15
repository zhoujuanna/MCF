import re

##input - 
R = ['P1(x1,a2,x2)', 'P1(x2,x1,x6)', 'P1(x2,x6,x3)', 'P1(x2,x1,x3)', 'P1(x3,x2,x8)', 'P1(a2,a5,x1)', 'P1(a2,x6,x1)',\
     'P1(a2,a1,x6)', 'P1(a2,a1,x1)', 'P1(a5,a1,x6)', 'P1(x6,x2,a5)', 'P1(x6,x2,a2)', 'P1(x6,a5,x8)', 'P1(x6,a2,x8)',\
     'P1(x6,x8,x2)', 'P1(a1,x8,a5)', 'P1(a1,x8,a2)', 'P1(x8,x3,x6)', 'P1(x8,x6,a1)', 'P1(x8,x3,a1)']
F = ['P1(a1,a3,a2)', 'P1(a2,a5,a8)', 'P1(a2,a1,a8)', 'P1(a3,a4,a1)', 'P1(a3,a5,a1)', 'P1(a3,a9,a4)', 'P1(a3,a9,a5)',\
     'P1(a3,a9,a1)', 'P1(a4,a3,a6)', 'P1(a4,a6,a5)', 'P1(a5,a2,a3)', 'P1(a5,a2,a4)', 'P1(a5,a3,a7)', 'P1(a5,a3,a10)',\
     'P1(a5,a4,a7)', 'P1(a5,a4,a10)', 'P1(a5,a7,a2)', 'P1(a5,a10,a2)', 'P1(a6,a4,a9)', 'P1(a6,a7,a4)', 'P1(a6,a9,a7)', \
     'P1(a7,a5,a6)', 'P1(a7,a6,a10)', 'P1(a8,a2,a10)', 'P1(a9,a6,a3)', 'P1(a9,a10,a6)', 'P1(a9,a10,a3)',\
     'P1(a10,a7,a9)', 'P1(a10,a5,a9)', 'P1(a10,a8,a7)', 'P1(a10,a8,a5)', 'P1(a10,a8,a9)']
used =  ['a2', 'a1', 'a5']
##分别从列表R和F中找出同时包含列表used中至少两个元素的元素。
##output - result_R = ['P1(a2,a5,x1)', 'P1(a2,a1,x6)', 'P1(a2,a1,x1)', 'P1(a5,a1,x6)', 'P1(a1,x8,a5)', 'P1(a1,x8,a2)'] 
##result_F = ['P1(a1,a3,a2)', 'P1(a2,a5,a8)', 'P1(a2,a1,a8)', 'P1(a3,a5,a1)', 'P1(a5,a2,a3)', 'P1(a5,a2,a4)', 'P1(a5,a7,a2)', 'P1(a5,a10,a2)']

def find_2elements_in_R_and_F(used, R, F):
    result_R = [r for r in R if sum(u in re.findall(r'\((.*?)\)', r)[0].split(',') for u in used) >= 2]
##    result_F = [f for f in F if sum(u in f for u in used) >= 2]
    result_F = [f for f in F if sum(u in re.findall(r'\((.*?)\)', f)[0].split(',')  for u in used) >= 2]
##result_F = [f for f i...该语句的功能等价于下面的1-11行代码的功能
##    for f in F:                                                   ##1
##        args_pr = re.findall(r'\((.*?)\)', f)[0]       ##2
##    ##    print('\nargs_pr = ', args_pr)              ##3
##        args = args_pr.split(',')                             ##4
##    ##    print('args = ', args)                              ##5
##
##        r = [u in args for u in used]                     ##6
##    ##    print('r = ', r)                                        ##7
##        t = sum(r)                                              ##8
##    ##    print('t = ' ,t)                                        ##9
##        if t >= 2:                                                ##10
##            print('f = ', f)                                      ##11
    
    return result_R, result_F

##result_R, result_F = find_elements_in_R_and_F(used, R, F)
####print("元素包含used中至少两个元素的列表R中的元素:")
##print('result_R = {} \nresult_F = {}'.format(result_R, result_F))
####print("元素包含used中至少两个元素的列表F中的元素:")
####print(result_F)

##-------------------------
##分别从列表R和F中找出同时包含列表used中1个元素的元素。
def find_1element_in_R_and_F(used, R, F):
    result_R = [r for r in R if sum(u in re.findall(r'\((.*?)\)', r)[0].split(',') for u in used) == 1]
##    result_F = [f for f in F if sum(u in f for u in used) >= 2]
    result_F = [f for f in F if sum(u in re.findall(r'\((.*?)\)', f)[0].split(',')  for u in used) == 1]
   
    return result_R, result_F

##-------------------------
##分别从列表R和F中找出同时包含列表used中0个元素的元素。
def find_0element_in_R_and_F(used, R, F):
    result_R = [r for r in R if sum(u in re.findall(r'\((.*?)\)', r)[0].split(',') for u in used) == 0]
##    result_F = [f for f in F if sum(u in f for u in used) >= 2]
    result_F = [f for f in F if sum(u in re.findall(r'\((.*?)\)', f)[0].split(',')  for u in used) == 0]
   
    return result_R, result_F
