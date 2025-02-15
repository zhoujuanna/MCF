import get_lt as gl


##input -   lits2us_R , lits2us_F
lits2us_R = ['P1(a2,a5,x1)', 'P1(a2,a1,x6)', 'P1(a2,a1,x1)', 'P1(a5,a1,x6)', 'P1(a1,x8,a5)', 'P1(a1,x8,a2)'] 
lits2us_F = ['P1(a1,a3,a2)', 'P1(a2,a5,a8)', 'P1(a2,a1,a8)', 'P1(a3,a5,a1)', 'P1(a5,a2,a3)', 'P1(a5,a2,a4)', 'P1(a5,a7,a2)', 'P1(a5,a10,a2)']
##先找lits_r, lits_f
##如果列表lits_r的元素的前4个元素等于lits_f的元素的前4个元素，\
##   那么把lits_r和lits_f中的元素的第5个元素作为组输出。\
##注意：如果在某个列表中的包含若干个前4个元素想等的元素，\
##把这若干个元素分别与另一个列表匹配。\
##比如：['P1(a2,a1,x6)', 'P1(a2,a1,a8)'], ['P1(a2,a1,x1)', 'P1(a2,a1,a8)'].
##output - result =  [['P1(a1,x8,a2)', 'P1(a1,a3,a2)'], ['P1(a2,a1,x6)', 'P1(a2,a1,a8)'], \
##['P1(a2,a1,x1)', 'P1(a2,a1,a8)'], ['P1(a2,a5,x1)', 'P1(a2,a5,a8)']]

def find_matching2(lits2us_R, lits2us_F):
    lits_r = gl.get_lits_Fm('&'.join(lits2us_R))
    ##lits_r = sorted(lits_r, key=lambda x: (x[1], x[3]))  # 按照第二个元素和第四个元素排序
##    print('lits_r = {} \tlen(lits_r) = {}'.format(lits_r, len(lits_r)))
    lits_f = gl.get_lits_Fm('&'.join(lits2us_F))
    ##lits_f = sorted(lits_f, key=lambda x: (x[1], x[3]))  # 按照第二个元素和第四个元素排序
##    print('lits_f = {} \tlen(lits_f) = {}'.format(lits_f, len(lits_f)))
    elements_map = {}
    matching_elements = []

    for r in lits_r:
        key = tuple(r[:4])
        if key in elements_map:
            elements_map[key].append(r[4])
        else:
            elements_map[key] = [r[4]]
##    print('\nelements_map = {}\n'.format( elements_map))

    for f in lits_f:
        key = tuple(f[:4])
##        print('key = ', key)
        if key in elements_map:
            for r_element in elements_map[key]:
                matching_elements.append([r_element, f[4]])
##                print('matching_elements = ', matching_elements)

    return matching_elements

##result = find_matching2(lits2us_R, lits2us_F)
##print('result = ', result)


