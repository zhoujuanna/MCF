import re, itertools, time #导入time模块
import get_fr as fr

def get_lits(literal):    
    args_pr = re.findall(r'\((.*?)\)', literal)[0]
    args = args_pr.split(',')

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

def get_lits_Fm(R):    
    literals_r = R.split('&')
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



##------------------------------------

def main():
    
    time_list = []  #存100个公式获取lits的运行时间, 有100个元素的列表

##    for i in range(10):
##    R =  'P1(x1,x2,x3,x4)&P1(x1,x3,x5,x6)&P1(x5,x1,x3,x2)'
##    R = 'P(x2,x5,x4)&P(x2,x5,x3)&P(x5,x1,x3)&P(x4,x5,x2)&P(x5,x2,x1)'
##    print('R = ', R)
##        1 формул, 4 аргументов, 12 переменных, 25 литералов        
##        formulas = fr.get_formulas(10,4,12,25)
    formulas = fr.get_formulas(100,2,50,100)
    print('formulas = ', formulas)
    
    #1-获取开始时间
##    Python中的time.time()函数返回的是自1970年1月1日0时0分0秒以来的秒数(浮点数形式),也称为UNIX时间戳。\
##    因此,time.time()的单位是秒(s)。
    startTime = time.time()
##        print('startTime = ', startTime)
    
    #需要执行的函数或程序
    for f in formulas:
        lits_r  = get_lits_Fm(f)
##            print('lits_r = ', lits_r)
##    for j in range(len(lits_r)):
##        print('lits({},{},{},{}) = {}'.format(lits_r[j][0], lits_r[j][2], lits_r[j][1], lits_r[j][3], lits_r[j][4]))
##    print('\nlits_r = ', lits_r)
        
        #2-获取结束时间
        endtime = time.time()
    ##        print('endtime = ', endtime)
        #3-获取时间间隔
        dt = endtime-startTime
##        print('diffrentTime= ' , dt)

        time_list.append(dt)

##    print('time_list = ', time_list)
    average = sum(time_list) / len(time_list)
    maximum = max(time_list)
    minimum = min(time_list)
    print("minimum = {:.5f}, \naverage = {:.5f}, \nmaximum = {:.5f}".\
          format(minimum, average, maximum))



if __name__ == '__main__':    
    main()
