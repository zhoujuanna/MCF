import copy
from collections import defaultdict

##---------------

# 获取参数在元素中的下标
def get_indices(s):
    s_backup = copy.deepcopy(s)
##    print('s = ', s)
    indices = {}
    s = s[s.find("(")+1:s.find(")")]
    params = s.split(",")
    
    for i in range(len(params)):
        for j in range(i+1, len(params)):
            indices[(i, j)] = {(params[i], params[j]):[s_backup]}
    indices = [(key, value) for key, value in indices.items()]
    return indices

##---------------

def get_union(result_R):
    updated_result_R = {}

    for item in result_R:
        key = item[0]
        value = item[1]
        if key in updated_result_R:
            for k, v in value.items():
                if k in updated_result_R[key]:
                    updated_result_R[key][k].extend(v)
                else:
                    updated_result_R[key][k] = v
        else:
            updated_result_R[key] = value
##    updated_result_R = [(key, value) for key, value in updated_result_R.items()]
    
    return updated_result_R

##---------------

def get_idx_arg(R):
    result_R = []
    for elem in R:    
        indices = get_indices(elem)
        result_R.extend(indices)
    return result_R

##---------------

def dict_to_list(litsF):    
    res = []
    ##转格式 
    for key, value in litsF.items():
    ##    print('\n\nkey = ', key,'\n', 'value = ', value)
        for k , v in value.items():
    ##        print('\nk = ', k, '\n', 'v = ', v)
    ##        print([key,{k:v}])
            res.append([key,{k:v}])
##    print('\n\nres = ', res)
    return res

##---------------

    # 分组
##    把列表litsR按照以下方式分组： 如果元素e1和元素e2的第2个元素的长度相等，、
##    并且第1个元素相等，那么把元素e1和e2分为一组。
##    output -r =  [[[(0, 1), {('x1', 'x2'): ['P1(x1,x2,x3)', 'P1(x1,x2,x6)']}]], [[(0, 1), {('x2', 'x4'): ['P1(x2,x4,x6)']}], [(0, 1), {('x3', 'x2'): ['P1(x3,x2,x1)']}], [(0, 1), {('x2', 'x1'): ['P1(x2,x1,x4)']}]], [[(0, 2), {('x1', 'x3'): ['P1(x1,x2,x3)']}], [(0, 2), {('x1', 'x6'): ['P1(x1,x2,x6)']}], [(0, 2), {('x2', 'x6'): ['P1(x2,x4,x6)']}], [(0, 2), {('x3', 'x1'): ['P1(x3,x2,x1)']}], [(0, 2), {('x2', 'x4'): ['P1(x2,x1,x4)']}]], [[(1, 2), {('x2', 'x3'): ['P1(x1,x2,x3)']}], [(1, 2), {('x2', 'x6'): ['P1(x1,x2,x6)']}], [(1, 2), {('x4', 'x6'): ['P1(x2,x4,x6)']}], [(1, 2), {('x2', 'x1'): ['P1(x3,x2,x1)']}], [(1, 2), {('x1', 'x4'): ['P1(x2,x1,x4)']}]]]
def group(litsR):
    grouped_litsR = {}
    for item in litsR:
    ##    print('\n\nitem = ', item)
    ##    print('list(item[1].values())[0] = ', list(item[1].values())[0])
    ##    print('len(list(item[1].values())[0]) = ', len(list(item[1].values())[0]))
       
        key = (len(list(item[1].values())[0]), item[0])
##        print('key = ', key)
        grouped_litsR.setdefault(key, []).append(item)
##        print('grouped_litsR = ', grouped_litsR)

    grouped_litsR = list(grouped_litsR.values())

##    print("分组后的列表：", grouped_litsR)
    return grouped_litsR

##-------------------

##input -
##litsR =  [[[(0, 1), {('x1', 'x2'): ['P1(x1,x2,x3)', 'P1(x1,x2,x6)']}]], [[(0, 1), {('x2', 'x4'): ['P1(x2,x4,x6)']}], [(0, 1), {('x3', 'x2'): ['P1(x3,x2,x1)']}], [(0, 1), {('x2', 'x1'): ['P1(x2,x1,x4)']}]], [[(0, 2), {('x1', 'x3'): ['P1(x1,x2,x3)']}], [(0, 2), {('x1', 'x6'): ['P1(x1,x2,x6)']}], [(0, 2), {('x2', 'x6'): ['P1(x2,x4,x6)']}], [(0, 2), {('x3', 'x1'): ['P1(x3,x2,x1)']}], [(0, 2), {('x2', 'x4'): ['P1(x2,x1,x4)']}]], [[(1, 2), {('x2', 'x3'): ['P1(x1,x2,x3)']}], [(1, 2), {('x2', 'x6'): ['P1(x1,x2,x6)']}], [(1, 2), {('x4', 'x6'): ['P1(x2,x4,x6)']}], [(1, 2), {('x2', 'x1'): ['P1(x3,x2,x1)']}], [(1, 2), {('x1', 'x4'): ['P1(x2,x1,x4)']}]]]
##转格式
##output - [[(0, 1), ['P1(x1,x2,x3)', 'P1(x1,x2,x6)']], [(0, 1), ['P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)']], [(0, 2), ['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)']], [(1, 2), ['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)']]]

def idx_comma_lits(litsR):
    # 对列表litsR进行处理
    for i in range(len(litsR)):
    ##    print('\nlitsR[i] = ', litsR[i])
        if len(litsR[i]) == 1:
            key = litsR[i][0][0]
            value = list(litsR[i][0][1].values())[0]
##            print('value = ', value)          
            litsR[i] = [key,value]
        else:
            key = litsR[i][0][0]
    ##        print('\nkey = ', key)
            vls = []
            value_list = [list(item[1].values())[0] for item in litsR[i]]
##            print('value_list = ', value_list)
##            print('len(value_list) = ', len(value_list))
            if len(value_list) > 1:
                for vl in value_list:
##                    print('vl = ', vl)
                    vls.extend(vl)
##                    print('vls = ', vls)
            litsR[i] = [key, vls]
    ##        print('litsR[i]  = ', litsR[i] )

    ##for lr in litsR:
    ##    print('\n', lr)
##    print(" litsR = ", litsR)
    return litsR

##---------------

##input - 
##litsR =  [[(0, 1), ['P1(x1,x2,x3)', 'P1(x1,x2,x6)']], [(0, 1), ['P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)']], [(0, 2), ['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)']], [(1, 2), ['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)']]] 
##litsF =  [[(0, 1), ['P1(b1,b3,b5)', 'P1(b1,b3,b2)']], [(0, 1), ['P1(b1,b2,b3)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)']], [(0, 2), ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)']], [(1, 2), ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)']]]
##如果litsR中第1个元素er1的第1个元素等于litsF中第1个元素ef1的第1个元素，\
##那么queueR = er1的第2个元素，queueF = ef1的第2个元素，输出queueR，queueF。\
##从litsR中删除第1个元素er1，从litsF中删除第1个元素ef1。\
##继续重复，如果litsR中第1个元素er1的第1个元素不等于litsF中第1个元素ef1的第1个元素，\
##那么判断litsR中第1个元素是否等于litsF中第2个元素ef2的第1个元素，\
##如果相等，那么queueR = er1的第2个元素，queueF = ef2的第2个元素，输出queueR，queueF。\
##从litsR中删除第1个元素er1，从litsF中删除第2个元素ef2。这样继续， \
##直到litsR为空，或者litsR中元素er的第一个元素不等于litsF中任意一个元素的第1个元素。
##output - [(['P1(x1,x2,x3)', 'P1(x1,x2,x6)'], ['P1(b1,b3,b5)', 'P1(b1,b3,b2)']), (['P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'], ['P1(b1,b2,b3)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)']), (['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'], ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)']), (['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'], ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)'])]
def get_queues(litsR, litsF):    
    result = []
    while litsR and litsF:
##        print('\nlitsR = {} \nlitsF = {}'.format(litsR, litsF))
        er1 = litsR[0][0]
        ef1 = litsF[0][0]
        
        if er1[0] == ef1[0]:            
            queueR = litsR[0][1]
            queueF = litsF[0][1]
            result.append((queueR, queueF, er1))
            litsR.pop(0)
            litsF.pop(0)
        else:
            match_found = False
            for ef2 in litsF[0][1:]:
                if er1[0] == ef2[0]:
                    queueR = litsR[0][1]
                    queueF = ef2[1]
                    result.append((queueR, queueF, er1))
                    litsR.pop(0)
                    litsF[0] = (ef1, [item for item in litsF[0][1:] if item != ef2])
                    match_found = True
                    break
            if not match_found:
                litsR.pop(0)
    return result

##---------------


##input - pps =  [(['P1(x1,x2,x3)', 'P1(x1,x2,x6)'], ['P1(b1,b3,b5)', 'P1(b1,b3,b2)'], (0, 1)), (['P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'], ['P1(b1,b2,b3)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)'], (0, 1)), \
##(['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'], ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)'], (0, 2)), \
##(['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'], ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)'], (1, 2))]
##len(pps) = 4
##如果列表pps中的元素e1与元素e2的前两个元素排序后相等，\
##那么从pps中删除元素e2，只保留元素e1。
##output - pps = [(['P1(x1,x2,x3)', 'P1(x1,x2,x6)'], ['P1(b1,b3,b5)', 'P1(b1,b3,b2)'], (0, 1)), (['P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'], ['P1(b1,b2,b3)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)'], (0, 1)), \
##(['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)'], ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)'], (0, 2))] 	\
##len(pps) = 3

def remove_duplicates(pps):
    seen = set()
    result = []
    for e1, e2, _ in pps:
        sorted_e1 = tuple(sorted(e1))
        if sorted_e1 not in seen:
            seen.add(sorted_e1)
            result.append((e1, e2, _))
    return result


##---------------    
    
def  prep_queue(F):
    litsF = get_union(get_idx_arg(F))
##    print("\nlitsF = ", litsF)
    litsF = dict_to_list(litsF)
    litsF = sorted(litsF, key=lambda x: (-len(list(x[1].values())[0]), x[0]))
##    print("\nlitsF = ", litsF)
    litsF = group(litsF)   
    litsF = idx_comma_lits(litsF)
    return litsF

##---------------

def queues(R, F):

    if len(R) <=5 and len(F) <= 5:
        pps = [(R, F, (0,1))]
##        print('pps = ', pps)
            
    else:
        litsR = prep_queue(R)
        litsF = prep_queue(F)
    
##    print("\nlitsR = ", litsR, "\n\nlitsF = ", litsF)    

##    for lr in litsR:                    
##        print(lr,'\n')
##    print("\n\n\n")
##    for lf in litsF:
##        print(lf, '\n')
   
        pps = get_queues(litsR, litsF)
##        print('\npps = ', pps)
##    print('\nlen(pps)= ', len(pps))
##    count = 1
##    for pp in pps:                    
####        print('\n', pp)##, '\t', len(pp[0]), len(pp[1]))
####        print('\nR_isom{}'.format(count) )
##        count = count + 1
##        print('queue_R = {} \nqueue_F = {}'.format(pp[0], pp[1]))

    return pps


##---------------

def main():
    ##input - 
    # R 列表
##    R = ['P1(x1,x2,x3)', 'P1(x1,x2,x6)', 'P1(x2,x4,x6)', 'P1(x3,x2,x1)', 'P1(x2,x1,x4)']
##    F =  ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)']
    
    R = 'P2(a1,a2,a3,a4)&P2(a2,a3,a1,a4)'
    F = 'P2(b1,b2,b3,b4)&P2(b2,b3,b1,b4)&P2(b1,b2,b2,b3)'
    
##a
##    F =  'P1(a1,a3,a2)&P1(a2,a1,a5)&P1(a2,a5,a8)&P1(a2,a1,a8)&P1(a3,a4,a1)&\
##P1(a3,a5,a1)&P1(a3,a9,a4)&P1(a3,a9,a5)&P1(a3,a9,a1)&P1(a4,a3,a6)&\
##P1(a4,a6,a5)&P1(a5,a2,a3)&P1(a5,a2,a4)&P1(a5,a3,a7)&P1(a5,a3,a10)&\
##P1(a5,a4,a7)&P1(a5,a4,a10)&P1(a5,a7,a2)&P1(a5,a10,a2)&P1(a6,a4,a9)&\
##P1(a6,a7,a4)&P1(a6,a9,a7)&P1(a7,a5,a6)&P1(a7,a6,a10)&P1(a8,a2,a10)&\
##P1(a9,a6,a3)&P1(a9,a10,a6)&P1(a9,a10,a3)&P1(a10,a7,a9)&P1(a10,a5,a9)&\
##P1(a10,a8,a7)&P1(a10,a8,a5)&P1(a10,a8,a9)'
##    
##b
##    R =  'P1(a1,a4,a2)&P1(a2,a1,a6)&P1(a2,a6,a3)&P1(a2,a1,a3)&P1(a3,a2,a8)&\
##P1(a4,a5,a1)&P1(a4,a6,a1)&P1(a4,a7,a5)&P1(a4,a7,a6)&P1(a4,a7,a1)&\
##P1(a5,a4,a7)&P1(a5,a7,a6)&P1(a6,a2,a5)&P1(a6,a2,a4)&P1(a6,a5,a8)&\
##P1(a6,a4,a8)&P1(a6,a8,a2)&P1(a7,a5,a4)&P1(a7,a8,a5)&P1(a7,a8,a4)&\
##P1(a8,a3,a6)&P1(a8,a6,a7)&P1(a8,a3,a7)'
##  
    R = R.replace('a', 'x')
    R = R.split('&')
    F = F.split('&')
    
##d 
##    F = 'P1(a1,a3,a2)&P1(a2,a1,a6)&P1(a3,a4,a1)&P1(a3,a5,a1)&P1(a3,a6,a1)&\
##P1(a3,a9,a4)&P1(a3,a9,a5)&P1(a3,a9,a6)&P1(a3,a9,a1)&P1(a4,a3,a7)&\
##P1(a4,a7,a5)&P1(a4,a7,a6)&P1(a5,a4,a8)&P1(a5,a3,a8)&P1(a5,a8,a6)&\
##P1(a6,a2,a5)&P1(a6,a2,a4)&P1(a6,a2,a3)&P1(a6,a5,a10)&P1(a6,a4,a10)&\
##P1(a6,a3,a10)&P1(a6,a2,a10)&P1(a7,a4,a9)&P1(a7,a8,a4)&P1(a7,a9,a8)&\
##P1(a8,a5,a7)&P1(a8,a7,a10)&P1(a8,a10,a5)&P1(a9,a7,a3)&P1(a9,a10,a3)&\
##P1(a9,a10,a7)&P1(a10,a6,a8)&P1(a10,a8,a9)&P1(a10,a6,a9)'
##  
##    R = R.replace('a', 'x')
##    R = R.split('&')
##    F = F.split('&')
    
    pps = queues(R, F)

##    print('pps = ', pps)



##--------------

if __name__ == '__main__':    
    main()
