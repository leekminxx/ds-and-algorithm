
# 함수 선언 부분 #

def printPoly (p_x) :
    term = len (p_x) - 1 # 최고차항 숫자 = 배열 길이-1
    polyStr = "P(x) = "

    for i in range (len(px)) :
        coef = p_x[i]  # 계수

        if (coef >= 0) :
            polyStr +="+"
        polyStr = str(coef) + "x^" + str(term) + " "

        term -= 1

    return polyStr

def calcPoly (xVal, p_x) :
    retValue = 0
    term = len(p_x) - 1 # 최고차항 숫자= 배열 길이-1

    for i in range (len(p_x)) :
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue


px= [7, -4, 0, 5]          #= 7×3-4×^2 +×^1 +5×0

# 메인 코드 부분 #
if __name__== "__main__":
    
    pStr = printPoly(px)
    print(pStr)
    
    xValue = int(input ("x 값 --> "))

    pxValue = calcPoly(xValue, px)
    print (pxValue)












