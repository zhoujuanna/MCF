##input -
R_isom =  [[12, ['P1(x4,x7,x5)', 'P1(x4,x5,x1)', 'P1(x4,x6,x1)', 'P1(x4,x7,x6)', 'P1(x4,x7,x1)', 'P1(x7,x8,x4)', 'P1(x1,x4,x2)', 'P1(x2,x1,x6)', 'P1(x6,x2,x5)', 'P1(x6,x2,x4)', 'P1(x2,x6,x3)', 'P1(x2,x1,x3)'], {'x3': 'a8', 'x2': 'a2', 'x1': 'a1', 'x6': 'a5', 'x8': 'a6', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}], [15, ['P1(x4,x7,x5)', 'P1(x4,x5,x1)', 'P1(x4,x6,x1)', 'P1(x4,x7,x6)', 'P1(x4,x7,x1)', 'P1(x6,x5,x8)', 'P1(x6,x4,x8)', 'P1(x7,x8,x4)', 'P1(x8,x6,x7)', 'P1(x1,x4,x2)', 'P1(x2,x1,x6)', 'P1(x6,x2,x5)', 'P1(x6,x2,x4)', 'P1(x6,x8,x2)', 'P1(x8,x3,x7)'], {'x3': 'a7', 'x2': 'a2', 'x1': 'a1', 'x6': 'a5', 'x8': 'a10', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}], [19, ['P1(x4,x7,x5)', 'P1(x4,x5,x1)', 'P1(x4,x6,x1)', 'P1(x4,x7,x6)', 'P1(x4,x7,x1)', 'P1(x6,x5,x8)', 'P1(x6,x4,x8)', 'P1(x7,x8,x4)', 'P1(x8,x6,x7)', 'P1(x1,x4,x2)', 'P1(x2,x1,x6)', 'P1(x2,x6,x3)', 'P1(x2,x1,x3)', 'P1(x3,x2,x8)', 'P1(x6,x2,x5)', 'P1(x6,x2,x4)', 'P1(x6,x8,x2)', 'P1(x8,x3,x6)', 'P1(x8,x3,x7)'], {'x3': 'a8', 'x2': 'a2', 'x1': 'a1', 'x6': 'a5', 'x8': 'a10', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}], [5, ['P1(x4,x7,x5)', 'P1(x4,x7,x6)', 'P1(x4,x7,x1)', 'P1(x7,x8,x4)', 'P1(x1,x4,x2)'], {'x2': 'a7', 'x1': 'a5', 'x6': 'a1', 'x8': 'a6', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}], [5, ['P1(x4,x7,x5)', 'P1(x4,x7,x6)', 'P1(x4,x7,x1)', 'P1(x7,x8,x4)', 'P1(x1,x4,x2)'], {'x2': 'a10', 'x1': 'a5', 'x6': 'a1', 'x8': 'a6', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}], [6, ['P1(x4,x7,x5)', 'P1(x4,x7,x6)', 'P1(x4,x7,x1)', 'P1(x7,x8,x4)', 'P1(x8,x3,x7)', 'P1(x3,x2,x8)'], {'x2': 'a6', 'x3': 'a7', 'x1': 'a5', 'x6': 'a1', 'x8': 'a10', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}], [6, ['P1(x4,x7,x5)', 'P1(x4,x7,x6)', 'P1(x4,x7,x1)', 'P1(x7,x8,x4)', 'P1(x1,x4,x2)', 'P1(x8,x3,x7)'], {'x3': 'a8', 'x2': 'a7', 'x1': 'a5', 'x6': 'a1', 'x8': 'a10', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}]]
##对于列表R_isom中的所有的元素ele，找到ele中第1个元素的值最大的元素max。\
##把元素max的第二个元素rmax与列表R_isom中除了元素max以外其他元素ele的第二个元素rele相比，\
##如果rele中的所有元素包含在rmax中，那么从R_isom中删除元素ele。输出列表R_isom。
##output - R_isom =  [[19, ['P1(x4,x7,x5)', 'P1(x4,x5,x1)', 'P1(x4,x6,x1)', 'P1(x4,x7,x6)', 'P1(x4,x7,x1)', 'P1(x6,x5,x8)', 'P1(x6,x4,x8)', 'P1(x7,x8,x4)', 'P1(x8,x6,x7)', 'P1(x1,x4,x2)', 'P1(x2,x1,x6)', 'P1(x2,x6,x3)', 'P1(x2,x1,x3)', 'P1(x3,x2,x8)', 'P1(x6,x2,x5)', 'P1(x6,x2,x4)', 'P1(x6,x8,x2)', 'P1(x8,x3,x6)', 'P1(x8,x3,x7)'], {'x3': 'a8', 'x2': 'a2', 'x1': 'a1', 'x6': 'a5', 'x8': 'a10', 'x4': 'a3', 'x7': 'a9', 'x5': 'a4'}]]


def find_max_element(R_isom):
    max_element = max(R_isom, key=lambda x: x[0])
    return max_element

def compare_and_remove_elements(R_isom, max_element):
    rmax = set(max_element[1])
##    print('\nrmax = ',rmax)
##    print('')
    to_remove = []
    for ele in R_isom:
        if ele != max_element:
            rele = set(ele[1])
##            print('\nrele = ', rele)
            if rele.issubset(rmax):
##                print('in if rele.issubset(rmax)')
                to_remove.append(ele)
##                print('to_remove = ', to_remove)
    for ele in to_remove:
        R_isom.remove(ele)
    return R_isom



max_element = find_max_element(R_isom)
##print('max_element = ', max_element)

compare_and_remove_elements(R_isom, max_element)
##print('\nR_isom = ', R_isom)
