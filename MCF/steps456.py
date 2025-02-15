import step4plambda as s4, step5replace as s5, step6deleteconst as s6, step4check_inconsistency as s4b

##------
##            做选择准备
##            ищем уинфикатор lambda1 литераов lr и lf
##            получаем used
##            заменяем R
##            удаляем const из R и F
##            получаем R_isom_p
##            R <- R - const
##            F <- F - const

def steps456(qR, qF, R, F):
    partial_lambda = s4.find_partial_lambda(qR, qF)
##добавить проверка на противоречивость?
    partial_lambda = s4b.inconsistency_check_sk_dv(partial_lambda)    
##    print('\nstep4\npartial_lambda = ', partial_lambda)
    if len(partial_lambda) > 0:
        used = list(partial_lambda.values())
    ##    print('\nstep5\nused = ', used)
    ##    print('\nBefore replacing \nR = {}\t\tlen(R) = {}'.format(R, len(R)))
        R = s6.rplc_dict(R, partial_lambda)
    ##    print('\nstep6\nAfter replacing \nR = {}\t\tlen(R) = {}'.format(R, len(R)))            
        R_const, R = s6.get_lt_vr_cn(R)
    ##    print('R_const = {} \nR = {}'.format(R_const, R))            
    ##            R_smp.append(R_const)
        F_const, F = s6.del_lt_fromF(F, R_const)
    ##    print('F_const = {} \nF = {}'.format(F_const, F))
        R_isom_p = s6.find_common_elements(R_const, F_const)
    ##    print('R_isom_p = {} \t len(R_isom_p) = {}'.format(R_isom_p, len(R_isom_p)))
    else:
        partial_lambda = {}
        used = []
        R_const = []    
        F_const = []
        R_isom_p = []        
    return partial_lambda, used, R_const, R, F_const, F, R_isom_p
    
    
