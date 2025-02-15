import re

##input
##partial_lambda = {'x1': 'b8', 'x2': 'b2', 'x3': 'b3', 'x10': 'b10'}
##R = "P1(x10,x2,x3)&P1(x1,x2,x6)&P1(x2,x4,x6)&P1(x3,x2,x1)&P1(x2,x1,x4)"
##在字符串 R中用字典partial_lambda的值代替键。\
##注意,在字符串R中找字典partial_lambda的键时，一定是完全匹配。\
##比如：字典partial_lambda中有键值对 'x1': 'b1'和 'x10': 'b9'，\
##R中有P1(x10,x2,x3)，那么应该用b9代替x10, 结果为 P1(b9,b2,b3)，而不是P1(b10,b2,b3)。
##output - P1(b10,b2,b3)&P1(b8,b2,x6)&P1(b2,x4,x6)&P1(b3,b2,b8)&P1(b2,b8,x4)

def rplc(R, partial_lambda):
    for key, value in partial_lambda.items():
        pattern = r"(?<![\w\d])" + key + r"(?![\w\d])"  # 创建匹配完整键的正则表达式模式
        R = re.sub(pattern, value, R)  # 使用正则表达式替换键为对应的值        
##    print(R)
    return  R

##print(rplc(R, partial_lambda))


