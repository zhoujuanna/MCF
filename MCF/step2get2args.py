from collections import Counter

##有一个嵌套列表
##lits_R = [[0, 'x1', 1, 'x2', 'P1(x1,x2,x3)'], [0, 'x1', 2, 'x3', 'P1(x1,x2,x3)'], [1, 'x2', 2, 'x3', 'P1(x1,x2,x3)'], \
##[0, 'x1', 1, 'x2', 'P1(x1,x2,x6)'], [0, 'x1', 2, 'x6', 'P1(x1,x2,x6)'], [1, 'x2', 2, 'x6', 'P1(x1,x2,x6)'], \
##    [0, 'x2', 1, 'x4', 'P1(x2,x4,x6)'], [0, 'x2', 2, 'x6', 'P1(x2,x4,x6)'], [1, 'x4', 2, 'x6', 'P1(x2,x4,x6)'], \
##    [0, 'x3', 1, 'x2', 'P1(x3,x2,x1)'], [0, 'x3', 2, 'x1', 'P1(x3,x2,x1)'], [1, 'x2', 2, 'x1', 'P1(x3,x2,x1)'], \
##    [0, 'x2', 1, 'x1', 'P1(x2,x1,x4)'], [0, 'x2', 2, 'x4', 'P1(x2,x1,x4)'], [1, 'x1', 2, 'x4', 'P1(x2,x1,x4)']]。
##输出列表每个元素中第2个元素和第4个元素出现次数最多的元素。\
##如果列表某个元素中的第2个元素和第4个元素互换以后，\
##与其他元素的第2个元素和第4个元素相等，换句话说，顺序不重要，\
##那么把该次数与之前已经统计过的次数相加。
def get2args(lits_R):
    # 统计每个元素中第2个元素和第4个元素出现的次数
    counts = Counter((min(element[1], element[3]), max(element[1], element[3])) for element in lits_R)
##    print('counts = ', counts)

    # 输出列表每个元素中第2个元素和第4个元素出现次数最多的元素
    most_common_element = max(counts, key=counts.get)

##    print("出现次数最多的元素:", most_common_element)
    return most_common_element


##input
##arg2_R = ('x1', 'x2')
##R = 'P1(x1,x2,x3)&P1(x1,x2,x6)&P1(x2,x4,x6)&P1(x3,x2,x1)&P1(x2,x1,x4)'
##先将字符串R用符号&分开。\
##在分开后的结果中找同时包含元组 arg2_R中两个元素的部分
##output
##['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)']

def get_lits_2arg(R, arg2_R):
    # 用符号&分开字符串R
##    R_list = R.split('&')

    # 找出同时包含元组arg2_R中两个元素的部分
    lits_2arg = [item for item in R if all(arg in item for arg in arg2_R)]
##    print(lits_2arg)
    return lits_2arg


##input -
##queue_R = ['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'] 
##arg2_R = ('x1', 'x2')
##计算元组arg2_R中两个元素'x1', 'x2' 在列表queue_R中每个元素中的下标。\
##下标按照以下方式计算，把每个字符串中圆括号中的内容用逗号隔开，得列表，\
##取元素在列表中的下标即可。
##output - idx_r = [[0, 1], [0, 1], [2, 1], [1, 0]] 
def idx(arg2_R,queue_R):
    result = []
    for item in queue_R:
        elements_in_parentheses = item.split('(')[1].split(')')[0].split(',')
        indices = [elements_in_parentheses.index(arg) for arg in arg2_R]
        result.append(indices)
##    print(result)
    return result


##input - 
##idx_r = [[0, 1], [0, 1], [2, 1], [1, 0]]
##计算列表重复次数最多的元素即其个数，并输出重复元素的下标。
##output -  ([(0, 1)], [0, 1])
##output -  重复次数最多的元素: (0, 1),  下标： [0, 1]

def get_rep_ele_idx(idx_r):
    # 将嵌套列表转换为元组以进行计数
    idx_r_tuples = [tuple(sublist) for sublist in idx_r]
    print('idx_r_tuples = ', idx_r_tuples)

    # 使用Counter函数计算重复元素的个数
    counter = Counter(idx_r_tuples)
    print('counter =' ,counter)

    ##print(counter.most_common(1)[0][1])
    # 选出重复次数最多的元素及其个数， 个数 = counter.most_common(1)[0][1]
    repeated_elements = [key for key, value in counter.items() \
                         if value == counter.most_common(1)[0][1]]
    print('repeated_elements = ',repeated_elements)
##    repeated_elements.sort()
##    print('repeated_elements = ',repeated_elements)
    

    # 输出重复元素的所有下标
    repeated_indices = [i for i, element in enumerate(idx_r_tuples) if element in repeated_elements]

    print('repeated_elements, repeated_indices = ', repeated_elements, repeated_indices)
    return repeated_elements, repeated_indices


##input -
##arg2_R = ('x1', 'x2') 
##queue_R = ['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'] 
##arg2_F = ('b1', 'b3') 
##queue_F = ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b3,b2,b1)', 'P1(b1,b3,b2)']
##获取对列
##output  - (['P1(x1,x2,x3)', 'P1(x1,x2,x6)'], ['P1(b1,b3,b5)', 'P1(b1,b3,b2)'])
##output  - q_r = ['P1(x1,x2,x3)', 'P1(x1,x2,x6)'], q_f = ['P1(b1,b3,b5)', 'P1(b1,b3,b2)']

def get_queues(arg2_R,queue_R,arg2_F,queue_F):

##1.找下标
    idx_r = idx(arg2_R,queue_R)
    idx_f = idx(arg2_F,queue_F)
##    print('idx_r = {} \nidx_f = {}'.format(idx_r, idx_f))

##2.找重复元素，即下标相同的    
    repele_r, repidx_r = get_rep_ele_idx(idx_r)
    repele_f, repidx_f = get_rep_ele_idx(idx_f)
    print('repele_r = {} \trepidx_r = {} \nrepele_f = {} \trepidx_f = {}'.\
          format(repele_r, repidx_r ,repele_f, repidx_f ))
    ##repele_r = [(0, 1)] 	repidx_r = [0, 1] 
    ##repele_f = [(0, 1)] 	repidx_f = [1, 3]

##3.得队列     有问题 需要改
    q_r = []
    q_f = []  
    if repele_r == repele_f:
        for rqd_r in repidx_r :
            q_r.append(queue_R[rqd_r])
        for rqd_f in repidx_f:
            q_f.append(queue_F[rqd_f])
                    
##    print(q_r, q_f )
    return q_r, q_f




def main():

    lits_R = [[0, 'x1', 1, 'x2', 'P1(x1,x2,x3)'], [0, 'x1', 1, 'x2', 'P1(x1,x2,x6)'], [0, 'x2', 1, 'x1', 'P1(x2,x1,x4)'], [0, 'x2', 1, 'x4', 'P1(x2,x4,x6)'], [0, 'x3', 1, 'x2', 'P1(x3,x2,x1)'], [0, 'x1', 2, 'x3', 'P1(x1,x2,x3)'], [0, 'x1', 2, 'x6', 'P1(x1,x2,x6)'], [0, 'x2', 2, 'x4', 'P1(x2,x1,x4)'], [0, 'x2', 2, 'x6', 'P1(x2,x4,x6)'], [0, 'x3', 2, 'x1', 'P1(x3,x2,x1)'], [1, 'x1', 2, 'x4', 'P1(x2,x1,x4)'], [1, 'x2', 2, 'x1', 'P1(x3,x2,x1)'], [1, 'x2', 2, 'x3', 'P1(x1,x2,x3)'], [1, 'x2', 2, 'x6', 'P1(x1,x2,x6)'], [1, 'x4', 2, 'x6', 'P1(x2,x4,x6)']]
    R = 'P1(x1,x2,x3)&P1(x1,x2,x6)&P1(x2,x4,x6)&P1(x3,x2,x1)&P1(x2,x1,x4)'

    lits_F = [[0, 'b1', 1, 'b2', 'P1(b1,b2,b3)'], [0, 'b1', 1, 'b3', 'P1(b1,b3,b5)'], [0, 'b1', 1, 'b3', 'P1(b1,b3,b2)'], [0, 'b2', 1, 'b4', 'P1(b2,b4,b6)'], [0, 'b3', 1, 'b2', 'P1(b3,b2,b1)'], [0, 'b4', 1, 'b5', 'P1(b4,b5,b6)'], [0, 'b1', 2, 'b2', 'P1(b1,b3,b2)'], [0, 'b1', 2, 'b3', 'P1(b1,b2,b3)'], [0, 'b1', 2, 'b5', 'P1(b1,b3,b5)'], [0, 'b2', 2, 'b6', 'P1(b2,b4,b6)'], [0, 'b3', 2, 'b1', 'P1(b3,b2,b1)'], [0, 'b4', 2, 'b6', 'P1(b4,b5,b6)'], [1, 'b2', 2, 'b1', 'P1(b3,b2,b1)'], [1, 'b2', 2, 'b3', 'P1(b1,b2,b3)'], [1, 'b3', 2, 'b2', 'P1(b1,b3,b2)'], [1, 'b3', 2, 'b5', 'P1(b1,b3,b5)'], [1, 'b4', 2, 'b6', 'P1(b2,b4,b6)'], [1, 'b5', 2, 'b6', 'P1(b4,b5,b6)']]
    F = 'P1(b1,b2,b3)&P1(b1,b3,b5)&P1(b2,b4,b6)&P1(b3,b2,b1)&P1(b4,b5,b6)&P1(b1,b3,b2)'
    
##    arg2_R  = get2args(lits_R)
####出现次数最多的元素:"    
##    arg2_F  = get2args(lits_F)
##    print("arg2_R = {} \targ2_F = {}".format(arg2_R,arg2_F))
##    
##    lits_2arg_R = get_lits_2arg(R.split('&'), arg2_R)       
##    lits_2arg_F = get_lits_2arg(F.split('&'), arg2_F)
##    print('lits_2arg_R = {} \nlits_2arg_F = {}'.format(lits_2arg_R, lits_2arg_F))
##
##    queue_R, queue_F = get_queues(arg2_R,lits_2arg_R, arg2_F, lits_2arg_F)
##    print('queue_R = {} \nqueue_F  = {}'.format(queue_R, queue_F ))


    queue_R = [[lits_R[0][4]]]
    queue_F = []
    queue_RF = []
    print('queue_R = {} '.format(queue_R))
    for i in range(1,len(lits_R)):
##        print(lits_R[i])
        if lits_R[i][0] == lits_R[0][0] and  lits_R[i][2] == lits_R[0][2]:
            if lits_R[i][1] ==   lits_R[0][1] and lits_R[i][3] ==lits_R[0][3]:
##            print(lits_R[i])
                queue_R[0].append(lits_R[i][4])
                print('queue_R = {} '.format(queue_R))
            else:
                break

        
    for j in range(len(lits_F)):
        print('\nj = ', j)
        print( ' lits_R[0][0] ,lits_R[0][2]  = ',lits_R[0][0] ,lits_R[0][2])
        if lits_F[j][0] == lits_R[0][0] and  lits_F[j][2] == lits_R[0][2]:## \
##               and  lits_F[j][1] ==   lits_R[0][1] and lits_F[j][3] ==lits_R[0][3]:
            print(lits_F[j][4])
##                queue_F[0].append(lits_F[j][4])
##                print('queue_F = {} '.format(queue_F))
        else:
            break

    
    
    
    
if __name__ == '__main__':    
    main()
