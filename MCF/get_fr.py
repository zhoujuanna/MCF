import random, itertools
##生成公式（文字数、变量数，每个文字中的变量数- 随机生成）

##-----------------

##input - 
##nv (N = количество переменных в формуле 10-50) = 5, \
##nl (L = количество литералов 15-100) = 3\
##np (T = количество аргументов у предиката 3-10)\
##获取文字
##output - [('x25', 'x27', 'x31'), ('x43', 'x27', 'x48'), ('x25', 'x31', 'x48')]

def pr_frm(nv, nl, np):
    variables = []    
##随机生成nv个不相同的整数,整数的取值范围是1~50。
##    print('nv = ', nv)
    r = range(1, nv+1)
##    print('len(r) = ', len(r))
    if nv <= len(r):
        unique_numbers = random.sample(r, nv)
    else:
        unique_numbers = []
##    print('unique_numbers = ', unique_numbers)        

    for i in range(len(unique_numbers)):
##        dg = random.randint(1, 50)
    ##    print('x'+str(dg))
        variables.append('x'+str(unique_numbers[i]))
##    print('variables = ', variables)

    selection = []
    count = 1

    # 任意挑选np个元素放到1个组中
    literals = itertools.combinations(variables, np)
##    print('literals = ', literals)
    for literal in literals:
        if count <= nl:
            selection.append(literal)
##    print('selection = ', selection)
            count += 1
        else:
            break
    
##    print('nl = ', nl)
##    # 从列表literals中随机取出nl个元素    
##    random_selection = random.sample(literals, nl)
##    print('random_selection = ', random_selection)

    return selection

##-----------------

##input - nv = 5, nl = 4, np =3, name_prd = 'P'
##把由函数pr_frm(nv, nl, np)得到的结果\
##formula_pr = [('x34', 'x37', 'x22'), ('x34', 'x20', 'x18'), ('x37', 'x22', 'x18'), ('x37', 'x20', 'x18')]\
##+谓词名称name_prd转换成公式形式。
##output -P(x23, x15, x40)&P(x15, x43, x40)&P(x23, x48, x40)&P(x23, x48, x43)

def get_frm(nv, nl, np, name_prd):
    formula_pr = pr_frm(nv, nl, np)
##    print('formula_pr =', formula_pr)
    for i in range(len(formula_pr)):
        formula_pr[i] = str(formula_pr[i]).replace("'", "") ##删引号
        formula_pr[i] = str(formula_pr[i]).replace(" ", "") ##删空格
    formatted_formula = [name_prd + item for item in formula_pr]
    formula = '&'.join(formatted_formula)    
    return formula

##-----------------

##input -
##nf - number of formulas公式数量 = 2
##获取nf个公式
##output -
##formulas =  ['P1(x5,x14,x22)&...&P1(x5,x23,x1)', 'P1(x5,x6,x3)&...&P1(x5,x6,x10)']
def get_formulas(nf, np, nv, nl):
    formulas = []
    for i in range(nf):
       
##        np = random.randint(3, 10)
##        nv = random.randint(10, 50)  #(10,50)
##        nl = random.randint(15, 100)    #(15-100)        
##        np = 4
##        nv = 12
##        nl = 25

##        print("\nnp (T = количество аргументов у предиката 3-10) = {} \
##\nnv (N = количество переменных в формуле 10-50) = {} \
##\nnl (L = количество литералов 15-100) = {}".format(np,nv,nl) )
        formula = get_frm(nv, nl, np, 'P1')
##        print('formula = ', formula)
        formulas.append(formula)
##    print('formulas = ', formulas)
    return formulas
    
##-----------------

def main():
    formulas = get_formulas(10,4,12,25)
    print('formulas = ', formulas)

##-----------------
    
if __name__ == '__main__':    
    main()
    
