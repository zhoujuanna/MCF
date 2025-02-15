import step0getRF as s0, step1getlits as s1, step2get2args as s2, step4plambda as s4, step5replace as s5,\
       step6deleteconst as s6, step7arevr as s7, steps456 as s456
import step81getcnstv as s81, step82getparamposition as s82, step83mergelambda as s83, \
       step81getlitscontainedused as s81b, step82getpairs as s82b,\
       step82prefor82groupargind as s82c, step82getpairs1arg as s82d,\
       step83correspondingrelationship as s83b, step82getpossplambda as s82e, \
       step85conflict as s85, step83getppchild as s83c, step82getFlcRcn as s82f, \
       step82getpp1arg as s82h, step83cons_t as s83d, step83consup12 as s83e, \
       step83getposspairs as s83f, step83getchildren as s83g, step83getrisom as s83h, \
       step83replace as s83i, step83getsubRisom as s83j, step86delsubset as s86, \
       step83prepbt as s83k,  step2getqueues  as s2b  

import copy

##----------------------

def bt(R, F, used, partial_lambda, R_isom_p, t, R_isom, qR, qF):#, found_pairs_lits):
    print('\nin bt')
    print('\nR = {} \tlen(R) = {} \nF = {} \tlen(F) = {} \nused = {} \npartial_lambda = {}  \
\nR_isom_p = {} \tlen(R_isom_p) = {} \nt = {}'.\
          format(R, len(R), F, len(F), used, partial_lambda, R_isom_p, len(R_isom_p), t))

##判断R中没有变量？或者R中有变量，但是在F中没有与之匹配的文字
##arevr(R) == True  意思是R中的参数都是常量
    if s7.arevr(R) == True or (s7.arevr(R) == False and s83c.gpp(R, F) == False):
        print('\nin if arevr(R) == True, R中没变量或F中没有与R同构的文字')

##+?  删除以下4行试试结果 看最终R_isom能不能等于134，不是105
##        if (qR, qF) not in found_pairs_lits:
##            found_pairs_lits.append((qR, qF))
##            print('found_pairs_lits = {} \tlen(found_pairs_lits) = {}'.\
##                  format(found_pairs_lits, len(found_pairs_lits)))                
##+?        
        
        if len(R_isom_p) >= 1:        
            R_isom_p = s83i.replace(R_isom_p, partial_lambda)
            print('\nR_isom_p = {} \t len(R_isom_p) = {} \npartial_lambda = {}'.\
                  format(R_isom_p,  len(R_isom_p), partial_lambda))
##            
##对字典按照键排序
            partial_lambda = dict(sorted(partial_lambda.items(), key=lambda x: int(x[0][1:])))
            R_isom_plist = [len(R_isom_p), R_isom_p, [partial_lambda]]
            print('R_isom_plist = ', R_isom_plist)

##!!!!!!!!!            
            if len(R_isom) == 0:
                R_isom.append(copy.deepcopy(R_isom_plist))
                print('\nR_isom = ', R_isom)
            else:##len(R_isom) > 0:
                print('in R_isom = s86.getmaxRisom(R_isom, R_isom_plist) ')
                R_isom = s86.getmaxRisom(R_isom, R_isom_plist)
                print('\nR_isom = ', R_isom, '\tlen(R_isom) = ', len(R_isom))
##!!!!!!!!!                

            return
        else:
            print('len(R_isom_p) < 1，不加到R_isom中')            
            partial_lambda = dict(sorted(partial_lambda.items(), key=lambda x: int(x[0][1:])))
            R_isom_plist = [len(R_isom_p), R_isom_p, [partial_lambda]]
            print('R_isom_plist = ', R_isom_plist)
            print('\nR_isom = ', R_isom)           
            

    else:##R中的参数有变量
##        t = s0.get_t(R[0])
##        print('t = ', t)
        lits_tR = [r for r in R if sum(u in r.split('(')[1].split(')')[0].split(',') for u in used) == t - 1]
        print('\nstep8a\nlits_tR = ', lits_tR)
        poss_pairs = s83f.find_matching_pairs(lits_tR, F, t - 1)
        print('step8c\nposs_pairs = ', poss_pairs)

        if len(poss_pairs) > 0:                    
            pairs_2arg = [list(pair) for pair in poss_pairs]
            print('step8c\npairs_2arg = ', pairs_2arg)

            if len(pairs_2arg) > 0:                    
                cr_rl2arg = s83b.get_cr_rl(pairs_2arg)
                print('cr_rl2arg = ', cr_rl2arg)
                
    ##                cr_rl2arg = s83d.get_upall(s83d.cons_t(partial_lambda, cr_rl2arg) , partial_lambda)
                cr_rl2arg = s83g.get_upall(s83g.getchild(partial_lambda, cr_rl2arg), partial_lambda)                
                print('cr_rl2arg = ', cr_rl2arg)
                
                if len(cr_rl2arg) > 0:
                    clm = 0
                    for lm in cr_rl2arg:
                        print('\n\nclm =  {} \tlm = {}' .format(clm, lm))
                        clm = clm +1
                        used_child = list(lm.values())
                        print('used_child = ', used_child)
                        
##                        为用bt做准备，即，准备输入的变量
                        R_child, F_child, used_child, lm, R_isom_p_child, R_isom_p_child_backup, \
                                 used_child_backup, R_backup_child, F_backup_child = \
                                 s83k.prepbtchild(R, lm, F, R_isom_p, used_child)
##                        print('@@@R_child = {} \nF_child = {} \nused_child = {} \nlm = {} \nR_isom_p_child  = {} \
##                                 \nR_isom_p_child_backup = {} \nused_child_backup = {}'.\
##                              format(R_child, F_child, used_child, lm, R_isom_p_child, \
##                                 R_isom_p_child_backup, used_child_backup))                     

                        bt(R_child, F_child, used_child, lm, R_isom_p_child, t, R_isom, qR, qF)#, found_pairs_lits)

                        R_isom_p_child  = copy.deepcopy(R_isom_p_child_backup)
                        print('\n恢复现场,转兄弟节点\nR_isom_p_child = ', R_isom_p_child)
                        used_child = copy.deepcopy(used_child_backup)
                        print('used_child = {}'.format(used_child))

                        R = copy.deepcopy(R_backup_child)
                        F = copy.deepcopy(F_backup_child)
                        
                    
                else: ##len(cr_rl2arg) == 0:
                    print('len(cr_rl2arg) == 0')
                    if t > 2:                        
                        print('t = {}, 继续递归 bt'.format(t))
                        lits_tR = [r for r in R if sum(u in r.split('(')[1].split(')')[0].split(',') for u in used) >= t - 1]
                        print('lits_tR = ', lits_tR)
                        R = list(set(R) - set(lits_tR))
                        t = t - 1                        
                        print('F = {}  \tlen(F) = {} \nused = {} \npartial_lambda = {} \nR_isom_p = {}  \
\nt = {}'. format(F, len(F), used, partial_lambda, R_isom_p, t))
                        bt(R, F, used, partial_lambda, R_isom_p, t, R_isom, qR, qF)#, found_pairs_lits)      
                    
                    elif t == 2:
                        print('t = 3,2,1,找完了')                    
                        print('\n\nR_isom_p = {} \tlen(R_isom_p) = {}'.format(R_isom_p, len(R_isom_p)))
                        
##                        if (qR, qF) not in found_pairs_lits:
##                            found_pairs_lits.append((qR, qF))
##                            print('found_pairs_lits = {} \tlen(found_pairs_lits) = {}'.\
##                                  format(found_pairs_lits, len(found_pairs_lits))) 

                        if len(R_isom_p) >= 1:
                            R_isom_p = s83i.replace(R_isom_p, partial_lambda)
                            print('R_isom_p = ', R_isom_p)

                ##对字典按照键排序
                            partial_lambda = dict(sorted(partial_lambda.items(), key=lambda x: int(x[0][1:])))
                            R_isom_plist = [len(R_isom_p), R_isom_p, [partial_lambda]]
                            print('R_isom_plist = ', R_isom_plist)                            

    ##!!!!!!!!!            
                            if len(R_isom) == 0:
                                R_isom.append(copy.deepcopy([len(R_isom_p), R_isom_p, [partial_lambda]]))
                                print('\nR_isom = ', R_isom)
                            else:##len(R_isom) > 0:
                                R_isom = s86.getmaxRisom(R_isom, [len(R_isom_p), R_isom_p, [partial_lambda]])
                                print('\nR_isom = ', R_isom, '\tlen(R_isom) = ', len(R_isom))
    ##!!!!!!!!!                            
    ##                        R_isom.append([len(R_isom_p), R_isom_p, [partial_lambda]])
                                print('\nR_isom = ', R_isom)                               
                            return
                        
                        else:## len(R_isom_p) <= 1:                                
                            print('len(R_isom_p) < 1，不加到R_isom中')                                
    ##                        if len(R_isom) == 0:
    ##                            print('\n\nR_isom = empty ')
    ##                        else:                                
                            print('\n\nR_isom = ', R_isom)                            
                    else:
                        pass                    
                
            else: ## len(pairs_2arg) == 0:
                print('len(pairs_2arg) == 0')
                pass                
                
        else:##len(poss_pairs) == 0
            print('len(poss_pairs) == 0')
##            print('R = {} \nlits_tR  = {}'.format(R, lits_tR ))
##            R = R - lits_tR

##            print('R = {} \tlen(R) = {}'.format(R, len(R)))
            lits_tR = [r for r in R if sum(u in r.split('(')[1].split(')')[0].split(',') for u in used) >= t - 1]
##            print('lits_tR = ', lits_tR)
            R = list(set(R) - set(lits_tR))                        
##            print('R = {} \tlen(R) = {}'.format(R, len(R)))
##            print('F = {}  \tlen(F) = {} \nused = {} \npartial_lambda = {} \nR_isom_p = {}  \nt = {}'.\
##                  format(F, len(F), used, partial_lambda, R_isom_p, t))
            if t > 2:
                t = t - 1
                bt(R, F, used, partial_lambda, R_isom_p, t, R_isom, qR, qF)#, found_pairs_lits)            

##            print('\n\n\nR = {} \tlen(R) = {} \nF = {} \tlen(F) = {} \nused = {} \
##\npartial_lambda = {} \nR_isom_p = {} \nt - 1 = {} '.\
##                  format(R, len(R), F, len(F), used, partial_lambda, R_isom_p, t - 1))
##            R = ['P1(x1,b2,x3)', 'P1(x1,b2,b6)', 'P1(x3,b2,x1)', 'P1(b2,x1,b4)'] 	len(R) = 4 
##            print('lits_tR = ', lits_tR)
##            lits_tR =  ['P1(x1,b2,b6)', 'P1(b2,x1,b4)']
##            bt(R, F, used, partial_lambda, R_isom_p, t)            
            pass       
                

##---------------------------
        
def backtrack(R_isom_p, R, F, queue_R, queue_F, t, R_isom): ##, found_pairs_lits):
##def backtrack(R_isom_p, R, F, queue_R, queue_F, t, R_isom):
    print('\n\nin backtrack')
    print('R = {} \tlen(R) = {} \nF = {} \tlen(F) = {}'.format(R, len(R), F, len(F)))
    if len(R_isom_p) > 0:
        print('R_isom_p = {} \tlen(R_isom_p) = {}'.format(R_isom_p, len(R_isom_p)))

##    print('qR = {} \tqF = {}'.format(qR, qF))
    
    t_backup = t
    count_in_2for = 1 
    for qR in queue_R:
        for qF in queue_F:
            print('\n\ncount_in_2for =', count_in_2for)
            R_backup = copy.deepcopy(R)
            F_backup = copy.deepcopy(F)            
            print('\nstep3\nqR = {} \tqF = {}'.format(qR, qF))
            count_in_2for += 1          
            partial_lambda, used, R_const, R, F_const, F, R_isom_p = s456.steps456(qR, qF, R, F)
            print('partial_lambda = {} \nused  = {}  \nR = {} \tlen(R) = {} \nR_const  = {}  \
    \nF = {} \tlen(F) = {} \nF_const = {}\nR_isom_p = {} \tlen(R_isom_p) = {}'\
                      .format(partial_lambda, used, R, len(R), R_const,  F, len(F) , F_const,  \
                              R_isom_p, len(R_isom_p)))
                
            if s7.arevr(R) == True:
                print('\nstep7 There are no variables in formula R')

                if len(R_isom_p) >= 1:        
                    R_isom_p = s83i.replace(R_isom_p, partial_lambda)
                    print('\nR_isom_p = {} \t len(R_isom_p) = {} \npartial_lambda = {}'.\
                          format(R_isom_p,  len(R_isom_p), partial_lambda))
        ##            
        ##对字典按照键排序
                    partial_lambda = dict(sorted(partial_lambda.items(), key=lambda x: int(x[0][1:])))
                    R_isom_plist = [len(R_isom_p), R_isom_p, [partial_lambda]]
                    print('R_isom_plist = ', R_isom_plist)

        ##!!!!!!!!!            
                    if len(R_isom) == 0:
                        R_isom.append(copy.deepcopy(R_isom_plist))
                        print('\nR_isom = ', R_isom)
                    else:##len(R_isom) > 0:
                        print('in R_isom = s86.getmaxRisom(R_isom, R_isom_plist) ')
                        R_isom = s86.getmaxRisom(R_isom, R_isom_plist)
                        print('\nR_isom = ', R_isom, '\tlen(R_isom) = ', len(R_isom))
        ##!!!!!!!!!

##                    if count_in_2for -1 ==1:
                    R = copy.deepcopy(R_backup)
                    print('\n返回上层R = {} \t len(R) = {}'.format(R, len(R)))
                    F = copy.deepcopy(F_backup)
                    print('F = {} \t len(F) = {}'.format(F, len(F)))                    
                    continue

                else:
                    print('len(R_isom_p) < 1，不加到R_isom中')            
                    partial_lambda = dict(sorted(partial_lambda.items(), key=lambda x: int(x[0][1:])))
                    R_isom_plist = [len(R_isom_p), R_isom_p, [partial_lambda]]
                    print('R_isom_plist = ', R_isom_plist)
                    print('\nR_isom = ', R_isom)           
               
                
##                if len(queue_R) == 0:
##                    print('queue_R is empty     需要补     очередь пуста, то переходим к п. 2.')
##                else:
##                    print('queue_R is not empty     需要补     очередь не пуста, то переходим к п. 3.  2个for循环实现')

        ##step8
            else:
                bt(R, F, used, partial_lambda, R_isom_p, t, R_isom, qR, qF) ##, found_pairs_lits)                                           
                
            R = copy.deepcopy(R_backup)
            print('\n返回上层R = {} \t len(R) = {}'.format(R, len(R)))
            F = copy.deepcopy(F_backup)
            print('F = {} \t len(F) = {}'.format(F, len(F)))

            
##        else:##(qR, qF) not in found_pairs_lits   (qR, qF)已经找过R了，不用再找
##            print('{}在之前的对中已经找过R了，不用再找'.format((qR, qF)))
##            pass


##---------------------------

def pred(F1, F2):
    
##step0    
    R, F = s0.getRF(F1, F2)
    print('\nstep0')
##    print('\nR = {} \nF = {} '.format(R, F))
##    R中的变量+个数
##    name_var_R, numb_var_R = s0.count_unique_x_parameters(R)
##    print('name_var_R = {} \tnumb_var_R = {}'.format(name_var_R, numb_var_R))

    R = R.split('&')
    R_backup = copy.deepcopy(R)    
    F = F.split('&')
    F_backup = copy.deepcopy(F)
    print('R = ', R, '\nF = ', F)    
    

##step1
##    lits_R = s1.get_lits_Fm(R)
##    lits_F = s1.get_lits_Fm(F)
##    lits_R = sorted(lits_R, key=lambda x: (x[0], x[2], x[1], x[3])) 
##    lits_F = sorted(lits_F, key=lambda x: (x[0], x[2], x[1], x[3])) 
##    print('\nstep1\nlits_R = {} \nlits_F = {} '.format(lits_R, lits_F))

## t-position - 每个文字中包含变量的数量 
    if len(R) > 0:
        t = s0.get_t(R[0])
##        print('t = ', t)
        t_bckp = t
        
##    R_isoms = []##存最终结果
    R_isom = [] ##存最终结果
##    found_pairs_lits = []   ##存从哪些文字对开始找R和合一子

##step2
    print('\nstep2')

    print('R = {} \nF = {}'.format(R, F))

    pps = s2b.queues(R, F)
##    litsR = s2b.prep_queue(R)
##    litsF = s2b.prep_queue(F)
##    print('litsR = {} \nlitsF = {}'.format(litsR, litsF) )
##    pps = s2b.get_queues(litsR, litsF)
##    去重，有可能减少pps的长度
##    print('pps = {} \tlen(pps) = {}'.format(pps, len(pps)))
    pps = s2b.remove_duplicates(pps)
    print('\npps = {} \tlen(pps) = {}'.format(pps, len(pps)))

    count_in_queue = 1   
    for pp in pps:                    
##        print('\n', pp)##, '\t', len(pp[0]), len(pp[1]))
        print('\n{}-th queue'.format(count_in_queue) )
        count_in_queue = count_in_queue + 1
        queue_R = pp[0]
        queue_F = pp[1]        
        print('queue_R = {} \nqueue_F = {}'.format(queue_R, queue_F))
   
##step3
        t = t_bckp
        R = copy.deepcopy(R_backup)
        F = copy.deepcopy(F_backup)
####        print('\nbefore backtrack R = {} \tlen(R) = {} \nF = {}  \tlen(F) = {} \nt = {}\
####\nR_isom = {} '. format(R,  len(R), F, len(F), t, R_isom))


        backtrack([], R, F, queue_R, queue_F, t, R_isom) ##, found_pairs_lits)
    ##    backtrack([], R, F, queue_R, queue_F, t, R_isom)     
        print('\nAfter backtrack \tR_isom = {} \tlen(R_isom) = {}'.format(R_isom,  len(R_isom)))
            
##        R_isoms.append(R_isom)
##        print('\n\nR_isoms = {} \tlen(R_isoms) = {}'.format(R_isoms,  len(R_isoms)))
        
    print('\n\nR_isom = {} \tlen(R_isom) = {}'.format(R_isom,  len(R_isom)))

    return R_isom


def main():
    print(pred(R, F))
    

if __name__ == '__main__':    
    main()


