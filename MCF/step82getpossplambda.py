def find_matching_indices(str1, str2):

    def extract_indices(s):
        indices = {}
        params = s[s.find("(")+1:s.find(")")].split(",")
##        print('params = ', params)
        for i, param in enumerate(params):
            indices[param] = i
        return indices

    indices1 = extract_indices(str1)
##    print('indices1= ', indices1)
    indices2 = extract_indices(str2)
##    print('indices2= ', indices2)

    matching_params = []
    nomatching_params = []
    for param in indices1:
##        print('\nparam = ', param)
##        print('in for indices1.get(param, None) = ', indices1.get(param, None))
        if indices1.get(param, None) == indices2.get(param, None):
##            print('para m = ', param)
            matching_params.append(param)
        else:
##          根据值找自字典indices2的键
            k = next((key for key,val in indices2.items( ) if val == indices1[param]),None)
            nomatching_params.append({param:k})

##    print('matching_params = ', matching_params)
##    print('nomatching_params = ', nomatching_params)
    if len(matching_params) == 2:
        return nomatching_params
    else:
        return []

    
if __name__ == '__main__':    
    
    chr_litsr = 'P1(a2,a5,x1)'
    chr_litsf = 'P1(a2,a5,a4)'
    result = find_matching_indices(chr_litsr, chr_litsf)
    print('result = ', result)

