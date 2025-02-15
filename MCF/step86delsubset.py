import npt83
import copy


##1start  -----------
##有一个按照从大到小排好序的列表 R_length = [19，11，7，7，2], 、
##有一个整数R_isom0 = 7, 在列表R_length 中找到与整数R_isom0相等的元素的个数。

def count_equal_elements(arr, target):
    left, right = 0, len(arr) - 1
    first_position = find_first_occurrence(arr, target, left, right)
    last_position = find_last_occurrence(arr, target, left, right)
    if first_position != -1 and last_position != -1:
        return last_position - first_position + 1
    else:
        return 0

def find_first_occurrence(arr, target, left, right):
    first = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return first

def find_last_occurrence(arr, target, left, right):
    last = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return last

##1end -----------




##-------------

##有一个按照从大到小排好序的列表 R_length = [19，11，7，7，2], \
##有一个整数R_isom0 = 7, 把整数R_isom0插入到列表R_length的比该整数小的整数前，\
##换句话说，把R_isom0插入到元素2前。输出列表R_length以及R_isom0在列表R_length中的下标。
##插入后的列表R_length: [19, 11, 7, 7, 7, 2]
##R_isom0在列表R_length中的下标: 4

def insert_sorted_list(arr, target):
    left = 0
    right = len(arr)

    while left < right:
##        print('\nleft = ', left)
##        print('right = ', right)
        
        mid = (left + right) // 2
##        print('mid = ',mid, 'arr[mid] = ', arr[mid])
        
        if arr[mid] < target:
##            print('arr[mid] < target')
            right = mid
##            print('right = ', right)
        else:
            left = mid + 1
##            print('left = ', left)

##    arr.insert(left, target)
    return left
##用法: index = insert_sorted_list(R_length, R_isom0)


##------------------------

##从列表R_isom的下标idx_cmpstart开始， 到 len(R_isom)结束，\
##找R_isom中的元素是否为e_rp的子集，如果是，删除R_isom的这个元素
##e_rp = R_isom_p[1]
def rm(idx_cmpstart, R_isom, e_rp):
    to_remove = []
    for j in range(idx_cmpstart, len(R_isom)):   
        e_r = set(R_isom[j][1])
        if e_r.issubset(e_rp):
            to_remove.append(j)
##        print('to_remove = ', to_remove)
    to_remove = list(set(to_remove))  # Remove duplicate indices
##        print('to_remove = ', to_remove)
    to_remove.sort(reverse=True)  # Sort in reverse order to avoid index issues
##        print('to_remove = ', to_remove)        
    for index in to_remove:
        del R_isom[index]
    return R_isom


##----------------

##从列表R_isom的下标0开始， 到 idx_cmpend结束，\
##找R_isom的元素是否为R_isom_max元素的子集，\
##如果是，把R_isom_max元素的下标记录在列表to_remove2中。

def get_idx_del(idx_cmpend, R_isom_p, R_isom):
    to_remove2 = []##这个列表只记录下标，并没有真正从R_isom中删除元素。
    e_rp = set(R_isom_p[1])
      ##            print('idx = ', idx)
    for j in range(0, idx_cmpend):##idx_cmpend= len(R_isom)
      ##                print('j = ', j)
        e_r = set(R_isom[j][1])
        if e_rp.issubset(e_r):
            to_remove2.append(j)
    return to_remove2

##-------------------
##input - 
##R_isom_plist =  [3, ['P1(x2,x4,x6)', 'P1(x1,x2,x3)', 'P1(x3,x2,x1)'], \
##                 [{'x1': 'b3', 'x3': 'b1', 'x2': 'b2', 'x4': 'b4', 'x6': 'b6'}]]
##R_isom =  [[3, ['P1(x1,x2,x3)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)'], \
##            [{'x3': 'b3', 'x1': 'b1', 'x2': 'b2', 'x4': 'b4', 'x6': 'b6'}, \
##             {'x1': 'b3', 'x3': 'b1', 'x2': 'b2', 'x4': 'b4', 'x6': 'b6'}]]]
##判断列表R_isom_plist 的第3个元素中的第1个元素字典p是否等于\
##嵌套列表R_isom的第1个元素的第3个元素中的某个元素\
##或者被包含在嵌套列表R_isom的第1个元素的第3个元素中，\
##如果是，输出True，否则，输出False
##output - True
##def check_isomorphism(R_isom_plist, R_isom):
def check_isomorphism(p, q_list):
##    p = R_isom_plist[2][0]
####    print('p = ', p)
##    q_list = R_isom[0][2]
##    print('q_list = ', q_list)    
    
    for q in q_list:
        if all(item in q.items() for item in p.items()):
            return True
    return False

##----------------

##比较两个字符串列表list1, list2的每个字符，\
##如果相等，输出True;  否则，输出False

def compare_lists(list1, list2):
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False  # If any elements are different, the lists are not equal
    
    return True  # If no differences are found, the lists are equal


##----------------

def getmaxRisom(R_isom, R_isom_p):
##    print('R_isom = {} \nR_isom = {}'.format(R_isom, R_isom_p))
    
    if len(R_isom) == 0:
        return []

    else:##len(R_isom) > 0:
        print('@@@@R_isom = {}'.format(R_isom))


        R_length = [e[0] for e in R_isom]
    ##    print('!!!!!R_length = ', R_length)
    ##    print('R_isom_p = ', R_isom_p)
        
    ##    1. 文字长度大于R_isom中所有元素文字的长度
        if R_isom_p[0] > max(R_length):
            print('\n1. 文字长度大于R_isom中所有元素文字的长度 R_isom_p[0] > max(R_isom_length) ')
            R_isom.insert(0, R_isom_p)
    ##        print('R_isom = ', R_isom)        
            e_rp = set(R_isom[0][1])
            R_isom = rm(1, R_isom, e_rp)
    ##        print(R_isom)
      


    ##    2. 文字长度介于R_isom中所有元素的文字长度之间
        elif  R_isom_p[0] <= max(R_length) and R_isom_p[0] >= min(R_length): 
            print('\n2. 文字长度介于R_isom中所有元素的文字长度之间 min(R_length) <= R_isom_p[0] <= max(R_length) ')
    ##找下标idx, 在列表R_length中比整数R_isom[0]小的整数前的下标\
    ##例：列表R_length: [19, 11, 7, 7, 2]， R_isom_p[0] = 7,那么 idx = 4
    ##        print('R_length = ', R_length)
            idx = insert_sorted_list(R_length, R_isom_p[0])
    ##        print('R_length = ', R_length)
    ##        print('idx = ', idx)
                
    ##        else:         ##R_isom_p[0] not in [e[0] for e in R_isom]:     文字长度不在R_isom中           
    ##R_isom_p 是否为其他长度比自己元素大或等于自己元素的R_isom子集？\
    ##如果不是,把R_isom_p添加到R_isom中。            
            to_remove2 = get_idx_del(idx, R_isom_p, R_isom)
            
    ##            print('\nto_remove2 = ', to_remove2)
            if len(to_remove2) == 0: #and R_isom_p[1].sort() != R_isom[i][1].sort():
                print('文字不同，不是子集， 添加整个R_isom_p')
    ##                print('if len(to_remove2) == 0 ')
                R_isom.insert(idx, R_isom_p)
                print('R_isom = {} \tlen(R_isom) = {} '.format(R_isom, len(R_isom)))
                idx = idx + 1

    ##R_isom_p 是否为其他长度比自己元素小的R_isom子集？如果是,删除R_isom中的小元素。
                R_isom = rm(idx, R_isom, set(R_isom_p[1]))

            else:  ##len(to_remove2) > 0: 是子集
                print('是子集')
    ##            print('R_isom = {} \nR_isom = {}'.format(R_isom, R_isom_p))
    ##          检查第3个元素（合一子）是否相等，如果不相等，只添加合一子。            
    ##            print('idx = ', idx)
    ##            print('R_length = {}  \nR_isom = {}'.format(R_length, R_isom_p))
                
    ##            k - 列表R_isom_max中文字长度等于R_isom[0]的第一个元素的下标
                k = idx - count_equal_elements(R_length, R_isom_p[0])
    ##            print('count_equal_elements(R_length, R_isom_p[0]) = ', count_equal_elements(R_length, R_isom_p[0]))
    ##            print('k = ', k)
                
                R_isom_p[1].sort()            
                while R_isom[k][0] == R_isom_p[0]:
    ##                print('\n\nin while')
                    R_isom[k][1].sort()
    ##                print('\nR_isom[{}][1] = {} \nR_isom_p[1] = {}'.format(k, R_isom[k][1] ,R_isom_p[1]))
    ##                if k < len(R_isom):         
                    if compare_lists(R_isom[k][1], R_isom_p[1]):
                        print('in compare_lists(R_isom[k][1], R_isom_p[1]) - 文字相同')
                        print('R_isom[{}][2] = {} \nR_isom_p[2][0] = {}'.format(k, R_isom[k][2] ,R_isom_p[2][0]))                

##                        if R_isom_p[2][0] in R_isom[k][2]:
##                        tmp = check_isomorphism(R_isom_p[2][0], R_isom[k][2]) 
##                        print('tmp = ',tmp)
                        
                        if check_isomorphism(R_isom_p[2][0], R_isom[k][2]) == False:
##check_isomorphism(R_isom_plist, R_isom)
                            
                            print('文字相同，合一子不同, 只添加合一子。')                        
    ##                        print('\nR_isom[k][2] = {} \tR_isom_p[2]  = {}'.format(R_isom[k][2], R_isom_p[2]))
    ##                        print('R_isom[{}] = {} \nR_isom_p = {}'.format(k, R_isom[k], R_isom_p))
                            R_isom[k][2].extend(R_isom_p[2])
    ##                        print('\nR_isom = {} \tlen(R_isom) = {}'.format(R_isom, len(R_isom)))

                        else:##文字相同，合一子相同，保持原样不变。
                            print('文字相同，合一子相同，保持原样不变。')       
                            pass
                        break
                    k = k + 1
                    if k == len(R_isom):
                        break              



                
                
    ##   3. 文字长度小于R_isom中所有元素文字的长度
        elif R_isom_p[0] < min(R_length):
            print('\n3. 文字长度小于R_isom中所有元素文字的长度  R_isom_p[0] < min(R_length) ')
              ##R_isom_p 是否为其他长度比自己元素大的R_isom子集？\
    ##          如果不是, 把R_isom_p添加到R_isom中。
            to_remove2 = get_idx_del(len(R_isom), R_isom_p, R_isom)               
              ##            print('\nto_remove2 = ', to_remove2)
            if len(to_remove2) == 0:
                print('不是子集，加到R_isom中')
              ##                print('if len(to_remove2) == 0 ')
                R_isom.insert(len(R_isom), R_isom_p)
                print('R_isom = {} \tlen(R_isom) = {} '.format(R_isom, len(R_isom)))
            else:
                print('是子集，不加')
                

    ## 4.如果有其他情况，再加 
        else:
            pass

        return R_isom


    



def main():
    
##R_isom_max的类型是嵌套列表 [[],[],[]...]，\
##R_isom的类型是含有三个元素的列表[长度，公式，合一子]。
    R_isom, R_isom_p = npt83.ind()
    print('inin dada:\nR_isom_max = {} \nR_isom = {}'.format(R_isom, R_isom_p))
        
    if len(R_isom) == 0:
        R_isom.append(copy.deepcopy(R_isom_p))
        print('\nR_isom = ', R_isom)
    else:##len(R_isom) > 0:
        R_isom = getmaxRisom(R_isom, R_isom_p)
        print('\nR_isom = ', R_isom, '\tlen(R_isom) = ', len(R_isom))
    

    
##    print('R_isom = ', R_isom)
##    print('\nR_isom_ps = ', R_isom_ps)
##    if  len(R_isom_ps) > 3: #isinstance() and
##        R_isom_ps.sort(key=lambda x: x[0],  reverse=True)
##    
##    print('\nR_isom_ps = ', R_isom_ps)

  
##    for i in range(len(R_isom_ps)):
##        print('\ni = ', i)
##        R_isom_p = R_isom_ps[i]
##        print('\nR_isom = ', R_isom, '\tlen(R_isom) = ', len(R_isom))
##        print('\nR_isom_p = ', R_isom_p)
##        R_isom = getmaxRisom(R_isom, R_isom_p)
##        print('\nR_isom = ', R_isom, '\tlen(R_isom) = ', len(R_isom))

##        if len(R_isom) == 0:
##            R_isom.extend(copy.deepcopy(R_isom_p))
##            print('\nR_isom = ', R_isom)
##        else:##len(R_isom) > 0:
##            R_isom = getmaxRisom(R_isom, R_isom_p)
##            print('\nR_isom = ', R_isom, '\tlen(R_isom) = ', len(R_isom))        

        

if __name__ == '__main__':    
    main()
    
