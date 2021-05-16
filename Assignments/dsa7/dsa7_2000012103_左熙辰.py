def knapsack(treasure, maxw):
    """ 博物馆大盗问题/背包问题
    输入：
        treasure: 一个字典列表，列表中的每个元素为key值为'w'和'v'的字典，分别代表物品的重量和价值 
        maxw: 一个整数，代表最大承重
    输出：
        一个二元组。
        第一项为一个列表，代表所选取的最高总价值的宝物的序号，可以用testKnapsack来测试
        第二项为一个整数，代表最高总价值
    要求使用用伪多项式时间的算法
    """
    dplist = []
    treasurelist = []
    for _ in range(len(treasure) + 1):
        dplist.append([0] * (maxw + 1))
    for i in range(1, len(treasure) + 1):
        for j in range(1, maxw + 1):
            if treasure[i-1]['w'] > j:
                dplist[i][j] = dplist[i-1][j]
            elif dplist[i-1][j-treasure[i-1]['w']] + treasure[i-1]['v'] > dplist[i-1][j]:
                dplist[i][j] = dplist[i-1][j-treasure[i-1]['w']] + treasure[i-1]['v']
            else:
                dplist[i][j] = dplist[i-1][j]
    j = maxw
    for i in reversed(range(1, len(treasure)+1)):
        if dplist[i][j] > dplist[i-1][j]:
            treasurelist.append(i-1)
            j -= treasure[i-1]['w']
    """
    for i in range(len(treasure)+1):
        for j in range(maxw+1):
            print(dplist[i][j], end=" ")
        print()
    """
    treasurelist.reverse()
    return treasurelist, dplist[len(treasure)][maxw]

def editDistance(word1, word2):
    """ 编辑距离
    输入：
        word1: 源单词，字符串
        word2: 目标单词，字符串
    输出：
        一个三元组。
        第一项为一个整数，代表从源单词变到目标单词所需要的最小编辑距离
        第二项为一个列表，代表编辑操作过程，'insert'代表插入，'delete'代表删除，'copy'代表复制。操作过程按照对word1的操作顺序排列。
            第二项里每个元素为二元组(operation, character)，operation代表操作类型，character代表待操作的字符
            若为插入操作，character为新加入的字符；若为删除或复制操作，character为空字符串''
            可以用testEditDistance函数来进行测试
        第三项为一个整数，代表编辑操作总得分
    要求时间复杂度为O(m x n)，m、n为word1和word2的长度
    """
    res = []
    for _ in range(len(word1) + 1):
        res.append([0] * (len(word2) + 1))
    for i in range(1, len(word1)+1):
        res[i][0] = res[i-1][0]+20
    for j in range(1, len(word2)+1):
        res[0][j] = res[0][j-1]+20
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2)+1):
            if word1[i-1] == word2[j-1]:
                res[i][j] = min([res[i-1][j-1]+5, res[i-1][j]+20, res[i][j-1]+20])
            else:
                res[i][j] = min([res[i-1][j]+20, res[i][j-1]+20])
    # for i in range(len(word1)+1):
    #     for j in range(len(word2)+1):
    #         print(res[i][j], end=" ")
    #     print()
    j = len(word2)
    i = len(word1)
    operatelist = []
    dist = 0
    while i > 0:
        if res[i][j] - 20 == res[i][j-1]:
            operatelist.append(('delete', f'{word2[j-1]}'))
            j -= 1
        elif res[i][j] - 20 == res[i-1][j]:
            operatelist.append(('insert', f'{word1[i - 1]}'))
            i -= 1
        else:
            operatelist.append(('copy', ''))
            j -= 1
            i -= 1
        dist += 1

        operatelist.reverse()
    return dist,operatelist , res[len(word1)][len(word2)]

def testKnapsack(treasure, maxw, selected_treasure_index, maxv):
    """ 博物馆大盗问题/背包问题的测试函数
    输入：
        treasure: 一个字典列表，列表中的每个元素为key值为'w'和'v'的字典，分别代表物品的重量和价值 
        maxw: 一个整数，代表最大承重
        selected_treasure_index:选取的宝物下标
        maxv：选取的宝物价值
    输出：
        布尔变量，True代表通过，False代表不通过
    """
    v = 0
    w = 0
    for i in selected_treasure_index:
        v += treasure[i]['v']
        w += treasure[i]['w']
    if v == maxv and w <= maxw:
        return True
    else:
        return False


def testEditDistance(word1, word2, operations):
    """ 根据编辑操作过程来操作单词
    输入：
        word1: 源单词，字符串
        word2: 目标单词，字符串
        operations：编辑操作过程
    输出：
        若根据编辑操作过程来操作word1使其和word2相同，则输出True，否则为False
    """
    pivot = 0 # 指向当前对word1操作的位置，插入操作会插入元素到此位置前，复制和删除操作会操作此位置元素
    new_str = ''

    for operation, character in operations:
        if operation == 'insert': # 插入
            new_str += character
        elif operation == 'delete': # 删除
            pivot += 1
        elif operation == 'copy': # 复制
            new_str += word1[pivot]
            pivot += 1
    return new_str == word2


def main():
    # treasure, maxw = [{'w': 2, 'v': 8}, {'w': 3, 'v': 4}, {'w': 4, 'v': 5}], 7
    # print(treasure, maxw)
    # selected_treasure_index, maxv = knapsack(treasure, maxw)
    # print(selected_treasure_index)
    # print(maxv)
    # print(testKnapsack(treasure, maxw, selected_treasure_index, maxv))
    word1, word2 = 'algorithm', 'alligator'
    dist, operations, score = editDistance(word1, word2)
    print(dist, operations, score)
    operations = [('copy', ''), ('insert', 'l'), ('copy', ''), ('insert', 'i'), ('copy', ''), ('insert', 'a'), ('insert', 't'), ('copy', ''), ('copy', ''), ('delete', ''), ('delete', ''), ('delete', ''), ('delete', '')]
    print(testEditDistance(word1, word2, operations))

if __name__ == '__main__':
    main()