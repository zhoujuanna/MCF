import step6deleteconst as s6
import copy

##R_isom = []
##input --
##R = ['P1(x1,b2,x3)', 'P1(x3,b2,x1)'] 
##lm = {'x1': 'b3', 'x3': 'b1', 'x2': 'b2', 'x4': 'b4', 'x6': 'b6'}
##F = ['P1(b1,b2,b3)', 'P1(b1,b3,b5)', 'P1(b3,b2,b1)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)'] 
##R_isom_p = ['P1(b2,b4,b6)'] 
##used_child = ['b3', 'b1', 'b2', 'b4', 'b6']
##为用bt做准备，即，准备输入的变量
##output -
##R_child = [] 
##F_child = ['P1(b1,b3,b5)', 'P1(b4,b5,b6)', 'P1(b1,b3,b2)'] 
##used_child = ['b3', 'b1', 'b2', 'b4', 'b6'] 
##lm = {'x1': 'b3', 'x3': 'b1', 'x2': 'b2', 'x4': 'b4', 'x6': 'b6'} 
##R_isom_p_child  = ['P1(b2,b4,b6)', 'P1(b3,b2,b1)', 'P1(b1,b2,b3)']                                  
##R_isom_p_child_backup = ['P1(b2,b4,b6)'] 
##used_child_backup = ['b3', 'b1', 'b2', 'b4', 'b6']
def prepbtchild(R, lm, F, R_isom_p, used_child):
##    print('\n\n\n@@@prepbtchild(R, lm, F, R_isom_p, used_child) : \n R = {} \nlm = {}\
##\nF = {} \nR_isom_p = {} \nused_child = {}'.format(R, lm, F, R_isom_p, used_child))


    R_backup_child = copy.deepcopy(R)
    F_backup_child = copy.deepcopy(F)                       
    print('R = {} \tlen(R) = {} \nF = {} \tlen(F) = {}'.format(R, len(R), F, len(F)))
    
    R_child = s6.rplc_dict(R, lm)                            
    print('s83->step6 After replacing \nR = {}\t\tlen(R) = {}'.format(R, len(R))) 
    R_const_child, R_child = s6.get_lt_vr_cn(R)
    print('R_const_child = {} \tlen(R_const_child) = {} \
\nR_child = {} \tlen(R_child) = {}'.format(R_const_child, len(R_const_child), R_child, len(R_child) ))            
##                            R_smp.append(R_const_child)
    F_child = copy.deepcopy(F)
    F_const_child, F_child = s6.del_lt_fromF(F_child, R_const_child)
    print('F_const_child = {} \tlen(F_const_child) = {} \
\nF_child = {} \tlen(F_child) = {}'.format(F_const_child, len(F_const_child) , F_child, len(F_child)))

    R_isom_p_child = []                            
    R_isom_p_child.extend(R_isom_p)
    R_isom_p_child_backup = copy.deepcopy(R_isom_p_child)
    print('R_isom_p_child_backup = {}'.format(R_isom_p_child_backup))
    R_isom_p_child.extend(s6.find_common_elements(R_const_child, F_const_child))
    print('R_isom_p_child = {} \t len(R_isom_p_child) = {}'.\
          format(R_isom_p_child, len(R_isom_p_child)))
    used_child_backup = copy.deepcopy(used_child)
    print('used_child_backup = {}'.format(used_child_backup))                       
    
    return R_child, F_child, used_child, lm, R_isom_p_child, \
           R_isom_p_child_backup, used_child_backup, R_backup_child, F_backup_child
