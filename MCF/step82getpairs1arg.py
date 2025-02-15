from itertools import product
##input - 
index_arglit_R = [{0: ['P1(a2,x6,x1)'], 1: ['P1(x1,a2,x2)', 'P1(x6,a2,x8)'], 2: ['P1(x6,x2,a2)']}, \
                  {0: [], 1: [], 2: ['P1(x8,x6,a1)', 'P1(x8,x3,a1)']}, \
                  {0: [], 1: ['P1(x6,a5,x8)'], 2: ['P1(x6,x2,a5)']}]
index_arglit_F = [{0: [], 1: ['P1(a8,a2,a10)'], 2: []}, \
                  {0: [], 1: [], 2: ['P1(a3,a4,a1)', 'P1(a3,a9,a1)']}, \
                  {0: ['P1(a5,a3,a7)', 'P1(a5,a3,a10)', 'P1(a5,a4,a7)', 'P1(a5,a4,a10)'], \
                   1: ['P1(a7,a5,a6)', 'P1(a10,a5,a9)'], 2: ['P1(a3,a9,a5)', 'P1(a4,a6,a5)', 'P1(a10,a8,a5)']}]

##rs_zip = list(zip(index_arglit_R, index_arglit_F))
##print('rs_zip  = ', rs_zip )
##rs_zip =  [({0: ['P1(a2,x6,x1)'], 1: ['P1(x1,a2,x2)', 'P1(x6,a2,x8)'], 2: ['P1(x6,x2,a2)']}, {0: [], 1: ['P1(a8,a2,a10)'], 2: []}),\
##           ({0: [], 1: [], 2: ['P1(x8,x6,a1)', 'P1(x8,x3,a1)']}, {0: [], 1: [], 2: ['P1(a3,a4,a1)', 'P1(a3,a9,a1)']}), \
##           ({0: [], 1: ['P1(x6,a5,x8)'], 2: ['P1(x6,x2,a5)']}, \
##            {0: ['P1(a5,a3,a7)', 'P1(a5,a3,a10)', 'P1(a5,a4,a7)', 'P1(a5,a4,a10)'], \
##             1: ['P1(a7,a5,a6)', 'P1(a10,a5,a9)'], 2: ['P1(a3,a9,a5)', 'P1(a4,a6,a5)', 'P1(a10,a8,a5)']})]
##把rs_zip中每个元素的两个元素的键进行比较，\
##如果键相等，并且键对应值的长度都大于0，\
##那么把两个键对应的值组成对（product - 笛卡尔积）。
##output -
##pairs_1arg = [['P1(x1,a2,x2)', 'P1(a8,a2,a10)'], ['P1(x6,a2,x8)', 'P1(a8,a2,a10)'], ['P1(x8,x6,a1)', 'P1(a3,a4,a1)'], ['P1(x8,x6,a1)', 'P1(a3,a9,a1)'], ['P1(x8,x3,a1)', 'P1(a3,a4,a1)'], ['P1(x8,x3,a1)', 'P1(a3,a9,a1)'], ['P1(x6,a5,x8)', 'P1(a7,a5,a6)'], ['P1(x6,a5,x8)', 'P1(a10,a5,a9)'], ['P1(x6,x2,a5)', 'P1(a3,a9,a5)'], ['P1(x6,x2,a5)', 'P1(a4,a6,a5)'], ['P1(x6,x2,a5)', 'P1(a10,a8,a5)']]

def get_pairs_1arg(index_arglit_R, index_arglit_F):
    rs_zip = list(zip(index_arglit_R, index_arglit_F))
    ##print('rs_zip = ' , rs_zip) 
    pairs_1arg = []
    for rs in rs_zip:
    ##    print()
        for key in rs[0].keys():
    ##        print('key = ', key)
            if key in rs[1] and rs[0][key] and rs[1][key]:              
                pairs_1arg.extend(list(product(rs[0][key], rs[1][key])))        
        ##        print( list(product(rs3[0][key3], rs3[1][key3])))
##    print('pairs_1arg = ', pairs_1arg)
                
    # 将每个元组中的元素转为list类型
    pairs_1arg = [list(pair) for pair in pairs_1arg]
##    print(pairs_1arg )
    return pairs_1arg


##print(get_pairs_1arg(index_arglit_R, index_arglit_F))
