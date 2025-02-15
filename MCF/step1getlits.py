import re, itertools##, time #导入time模块


##-------------------------
def get_lits(literal):    
    args_pr = re.findall(r'\((.*?)\)', literal)[0]
    args = args_pr.split(',')
##    print('args = ', args)
    idxs_args = list(itertools.combinations(list(enumerate(args)),2))
    ##print('idxs_args = ', idxs_args)

    # 将元组列表的每个元素及其子元素的类型转换为列表
    idxs_args = [list(map(list, item)) for item in idxs_args]

    for i in range(len(idxs_args)):
    ##    print('\nidxs_args[i] = ', idxs_args[i])
        idxs_args[i][0].extend(idxs_args[i][1])
        idxs_args[i].pop()
        idxs_args[i] = idxs_args[i][0]
        idxs_args[i].append(literal)
    ##    print('idxs_args[i] = ', idxs_args[i])
    ##    print('lits_{}_{}_{}_{} = {}'.format(idxs_args[i][0],idxs_args[i][2],idxs_args[i][1],idxs_args[i][3], idxs_args[i][4]))   
    ##print(idxs_args)
    return idxs_args


##-------------------------

def get_lits_Fm(R):    
    literals_r = R
    lits_r = []
    for i in range(len(literals_r)):
##        print('\n', literals_r[i])
        lit_r = get_lits(literals_r[i])
##        print('lit_r = ', lit_r)
        lits_r.extend(lit_r)
##        for j in range(len(lit_r)):
##            print('lits({},{},{},{}) = {}'.format(lit_r[j][0], lit_r[j][2], lit_r[j][1], lit_r[j][3], lit_r[j][4]))
##    print('\nlits_r = ', lits_r)
    return lits_r

##-------------------------

def main():
    R = 'P1(x1,x2,x3)&P1(x1,x2,x6)&P1(x2,x4,x6)&P1(x3,x2,x1)&P1(x2,x1,x4)'
    R = R.split('&')
    lits_r  = get_lits_Fm(R)
    print('lits_r = ', lits_r)
    print('R = ', R)


##-------------------------
    
if __name__ == '__main__':    
    main()
