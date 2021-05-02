import collections


def infixToProfix(infixexpr):
    """
    中缀转前缀
    :param String Object:一个中缀表达式，字符串由英文大小写字母、数字以及+-*\()组成，中间不带空格，如"(3+4)*5-6"或者"(a-b/c)*(a/k-l)":
    :return 一个前缀表达式的字符串:
    """
    dict1 = {"+": 0, "-": 0, "*": 1, "/": 1}
    stack1 = collections.deque()
    stack2 = collections.deque()
    list1 = list(infixexpr)
    list1.reverse()
    str1 = ""
    for i in list1:
        try:
            int(i)
            stack2.append(i)
        except ValueError:
            if i in ["+", "-", "*", "/"]:
                if not (len(stack1) == 0 or stack1[-1] == ")"):
                    if dict1[i] >= dict1[stack1[-1]]:
                        stack1.append(i)
                    else:
                        stack2.append(stack1.pop())
                else:
                    stack1.append(i)
            elif i == ")":
                stack1.append(i)
            else:
                while stack1[-1] != ")":
                    stack2.append(stack1.pop())
                else:
                    stack1.pop()
    else:
        while len(stack1) != 0:
            stack2.append(stack1.pop())
        else:
            while len(stack2) != 0:
                str1 += str(stack2.pop())
    return str1


def isHtmlTagMatch(htmlFile):
    # 扩展括号匹配
    # 输入：html文档名
    # 输出：布尔变量，如果HTML文档的标记匹配，输出True，否则输出False
    stack1 = collections.deque()
    with open(htmlFile, encoding='utf8') as f:
        html = f.read()
    for i in html:
        if i == "<":
            temp = ""
            temp += i
        elif i == ">":
            temp += i
            if "/" in temp and len(stack1) != 0:
                temp = temp.replace("/", "")
                if temp == stack1[-1]:
                    stack1.pop()
            else:
                stack1.append(temp)
        else:
            temp += i
    if len(stack1) == 0:
        return True
    else:
        return False


def main():
    #infixexpr = "(3+4)*5-6"
    #print(infixToProfix(infixexpr))
    htmlFile = 'example.html'
    print(isHtmlTagMatch(htmlFile))


if __name__ == '__main__':
    main()
