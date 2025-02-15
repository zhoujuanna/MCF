

##input - 
##lits1arg_R = ['P1(x1,b3,x3)', 'P1(x3,b3,x1)']
##获取参数下标
##output --  [{'P1(x1,b3,x3)': {'x1': 0, 'b3': 1, 'x3': 2}}, {'P1(x3,b3,x1)': {'x3': 0, 'b3': 1, 'x1': 2}}]

def get_argindex(lits1arg_R):
    arg_indices = []
    for lr in lits1arg_R:
        arg = lr.split('(')[1].split(')')[0]
##        print('arg = ', arg)
        args_list = arg.split(',')
##        print('args_list = ', args_list)
        vs = {}
        for i, ar in enumerate(args_list):
##            print('ar:i = {}:{} '.format(ar,i))
            vs.update({ar:i})    
##        print({lr:vs})
        arg_indices.append({lr:vs})          

##    print(arg_indices)
    return arg_indices


##input - 
##lits1arg_R_idx = [{'P1(x1,b3,x3)': {'x1': 0, 'b3': 1, 'x3': 2}}, {'P1(x3,b3,x1)': {'x3': 0, 'b3': 1, 'x1': 2}}]
##对于列表lits1arg_R中的每个元素lr，找到lr值v中的键k以字母b开头的键值对，\
##添加到列表rsl中，列表rsl去重。
##output - [{'b3': 1}]
def get_constidx( lits1arg_R_idx):
    rsl = []
    for lr in lits1arg_R_idx:
        for k, v in lr.items():
            for key, value in v.items():
                if key.startswith('b'):
                    rsl.append({key: value})
    ##print(rsl)
##    去重
    unique_rsl = [dict(t) for t in {tuple(d.items()) for d in rsl}]

##    print(unique_rsl)
    return unique_rsl


##input - 
##rsl = [{'b3': 1}]
##F =  [{'P1(b1,b2,b3)': {'b1': 0, 'b2': 1, 'b3': 2}}, {'P1(b1,b3,b5)': {'b1': 0, 'b3': 1, 'b5': 2}}, {'P1(b2,b4,b6)': {'b2': 0, 'b4': 1, 'b6': 2}}, {'P1(b4,b5,b6)': {'b4': 0, 'b5': 1, 'b6': 2}}, {'P1(b1,b3,b2)': {'b1': 0, 'b3': 1, 'b2': 2}}]
##对于F中的每个元素lf， 如果元素lf值中包含rsl的元素，那么输出lf的键。
##output - ['P1(b1,b3,b5)', 'P1(b1,b3,b2)']

def get_ltFcontR(rsl , F_idx):
##    print('rsl , F_idx = ', rsl , F_idx)
    output_keys = []
    for lf in F_idx:
        for key, value in lf.items():
            for r in rsl:
                if r.items() <= value.items():
                    output_keys.append(key)
##    print(output_keys)
    return output_keys

##input
##lits1arg_R = ['P1(x1,b3,x3)', 'P1(x3,b3,x1)']
##F  = ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)']
##在F中找与lits1arg_R 中1个常量下标相同的文字
##output  index_arglit_F  =  ['P1(b1,b3,b5)', 'P1(b1,b3,b2)']
def get_litF_contR(lits1arg_R, F):
    lits1arg_R_idx = get_argindex(lits1arg_R)
    ##print(' lits1arg_R_idx =  ',lits1arg_R_idx )
    F_idx = get_argindex(F)
    ##print('\nF_idx = ',  F_idx)
    rsl = get_constidx( lits1arg_R_idx)
    ##print('\nrsl = ', rsl)
    iarF = get_ltFcontR(rsl , F_idx)
    return iarF

##index_arglit_F = get_litF_contR(lits1arg_R, F)
##print('index_arglit_F  = ', index_arglit_F )
