##input - 
##indices_R1 = ['P1(x8,x6,a1)', 'P1(x8,x3,a1)']
##arg_found = 'a1'
##求 arg_found 在列表indices_R1中每个元素的下标, 根据下标分组元素.
##output - {0: [], 1: [], 2: ['P1(x8,x6,a1)', 'P1(x8,x3,a1)']}

def index_arg(indices_R1, arg_found):
    index_dict = {0:[],1:[], 2:[]}
    # 遍历列表indices_R1
    for i, element in enumerate(indices_R1):    
        # 获取'a2'在元素中的下标
        args = element.split('(')[1].split(')')[0].split(',')
##        print('args = ', args)
        try:
            index = args.index(arg_found)
        except ValueError:
            index = -1
##        print('index = ', index)
        if index in index_dict:
            index_dict[index].append(element)
        else:
            index_dict[index] = [element]

    index_dict = dict(sorted(index_dict.items(), key=lambda x: x[0]))
    ##print(sorted(index_dict.keys()))
##    print('index_dict = ', index_dict)
    return index_dict

##-------------------------------------------

##input - 
##used_args =  ['a2', 'a1', 'a5']
##search_list =   ['P1(x1,a2,x2)', 'P1(a2,x6,x1)', 'P1(x6,x2,a5)', 'P1(x6,x2,a2)', \
##'P1(x6,a5,x8)', 'P1(x6,a2,x8)', 'P1(x8,x6,a1)', 'P1(x8,x3,a1)']
##先根据列表used_args中的元素对search_list中的元素分组， 得grp_R。
##在组内 对分组后的元素找下标，按下标分组。
##output - 
##grp_R =  [['P1(x1,a2,x2)', 'P1(a2,x6,x1)', 'P1(x6,x2,a2)', 'P1(x6,a2,x8)'], \
##              ['P1(x8,x6,a1)', 'P1(x8,x3,a1)'], ['P1(x6,x2,a5)', 'P1(x6,a5,x8)']] 
##index_arglit_R =  [{0: ['P1(a2,x6,x1)'], 1: ['P1(x1,a2,x2)', 'P1(x6,a2,x8)'], 2: ['P1(x6,x2,a2)']}, \
##            {0: [], 1: [], 2: ['P1(x8,x6,a1)', 'P1(x8,x3,a1)']}, {0: [], 1: ['P1(x6,a5,x8)'], 2: ['P1(x6,x2,a5)']}]



def find_indices_formula(used_args, search_list):    
##    print('used_args = ', used_args , 'search_list =  ', search_list)
    indices = []
    ind_arg_lits = []    
    for used_arg in used_args:        
        lits_used_arg = [x for i, x in enumerate(search_list) if used_arg in x.split('(')[1].split(')')[0].split(',')]
##        print('\nlits_used_arg = ', lits_used_arg)
        indices.append(lits_used_arg)        
##        print('indices = ', indices)
        ind_arg = index_arg(lits_used_arg, used_arg)
##        print('ind_arg = ',ind_arg)
        ind_arg_lits.append(ind_arg)
##        print('ind_arg_lits = ',ind_arg_lits)
    return indices, ind_arg_lits


##lits1arg_R = ['P1(x1,a2,x2)', 'P1(a2,x6,x1)', 'P1(x6,x2,a5)', 'P1(x6,x2,a2)', \
##              'P1(x6,a5,x8)', 'P1(x6,a2,x8)', 'P1(x8,x6,a1)', 'P1(x8,x3,a1)'] 
##lits1arg_F = ['P1(a3,a4,a1)', 'P1(a3,a9,a5)', 'P1(a3,a9,a1)', 'P1(a4,a6,a5)', \
##              'P1(a5,a3,a7)', 'P1(a5,a3,a10)', 'P1(a5,a4,a7)', 'P1(a5,a4,a10)', \
##              'P1(a7,a5,a6)', 'P1(a8,a2,a10)', 'P1(a10,a5,a9)', 'P1(a10,a8,a5)']
##used = ['a2', 'a1', 'a5']

##grp_R,index_arglit_R = find_indices_formula(used, lits1arg_R)
##print('\ngrp_R = ', grp_R, '\nindex_arglit_R = ', index_arglit_R)
##
##grp_F, index_arglit_F = find_indices_formula(used, lits1arg_F)
##print('\ngrp_F = ', grp_F, '\nindex_arglit_F = ', index_arglit_F )

