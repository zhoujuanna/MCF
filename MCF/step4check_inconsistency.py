##input -
##partial_lambda = {'x1': 'b1', 'x2': 'b2', 'x3': 'b2', 'x4': 'b3'}
##output - partial_lambda = {}
##有一个字典：partial_lambda = {'x1': 'b1', 'x2': 'b2', 'x3': 'b2', 'x4': 'b3'}。\
##如果在字典partial_lambda中不同的键对应相同的值，\
##那么将字典partial_lambda设置为空。(冲突性检测)

def inconsistency_check_sk_dv(partial_lambda): ## dk_sv = differernt keys, same value

    # 使用集合来找出重复的值
    value_set = set()
    duplicate_values = set()
    for key, value in partial_lambda.items():
        if value in value_set:
            duplicate_values.add(value)
##            print('in if : duplicate_values = ', duplicate_values)
        else:
            value_set.add(value)
##            print('in else: value_set = ', value_set)

    # 如果有重复的值，则将字典设置为空
    if duplicate_values:
        partial_lambda = {}

##    print('partial_lambda = ', partial_lambda)
    return partial_lambda


##print(inconsistency_check_sk_dv(partial_lambda)) 
