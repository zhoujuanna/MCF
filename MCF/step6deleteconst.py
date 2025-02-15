##input  -
R = "P1(b1,b2,b3)&P1(b1,b2,x6)&P1(b2,x4,x6)&P1(b3,b2,b1)&P1(b2,b1,x4)"
##or R = "P1(a1,a2,a3)& P1(a1,a2,x6)&P1(a2,x4,x6)&P1(a3,a2,a1)&P1(a2,a1,x4)"
##如果该字符串R中文字中只包含常量， 那么把该文字添加到R_const中，否则添加到R_vr_cn中。
##output -  R_const = ['P1(b1,b2,b3)', 'P1(b3,b2,b1)'], \
##R_vr_cn = ['P1(b1,b2,x6)', 'P1(b2,x4,x6)', 'P1(b2,b1,x4)'])

def get_lt_vr_cn(R):
    R_const = []
    R_vr_cn = []
    for item in R:
    ##    print('\nitem = ', item)
        params = item.strip(')').split('(')[1].split(',')
##        print('params = ', params)
        if all(param[0] == 'a' or param[0] == 'b' for param in params):
            R_const.append(item)
        else:
            R_vr_cn.append(item)          

##    print(R_const, R_vr_cn)
    return R_const, R_vr_cn

##print(get_lt_vr_cn(R))


##input -
##F = "P1(b1,b2,b3)&P1(b1,b3,b5)&P1(b2,b4,b6)&P1(b3,b2,b1)&P1(b4,b5,b6)&P1(b1,b3,b2)"
##R_c = ['P1(b1,b2,b3)', 'P1(b3,b2,b1)']
##把字符串F用&符号分开。\
##如果分开后得到的内容包含在列表R_c = ['P1(b1,b2,b3)', 'P1(b3,b2,b1)']中，那么从F中删除
##output - intersection_elements = ['P1(b1,b2,b3)', 'P1(b3,b2,b1)']
##F = ['P1(b1,b3,b5)','P1(b2,b4,b6)','P1(b4,b5,b6)','P1(b1,b3,b2)']
##有可能存在这样一种状况，在R_c中只有部分元素同时在R_c和F中出现，
##这样一来输出结果intersection_elements的长度就小于初始列表R_c的长度。
def del_lt_fromF(F, R_c):    
##    split_F = F.split('&')
    new_F = [item for item in F if item not in R_c]
    intersection_elements = [item for item in F if item in R_c]  # 找出即包含在F中，也包含在R_c中的元素


##    print(new_F)
    return intersection_elements, new_F

##print(del_lt_fromF(F, R_c))


##input - 
##queue_R = ['P1(x1,x2,x3)', 'P1(x3,x2,x1)', 'P1(x10,x2,x3)']
##partial_lambda = {'x1': 'b1', 'x2': 'b2', 'x3': 'b3', 'x10': 'b9'}
##用字典中的值去替换列表中字典的键。注意字典的键必须完全匹配。\
##比如：字典partial_lambda中有键值对 'x1': 'b1'和 'x10': 'b9'，R中有P1(x10,x2,x3)，\
##那么应该用b9代替x10, 结果为 P1(b9,b2,b3)，而不是P1(b10,b2,b3)。
##output -  ['P1(b1,b2,b3)', 'P1(b3,b2,b1)', 'P1(b9,b2,b3)']

def rplc_dict(queue_R, partial_lambda):
    # 循环遍历队列中的表达式
    for i in range(len(queue_R)):
        # 循环遍历partial_lambda字典中的键值对
        for key, value in partial_lambda.items():
            # 使用正则表达式替换键值对应的值，确保只有完全匹配的键会被替换
            import re
            pattern = r'\b' + key + r'\b'  # 匹配单词边界
            queue_R[i] = re.sub(pattern, value, queue_R[i])

    # 打印替换后的队列
##    print(queue_R)
    return queue_R


##有两个列表，
##R_const = ['P1(a3,a9,a4)', 'P1(a4,a3,a9)', 'P1(a9,a4,a3)']
##F_const = ['P1(a3,a9,a4)']
##对于长度比较短的列表中的每一个元素e，\
##如果该元素e既存在于第1个列表const中，也存在于第2个列表const中，\
##那么把这个元素e添加到新列表R_isom_p中。

def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:  # 时间复杂度为O(n)
        if element in list2:  # 时间复杂度为O(m)
            common_elements.append(element)  # 时间复杂度为O(1)
    return common_elements
