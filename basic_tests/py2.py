#!/usr/bin/python
#coding:utf-8

class Demo(object):
    def __init__(self,x):
        self.x = x

    @classmethod
    def addone(self, x):
        return x+1

    @staticmethod
    def addtwo(x):
        return x+2

    def addthree(self, x):
        return x+3

def main():
    print Demo.addone(2)
    print Demo.addtwo(2)

    #print Demo.addthree(2) #Error
    demo = Demo(2)
    print demo.addthree(2)


if __name__ == '__main__':
    main()
