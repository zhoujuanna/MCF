
##input 
##up1 = {'x2': 'b3', 'x4': 'b2', 'x6': 'b1'}
##up2 = [{'x1': 'b1', 'x3': 'b2'}, {'x3': 'b1', 'x1': 'b2'}, {'x1': 'b7', 'x3': 'b5'}, {'x3': 'b1', 'x1': 'b5'}]
##对于字典列表up2中的每一个元素child，\
##如果该元素child任意一个键值对kv的值v已出现在字典up1中，\
##但是键值对kv的键与字典up1中值等于v的键不相等，\
##那么把元素child从up2中删除。\
##输出字典列表up2
##output - [{'x1': 'b7', 'x3': 'b5'}]

def cons_up12(up1, up2):
    up1_values = set(up1.values())

    # 用一个函数来检查每个子字典是否符合条件，然后筛选出符合条件的子字典
    def is_valid(child):
        for key, val in child.items():
            if val in up1_values and key != up1.get(val):
                return False
        return True

    up2 = [child for child in up2 if is_valid(child)]
##    print(up2)
    return up2

##print(cons_up12(up1, up2))
