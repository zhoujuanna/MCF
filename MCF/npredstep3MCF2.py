##def check_dict(d1, d2):
##    return all((k in d2 and v == d2[k]) for k, v in d1.items())

##以下是测试函数check_dict的数据  共12组
##count =  1
##e0d =  {'x3': 'b5', 'x5': 'b9', 'x6': 'b4'} 
##e1d =  {'x2': 'b6', 'x4': 'b7', 'x6': 'b4', 'x9': 'b1'}
##
##count =  2
##e0d =  {'x3': 'b9', 'x5': 'b4', 'x6': 'b2'} 
##e1d =  {'x2': 'b6', 'x4': 'b7', 'x6': 'b4', 'x9': 'b1'}
##
##count =  3
##e0d =  {'x3': 'b5', 'x5': 'b9', 'x6': 'b4'} 
##e1d =  {'x1': 'b3', 'x2': 'b1', 'x4': 'b5', 'x6': 'b6', 'x7': 'b8'}
##
##count =  4
##e0d =  {'x3': 'b9', 'x5': 'b4', 'x6': 'b2'} 
##e1d =  {'x1': 'b3', 'x2': 'b1', 'x4': 'b5', 'x6': 'b6', 'x7': 'b8'}
##
##count =  5
##e0d =  {'x3': 'b9', 'x5': 'b4', 'x6': 'b5'} 
##e1d =  {'x2': 'b6', 'x4': 'b7', 'x6': 'b4', 'x9': 'b1'}
##
##count =  6
##e0d =  {'x3': 'b4', 'x5': 'b2', 'x6': 'b9'} 
##e1d =  {'x2': 'b6', 'x4': 'b7', 'x6': 'b4', 'x9': 'b1'}
##
##count =  7
##e0d =  {'x3': 'b9', 'x5': 'b4', 'x6': 'b5'} 
##e1d =  {'x1': 'b3', 'x2': 'b1', 'x4': 'b5', 'x6': 'b6', 'x7': 'b8'}
##
##count =  8
##e0d =  {'x3': 'b4', 'x5': 'b2', 'x6': 'b9'} 
##e1d =  {'x1': 'b3', 'x2': 'b1', 'x4': 'b5', 'x6': 'b6', 'x7': 'b8'}
##
##count =  9
##e0d =  {'x3': 'b4', 'x5': 'b5', 'x6': 'b9'} 
##e1d =  {'x2': 'b6', 'x4': 'b7', 'x6': 'b4', 'x9': 'b1'}
##
##count =  10  没有冲突
##e0d =  {'x3': 'b2', 'x5': 'b9', 'x6': 'b4'} 
##e1d =  {'x2': 'b6', 'x4': 'b7', 'x6': 'b4', 'x9': 'b1'}
##output -  lambda_ed =  {'x3': 'b2', 'x5': 'b9', 'x6': 'b4', 'x2': 'b6', 'x4': 'b7', 'x9': 'b1'}
##

##count =  11  有冲突
##e0d =  {'x3': 'b4', 'x5': 'b5', 'x6': 'b9'} 
##e1d =  {'x1': 'b3', 'x2': 'b1', 'x4': 'b5', 'x6': 'b6', 'x7': 'b8'}
##output -
##Conflict: 	kvin1d_e1d =  {'x4': 'b5', 'x6': 'b6'} 
##	confl_e0d =  {'x5': 'b5', 'x6': 'b9'}
##lambda_ed =  {}

##count =  12
##e0d =  {'x3': 'b2', 'x5': 'b9', 'x6': 'b4'} 
##e1d =  {'x1': 'b3', 'x2': 'b1', 'x4': 'b5', 'x6': 'b6', 'x7': 'b8'}


##判断两个合一子e0d, e1d（类型：字典）的冲突性，
##如果有冲突，返回False+有冲突的键值对+空字典，\
##如果没有冲突，返回True + 合并后的合一子。

def check_dict(e0d, e1d):
##    print('e0d = {} \ne1d = {}'.format(e0d, e1d))
    ed = {}

    for k, v in e1d.items():
##        不冲突
        if (k in e0d and e0d[k] == v) or (k not in e0d and v not in e0d.values()):
            ed[k] = v

    if ed:
##        print('\nafter check ed = ', ed)
        if len(ed) == len(e1d):
            ed = {**e0d, **e1d}  ##合并两字典
##            print('lambda = ', ed)
            return True, ed
        else:   ##len(ed) < len(e1d):  有冲突
##            输出这两个字典e1d, ed中只出现在一个字典中的键值对。
            kvin1d_e1d = {k: e1d[k] for k in e1d if k not in ed}   ##kvin1d  kv in 1 dict
            kvin1d_e1d.update({k: ed[k] for k in ed if k not in e1d})
            confl_e0d = {k: v for k, v in e0d.items() if k in kvin1d_e1d or v in kvin1d_e1d.values()}
##            print('Conflict: \tkvin1d_e1d = ', kvin1d_e1d, '\n\tconfl_e0d = ', confl_e0d)
            return False, {}
    else:
##        print('N')
        return False, {}


def unionRp12(R_isom, R_isom1):
    count = 1
    R_isomP12 = []
    for e0 in R_isom:
##        print('\n\n\ne0 = ', e0)
        for e1 in R_isom1:
##            print('\ne1 = ', e1)
            for e0d in e0[2]:
##                print('e0d = ', e0d)
                for e1d in e1[2]:
##                    print('\ncount = ', count)
                    count += 1
##                    print('e0d = ', e0d, '\ne1d = ', e1d)
                    if check_dict(e0d, e1d)[0]:
##                        print(check_dict(e0d, e1d)[1])
##                        print('\ne0d = {} is subset of e1d = {} '.format(e0d, e1d))
##                        print('e0[1] = {}  \tlen(e0[1]) = {} \ne1[1] = {} \
##                        \tlen(e1[1]) = {}'.format(e0[1], len(e0[1]), e1[1], len(e1[1])))
                        union_literal = e0[1] + e1[1]  
##                        print('union_literal = {} \tlen(union_literal) = {}'.\
##                              format( union_literal, len(union_literal)))
                        e2 = [len(union_literal), union_literal, [check_dict(e0d, e1d)[1]]]
##                        print('e2 = ', e2)
                        R_isomP12.append(e2)
##                        print('\nR_isomP12 = {} \tlen(R_isomP12) = {}'.\
##                              format(R_isomP12, len(R_isomP12)))

##合一子排序
    for i in range(len(R_isomP12)):
##        print('R_isom_12[{}] = {}'.format(i, R_isom_12[i][2]))
        for j in range(len(R_isomP12[i][2])):
##            print(len(R_isom_12[i][2]))
            R_isomP12[i][2][j] = dict(sorted(R_isomP12[i][2][j].items()))

    return R_isomP12


def main():

##    R_isom_g =  [
##        [[2, ['P1(x1,x2,x3,x4)', 'P1(x2,x3,x1,x4)'], [{'x1': 'b1', 'x2': 'b2', 'x3': 'b3', 'x4': 'b4'}]]], \
##        [[2, ['P2(x1,x2,x3,x4)', 'P2(x2,x3,x1,x4)'], [{'x1': 'b1', 'x2': 'b2', 'x3': 'b3', 'x4': 'b4'}]]]\
##        ]

    R_isom_g =  [\
        [[2, ['P2(x3,x5)', 'P2(x5,x6)'], [{'x3': 'b5', 'x5': 'b9', 'x6': 'b4'}, {'x3': 'b9', 'x5': 'b4', 'x6': 'b2'}]], \
         [2, ['P2(x3,x5)', 'P2(x6,x3)'], [{'x3': 'b9', 'x5': 'b4', 'x6': 'b5'}, {'x3': 'b4', 'x5': 'b2', 'x6': 'b9'}]], \
         [2, ['P2(x5,x6)', 'P2(x6,x3)'], [{'x3': 'b4', 'x5': 'b5', 'x6': 'b9'}, {'x3': 'b2', 'x5': 'b9', 'x6': 'b4'}]]], \
        [[2, ['P3(x2,x4,x9)', 'P3(x2,x6,x4)'], [{'x2': 'b6', 'x4': 'b7', 'x6': 'b4', 'x9': 'b1'}]], \
         [2, ['P3(x2,x6,x4)', 'P3(x7,x4,x1)'], [{'x1': 'b3', 'x2': 'b1', 'x4': 'b5', 'x6': 'b6', 'x7': 'b8'}]]], \
        [[2, ['P4(x2,x7,x3,x5)', 'P4(x6,x3,x9,x4)'], \
          [{'x2': 'b6', 'x3': 'b5', 'x4': 'b7', 'x5': 'b9', 'x6': 'b4', 'x7': 'b8', 'x9': 'b1'}]], \
         [2, ['P4(x2,x7,x3,x5)', 'P4(x3,x5,x9,x2)'], [{'x2': 'b6', 'x3': 'b5', 'x5': 'b9', 'x7': 'b8', 'x9': 'b2'}]]]\
        ]


    R_isom = R_isom_g[0]
    R_isom1 = R_isom_g[1]
    print('R_isom = {} \nR_isom1 = {}'.format(R_isom, R_isom1))
    t = unionRp12(R_isom, R_isom1)
    print('\nt = ', t)

if __name__ == '__main__':    
    main()
    
