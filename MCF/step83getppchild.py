R_child = ['P1(b3,x4,b2)', 'P1(b3,b1,x4)']	
F_child = ['P1(b1,b2,b3)', 'P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)']


def list_to_arglist(R_child):
    arglist = []
    for rc in R_child:
        arglist.append(rc.split('(')[1].split(')')[0].split(','))
##    print('arglist = ',arglist)
    return arglist


def get_poss_pairs(R_child, F_child):
    result = []

    for r_list in R_child:
        found_match = False
        for f_list in F_child:
            match = True
            for index, ele in enumerate(r_list):
    ##            print('\n\nindex, ele = ', index, ele)
                if not ele.startswith('x'):
    ##                print('\nf_list[{}] = {}'.format(index, f_list[index]) )
                    if index < len(f_list) and f_list[index] != ele:
    ##                    print('in  if ')
                        match = False
    ##                    print('match = ', match)
                        break
            if match:
    ##            print('in if match')
                result.append((r_list, f_list))            
                found_match = True
    ##            print('result = {} \nfound_match = {}'.format(result, found_match))
                break
        if not found_match:
            result.append(False)
    ##        print('result = {}'.format(result))

##    print(result)
##            如果result列表都是False，那没啥问题，\
##            如果包含True的话 , 注意要把只包含参数的列表还原到之前字符串的样子。
    return result

def gpp(R_child, F_child):

    R_child = list_to_arglist(R_child)
    F_child = list_to_arglist(F_child)
##    print('R_child = ', R_child)
##    print('F_child = ', F_child)
    
    pp = get_poss_pairs(R_child, F_child)
##    print('pp = ',pp)

##如果列表 pp 中所有的元素都为False那么输出False，否则输出True。
    ##pp = [False, False]
    ##pp = [(['b3', 'x4', 'b2'], ['b3', 'b2', 'b2']), False]
    result = any(pp)
##    print(result)
    return result

##print(gpp(R_child, F_child))
