import turtle
import random
import math

class PascalTriangle():
    def __init__(self, row):
        self.row = row
        self.count = 0
        self.data = []
        for i in range(row):
            self.data.append([0] * (i + 1))
            self.data[i][0] = 1
            self.data[i][-1] = 1
        self.add_num()

    def add_num(self):
        col = 0
        if self.count == self.row:
            return 0
        else:
            for i in range(self.count):
                if self.data[self.count][i] != 1:
                    self.data[self.count][i] = self.data[self.count - 1][i - 1] + self.data[self.count - 1][i]
            self.count += 1
            self.add_num()

def leaf(t):
    # t.colormode(255) # 随机生成 rgb 色值
    t.begin_fill()
    t.fillcolor("green")
    t.pencolor("green")
    t.circle(3)
    t.end_fill()

def tree(branchlen, branchwideth, t):
    if branchlen > 0 and branchwideth > 0:
        t.pensize(branchwideth)
        t.pencolor("brown")
        t.forward(branchlen)
        t.right(30)
        tree(branchlen // math.sqrt(2), branchwideth // math.sqrt(2), t)
        t.left(60)
        tree(branchlen // math.sqrt(2), branchwideth // math.sqrt(2), t)
        t.right(30)
        t.penup()
        t.backward(branchlen)
        t.pendown()
    else:
        leaf(t)

"""
    elif branchlen > 0 or branchwideth == 1:
        t.pensize(2)
        t.pencolor("green")
        t.forward(25)
        return 0
    else:
        return 0
"""


def pascalTriangle(numofrow):
    pascaltriangle = PascalTriangle(numofrow)
    return pascaltriangle.data


if __name__ == '__main__':
    t = turtle
    branchlen = 100
    branchwideth = 20
    tree(branchlen,branchwideth, t)
    numofrow = 6
    #pascalTriangle(numofrow)
