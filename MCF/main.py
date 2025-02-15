import npt, pred, npredstep3MCF2 as ns3
from collections import defaultdict
import copy

##input 
##F_list  = ['P1(a1,a2,a3,a4)', 'P1(a2,a3,a1,a4)', 'P2(a1,a2,a3,a4)', 'P2(a2,a3,a1,a4)', 'P3(a1)', 'P3(a2)', 'P3(a3)', 'P3(a4)']
##按照谓词名称分组，得字典。
##output 
##F_dict  = {'P1': ['P1(a1,a2,a3,a4)', 'P1(a2,a3,a1,a4)'], 'P2': ['P2(a1,a2,a3,a4)', 'P2(a2,a3,a1,a4)'], 'P3': ['P3(a1)', 'P3(a2)', 'P3(a3)', 'P3(a4)']}

def groupbypred(F_list):
    
    Ps = set()
    for item in F_list:
        index = item.index('(')
    ##    print('index = ', index)
        p_name = item[:index]
    ##    print('p_name = ', p_name)
        Ps.add(p_name)
##    print(Ps)
    Ps = sorted(list(Ps))
##    print('Ps = ', Ps)
    ##Ps = ['P1', 'P2', 'P3']
    ##F1_list = ['P1(a1,a2,a3,a4)', 'P1(a2,a3,a1,a4)', 'P2(a1,a2,a3,a4)', 'P2(a2,a3,a1,a4)', 'P3(a1)', 'P3(a2)', 'P3(a3)', 'P3(a4)']
    F_dict = {key: [val for val in F_list if key in val] for key in Ps}
##    print('F1_dict = ', F1_dict)
    return F_dict

##---------------

##input - 
##F1_dict = {'P1': ['P1(a1,a2,a3,a4)', 'P1(a2,a3,a1,a4)'], 'P2': ['P2(a1,a2,a3,a4)', 'P2(a2,a3,a1,a4)'], 'P3': ['P3(a1)', 'P3(a2)', 'P3(a3)', 'P3(a4)']}
##F2_dict = {'P1': ['P1(b1,b2,b3,b4)', 'P1(b2,b3,b1,b4)'], 'P2': ['P2(b1,b2,b3,b4)', 'P2(b2,b3,b1,b4)', 'P2(b1,b2,b2,b3)']}
##把两个公式（字典）合并，按照谓词名称分组。
##output -
##Fs_list =  [('P1', [['P1(a1,a2,a3,a4)', 'P1(a2,a3,a1,a4)'], ['P1(b1,b2,b3,b4)', 'P1(b2,b3,b1,b4)']]), ('P2', [['P2(a1,a2,a3,a4)', 'P2(a2,a3,a1,a4)'], ['P2(b1,b2,b3,b4)', 'P2(b2,b3,b1,b4)', 'P2(b1,b2,b2,b3)']]), ('P3', [['P3(a1)', 'P3(a2)', 'P3(a3)', 'P3(a4)']])]

def group2formulas(F1_dict, F2_dict):
    grouped_dict = defaultdict(list)

    for d in [F1_dict, F2_dict]:
    ##    print('\n\nd = ', d)
        for key, value in d.items():
            grouped_dict[key].append(value)
    ##        print('grouped_dict = ', grouped_dict)

    F_dict = dict(grouped_dict)
##    print('F_dict = ', F_dict)

    Fs_list = [(key, value) for key, value in F_dict.items()]
##    print('Fs_list = ', Fs_list)
    
    return Fs_list

##---------------


def getF12():
    F1, F2 = npt.input()
    print('Initial data: \nF1 = {} \nF2 = {}'.format(F1, F2))
##    print(len(F1.split('&')))
##    print(len(F2.split('&')))

    if isinstance(F1, str):
        F1_list = F1.split('&')
##    print('\nF1_list  = {}'.format(F1_list))
##    对每个公式按照谓词名称分组
    else:
        F1_list = copy.deepcopy(F1)           
    F1_dict = groupbypred(F1_list)
##    print('F1_dict  = {}'.format(F1_dict))
    if isinstance(F2, str):
        F2_list = F2.split('&')
##    print('\nF2_list  = {}'.format(F2_list))
    else:
        F2_list = copy.deepcopy(F2)
        
##    对每个公式按照谓词名称分组
    F2_dict = groupbypred(F2_list)
##    print('F2_dict  = {}'.format(F2_dict))

    Fs_list = group2formulas(F1_dict, F2_dict)
##    print('\nFs_list = ', Fs_list)

##    如果在一个公式中有一个谓词符号，在另一个公式中没有，\
##    那么删除该谓词符号对应的文字。
    Fs_list = [e for e in Fs_list if len(e[1]) != 1]

    return Fs_list

##---------------

def main():
    
##step1
    Fs_list = getF12()
    print('\nFs_list = ', Fs_list)
##    print('\nR = {}  \nF = {}'.format(R, F))

##step2
    
    R_isom_g = []
    for i in range(len(Fs_list)):
        print('\ni = {}'.format(i))
        for j in range(len(Fs_list[i][1])):            
##            print('len(Fs_list[i][1]) = ', len(Fs_list[i][1]))            
##            print('\tj = {}'.format(j))
            print('Fs_list[{}][1][{}] = {} '.format(i, j, Fs_list[i][1][j]) )

        F1 = '&'.join(Fs_list[i][1][0])
        F2 = '&'.join(Fs_list[i][1][1])
        print('F1 = {} \nF2 = {}'.format(F1, F2) )
        R_isom = pred.pred(F1, F2)        
        R_isom_g.append(R_isom)
        print('\nR_isom_g = ', R_isom_g)

##step3
##    R_isom = R_isom_g[0]
    if len(R_isom_g) > 1:
##        for np in range(len((R_isom_g))):        
##        R_isom1 = R_isom_g[1]
        R_isom_12 = ns3.unionRp12(R_isom_g[0], R_isom_g[1])
        print('\nR_isom_12 = ', R_isom_12)

        if len(R_isom_g) > 2:
            R_isom_123 = ns3.unionRp12(R_isom_12, R_isom_g[2])
            print('\nR_isom_123 = ', R_isom_123)

            if len(R_isom_g) > 3:
                R_isom_1234 = ns3.unionRp12(R_isom_123, R_isom_g[3])
                print('\nR_isom_1234 = ', R_isom_1234)       
            
        

            


if __name__ == '__main__':    
    main()
