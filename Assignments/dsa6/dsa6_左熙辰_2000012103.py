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

    def printdata(self):
        for i in range(self.row):
            c = self.row - i - 1
            print("  " * c, end="")
            for j in range(len(self.data[i])):
                if j < len(self.data[i]):
                    print(str(self.data[i][j]).center(4), end="")
                else:
                    print(str(self.data[i][j]).center(4), end="")
            print()



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
    t.begin_fill()
    t.fillcolor("green")
    t.pencolor("green")
    t.circle(4)
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


class HibertCurve():
    def __init__(self, n, len, t = turtle):
        self.turtle = t
        self.turtle.seth(0)
        self.turtle.width(3)
        self.HelbertX(n, len)
        self.turtle.done()

    def HelbertX(self, n, len):
        if n > 0:
            # 生成列：−LF+RFR+FL−
            ## ----
            self.turtle.right(90)
            self.HelbertY(n - 1, len)
            self.turtle.forward(len)
            self.turtle.left(90)
            self.HelbertX(n - 1, len)
            self.turtle.forward(len)
            self.HelbertX(n - 1, len)
            self.turtle.left(90)
            self.turtle.forward(len)
            self.HelbertY(n - 1, len)
            self.turtle.right(90)
        else:
            pass
        """
        +RF-LFL-FR+
        """
    def HelbertY(self, n, len):
        if n > 0:
            self.turtle.left(90)
            self.HelbertX(n - 1, len)
            self.turtle.forward(len)
            self.turtle.right(90)
            self.HelbertY(n - 1, len)
            self.turtle.forward(len)
            self.HelbertY(n - 1, len)
            self.turtle.right(90)
            self.turtle.forward(len)
            self.HelbertX(n - 1, len)
            self.turtle.left(90)
        else:
            pass

def pascalTriangle(numofrow):
    pascaltriangle = PascalTriangle(numofrow)
    return pascaltriangle.printdata()


if __name__ == '__main__':
    # t = turtle
    branchlen = 100
    branchwideth = 20
    # t.seth(90)
    # tree(branchlen,branchwideth, t)
    numofrow = 6
    pascalTriangle(numofrow)
    # helbert = HibertCurve(4, 15)