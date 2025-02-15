import step82getFlcRcn as s82f

##input - 
##lits1arg_R_idx = [{'P1(x1,b2,x3)': {'x1': 0, 'b2': 1, 'x3': 2}}, {'P1(x3,b2,x1)': {'x3': 0, 'b2': 1, 'x1': 2}}]
##lits1arg_F_idx = [{'P1(b1,b2,b3)': {'b1': 0, 'b2': 1, 'b3': 2}}, {'P1(b1,b3,b5)': {'b1': 0, 'b3': 1, 'b5': 2}}, \
##                  {'P1(b3,b2,b1)': {'b3': 0, 'b2': 1, 'b1': 2}}, {'P1(b4,b5,b6)': {'b4': 0, 'b5': 1, 'b6': 2}}, \
##                  {'P1(b1,b3,b2)': {'b1': 0, 'b3': 1, 'b2': 2}}]
##rsl = [{'b2': 1}]

##求可能对（适合R的文字中包含一个常量的情况，\
##而且该常量在不同的文字中的下标一样：rsl = [{'b2': 1}]）
##如果没有可能对，返回[]
##output - [('P1(x1,b2,x3)', 'P1(b1,b2,b3)'), ('P1(x1,b2,x3)', 'P1(b3,b2,b1)'), ('P1(x3,b2,x1)', 'P1(b1,b2,b3)'), ('P1(x3,b2,x1)', 'P1(b3,b2,b1)')]

def get_posspairs1arg(lits1arg_R_idx, lits1arg_F_idx, rsl):
    pps = []
    for r in rsl:
        ppr = {}
        for lr in lits1arg_R_idx:
            for kr, vr in lr.items():
                if r.items() <= vr.items():
                    if len(ppr) == 0:
                        ppr[list(r.items())[0]] = kr
                    else: ## len(pp) > 0: 
                        value_list = [ppr[list(r.items())[0]]]
                        value_list.append(kr)
                        ppr[list(r.items())[0]] = value_list
##        print('in r ppr = ', ppr)
        ppf = {}           
        for lf in lits1arg_F_idx:
            for kf, vf in lf.items():
                if r.items() <= vf.items():
                    if len(ppf) == 0:
                        ppf[list(r.items())[0]] = kf
                    else: ## len(pp) > 0: 
                        value_list = [ppf[list(r.items())[0]]]
                        value_list.append(kf)
                        ppf[list(r.items())[0]] = value_list
##        print('in f ppf =', ppf)

    k = list(ppr.keys())[0]

    if k in ppr and k in ppf:
        if isinstance(ppr[k],str):
            ppr[k] = [ppr[k]]
        if isinstance(ppf[k],str):
            ppf[k] = [ppf[k]]
        
        pp = [(x, y) for x in ppr[k] for y in ppf[k]]
##        print('pp = ', pp)
        return pp
    else:
        return []


##input
lits1arg_R = ['P1(x1,b3,x3)', 'P1(x3,b3,x1)']
F  = ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b2,b4,b6)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)']
##output - 
##lits1arg_R_idx = [{'P1(x1,b3,x3)': {'x1': 0, 'b3': 1, 'x3': 2}}, {'P1(x3,b3,x1)': {'x3': 0, 'b3': 1, 'x1': 2}}] \
##lits1arg_F_idx =   [{'P1(b1,b2,b3)': {'b1': 0, 'b2': 1, 'b3': 2}}, {'P1(b1,b3,b5)': {'b1': 0, 'b3': 1, 'b5': 2}}, \
##                    {'P1(b2,b4,b6)': {'b2': 0, 'b4': 1, 'b6': 2}}, {'P1(b4,b5,b6)': {'b4': 0, 'b5': 1, 'b6': 2}}, \
##                    {'P1(b1,b3,b2)': {'b1': 0, 'b3': 1, 'b2': 2}}] \
##rsl  = [{'b3': 1}]


def prep(lits1arg_R, F):
    lits1arg_R_idx = s82f.get_argindex(lits1arg_R)
    ##print(' lits1arg_R_idx =  ',lits1arg_R_idx )
    lits1arg_F_idx = s82f.get_argindex(F)
    ##print('\nF_idx = ',  F_idx)
    rsl = s82f.get_constidx( lits1arg_R_idx)
    ##print('\nrsl = ', rsl)
##    print(lits1arg_R_idx, lits1arg_F_idx, rsl)
    return lits1arg_R_idx, lits1arg_F_idx, rsl




lits1arg_R_idx, lits1arg_F_idx, rsl = prep(lits1arg_R, F)
##print(lits1arg_R_idx, lits1arg_F_idx, rsl)
##print(get_posspairs1arg(lits1arg_R_idx, lits1arg_F_idx, rsl))    

