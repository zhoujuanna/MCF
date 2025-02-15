##input -
##up3 = [{'x3': 'a3', 'x5': 'a5', 'x6': 'a6'}, {'x3': 'a5', 'x5': 'a3', 'x6': 'a6'}], d = {'x3': 'a7'}
##判断是否把d作为一个新元素添加到up3中
##output - True

def isadd(up3, d):
##    print('up3 = {}, d = {}'.format(up3,d))
    r = []
    for item in up3:
    ##    print('\nitem = ', item)
        f = [key in item and item[key] != value for key, value in d.items()]
    ##    print('f = ',f)
        r.append(f[0])
    ##    print('r = ', r)
        if f == [False]:        
            break      

    result = False
    if len(r) > 0 and all(r):
        result = True
    ##print('\nresult = ', result)
    return result


##input -up1 = {'x1':'a1' , 'x2':'a2'}
##    up2 = [{'x3':'a3'},{'x3':'a5'},{'x5':'a5'},{'x5':'a3'},{'x6':'a6'},{'x3':'a7'}]
##创建合一子没有冲突的树
##只适合up2中每个元素长度为1的情况，不适合up二中每个元素长度为2的情况。
##换句话说，这个只适合1个文字中包含2个常量的情况，\
##不适合1个文字中包含一个常量的情况。
##output - up3 = [{'x3': 'a3', 'x5': 'a5', 'x6': 'a6'}, {'x3': 'a5', 'x5': 'a3', 'x6': 'a6'}, {'x3': 'a7'}] 
def cons_t(up1,up2):
    up3 = []
    for i in range(1, len(up2)):
##        print('\ni = ', i)
        
        for j in range(i):
##            print('\tj = ',j)
##            print('up2[i] = {} \t up2[j] = {}'.format(up2[i], up2[j]))
            
            if list(up2[i].keys()) == list(up2[j].keys()) and list(up2[i].values()) != list(up2[j].values()):
##                print('1键相等,值不等')
##                print('list(up2[i].keys()) = {} \t list(up2[j].keys()) = {}'.format( list(up2[i].keys()), list(up2[j].keys())))
                if len(up3) == 0:
                    up3.append(up2[j])
                    up3.append(up2[i])                
##                    print('up3 = ', up3)
                else: ##len(up3) != 0:
##                    print('len(up3) != 0')
    ##                print('up3, up2[i] = ', up3, up2[i])
    ##                print( isadd(up3, up2[i]))
                    if isadd(up3, up2[i]) == True:
##                        print('in if add')
                        up3.append(up2[i])
                 ##已加，不用再看了           
                        break
                        
                    else:
##                        print('已经添加，无需再加')
                        pass
##                    print('up3 = ', up3)               
                    
            elif list(up2[i].keys()) != list(up2[j].keys()) and list(up2[i].values()) != list(up2[j].values()):
##                print('2键不等，值不等')            
##                print('list(up2[i].keys()) = {}  \tlist(up2[j].keys()) = {} \
##    \nlist(up2[i].values()) = {} \t list(up2[j].values()) = {}'.\
##                      format(list(up2[i].keys()) , list(up2[j].keys()) , list(up2[i].values()) , list(up2[j].values())))
    ##            for k in range(len(up3)):
    ##                print('k = ', k, 'up3[k] = ', up3[k])
##                print('up3 = {}'.format(up3))
                if j <  len(up3):
                    up3[j] = {**up3[j], **up2[i]}
                else:
                    pass
    ##            up3[j].update(up2[i])
##                print('up3 = {} \nup2 = {}'.format(up3, up2))
                
            elif list(up2[i].keys()) != list(up2[j].keys()) and list(up2[i].values()) == list(up2[j].values()):
##                print(('3 键不等，值相等') )
                if j == i-1:
##                    print('最后一个元素，所以不添加')
                    pass
                else:
##                    print('不是最后一个元素，添加')
                    flag = [not all(key in item and item[key] == value for key, value in up2[j].items()) \
                            for item in up3]      
                    for k in range(len(flag)):
##                        print('k= ', k)
##                        print('up3[k] = {} \t up2[j]  = {} '.format(up3[k], up2[j] ))
                        if flag[k] == True:
##                            print('添加')
##                            print('up3[k] = {} up2[i] = {}'.format(up3[k], up2[i]))
                            up3[k] = {**up3[k], **up2[i]}
##                    print('up3 = ', up3)           
            else:
                pass
                
##        print('up3 = {} '.format(up3 ))
    return up3

##input - 
##up3 = [{'x3': 'a3', 'x5': 'a5', 'x6': 'a6'}, {'x3': 'a5', 'x5': 'a3', 'x6': 'a6'}, {'x3': 'a7'}]
##up1 = {'x1':'a1' , 'x2':'a2'}
##output - up_all = [{'x3': 'a3', 'x5': 'a5', 'x6': 'a6', 'x1': 'a1', 'x2': 'a2'}, \
##{'x3': 'a5', 'x5': 'a3', 'x6': 'a6', 'x1': 'a1', 'x2': 'a2'}, {'x3': 'a7', 'x1': 'a1', 'x2': 'a2'}]


def get_upall(up3,up1):
    up_all = []
    for u3 in up3:        
##        print({**u3, **up1})
        up_all.append({**u3, **up1})
##        pass
##    print('up_all = ', up_all)
    return up_all


    

def main():
    up2 =  [{'x1': 'b1', 'x3': 'b2'}, {'x3': 'b1', 'x1': 'b2'}, {'x1': 'b1', 'x3': 'b5'}, {'x3': 'b1', 'x1': 'b5'}]
    up1 =  {'x2': 'b3', 'x4': 'b2', 'x6': 'b1'}
##    up1 = {'x1':'a1' , 'x2':'a2'}
##    up2 = [{'x3':'a3'},{'x3':'a5'},{'x5':'a5'},{'x5':'a3'},{'x6':'a6'},{'x3':'a7'}]
    ##up2 = [{'x3':'a3'},{'x3':'a5'},{'x5':'a5'},{'x6':'a6'}]
    up3 = cons_t(up1, up2)    
##    print('up3 =', up3)
    up_all = get_upall(up3,up1)


    print(get_upall(up3,up1))
##
##    cr_rl2arg_c2 =  [{'x2': 'a3'}, {'x2': 'a4'}, {'x2': 'a6'}, {'x3': 'a1'}]   ##up2
##    lm =  {'x4': 'a10', 'x7': 'a8', 'x5': 'a7', 'x1': 'a9', 'x8': 'a2', 'x6': 'a5'}   ##up1
##    up_all = get_upall(cons_t(lm, cr_rl2arg_c2)  , lm)
##    print('up_all = ',up_all)
    
    
if __name__ == '__main__':    
    main()
