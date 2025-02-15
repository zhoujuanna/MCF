

# This helper function checks if there's a conflict with the existing combinations
def has_conflict(comb, kv):
    return any(k in comb or v in comb.values() for k, v in kv.items())

# This helper function adds a new non-conflicting kv pair to the existing combination
def add_to_combination(combs, kv):
    new_combs = []
    for comb in combs:
        if not has_conflict(comb, kv):
            new_comb = comb.copy()
##            print('new_comb = ', new_comb)
            new_comb.update(kv)
##            print('new_comb = ', new_comb)
            new_combs.append(new_comb)
##            print('new_combs = ', new_combs)
    return new_combs

##input - 
##up4 =  [{'x1': 'a5'}]
##up3 = [{'x6': 'a1'}, {'x1': 'a5'}, {'x1': 'a1'}, {'x6': 'a5'}, {'x8': 'a10'}, {'x8': 'a6'}]
##创建一个新的列表，使得新列表中的元素包含up3中的，但不含up4中的元素。
##output - [{'x6': 'a1'}, {'x1': 'a1'}, {'x8': 'a6'}, {'x6': 'a5'}, {'x8': 'a10'}]
def get_other_elem(up3, up4):    
    up3_set = {frozenset(item.items()) for item in up3}
    up4_set = {frozenset(item.items()) for item in up4}
    result_set = [dict(item) for item in (up3_set - up4_set)]
##    print(result_set)
    return result_set

##input -
##unique_up4 =  [{'x8': 'a6'}, {'x8': 'a6', 'x1': 'a5'}, {'x8': 'a6', 'x6': 'a1'}, {'x8': 'a6', 'x1': 'a5', 'x6': 'a1'},\
##               {'x8': 'a6', 'x6': 'a5'}, {'x8': 'a6', 'x1': 'a1'}, {'x8': 'a6', 'x6': 'a5', 'x1': 'a1'}]
##如果列表unique_up4中的元素e1包含在任意其他元素中，那么删除元素e1。
##output  - [{'x8': 'a6', 'x1': 'a5', 'x6': 'a1'}, {'x8': 'a6', 'x6': 'a5', 'x1': 'a1'}]
def delsubset(unique_up4):            
    reduced_unique_up4 = [item for item in unique_up4\
                          if not any(all(k in i.items() for k in item.items()) and i != item for i in unique_up4)]
##print('reduced_unique_up4 = ', reduced_unique_up4)
    return reduced_unique_up4






def getchild(up1, up2):

##    删除up2中与up1有冲突的键值对，删除后，为up3
    up3 = [e for e in up2 if not any(val in up1.values() or key in up1.keys() for key, val in e.items())]


    up = []   
    for i in range(len(up3)):
        # Initialize up4 with the i-th element
        up4 = [up3[i]]
##        print('\nup4 = ', up4)
        
##        如果列表up4中的元素包含在列表up的每个元素中，输出False
        if not any(all(k in item.items() for k in up4[0].items()) for item in up) == False:
##        if all(all(k in item.items() for k in up4[0].items()) for item in up):  不知道为啥，不对
            pass
        
        else:   
            # Iterate over the rest of the elements in up3
            up5 = get_other_elem(up3, up4)        
            for kv in up5:
    ##            print('\nkv = ', kv)
                # Try to add the current kv to all the existing combinations in up4
                up4.extend(add_to_combination(up4, kv))
##                print('up4 = ', up4)

            # Post-process to remove duplicates
            unique_up4 = []
            for comb in up4:
                if comb not in unique_up4:
                    unique_up4.append(comb)

##            print('unique_up4 = ', unique_up4)
            up6 = delsubset(unique_up4)
##            print('up6 = ', up6)
            
            up.extend(up6)
##            print('up = ', up)
    return up

def get_upall(up3,up1):
    up_all = []
    for u3 in up3:        
##        print({**u3, **up1})
        up_all.append({**u3, **up1})
        pass
##    print('up_all = ', up_all)
    return up_all



            
def main():
    up1 = {'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}
    up2 = [{'x6': 'a1'}, {'x1': 'a5'}, {'x1': 'a1'}, {'x6': 'a5'}, {'x8': 'a10'}, {'x8': 'a6'}]
    
    ##    print('up3 = ', up3)
    upall = get_upall(getchild(up1,up2), up1)
    print('upall = ', upall)
    
    

if __name__ == '__main__':    
    main()
