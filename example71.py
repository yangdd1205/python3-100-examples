#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 071
"""


class Student(object):
    def __init__(self):
        self.__num = 0
        self.__name = ""
        self.__score = [0, 0, 0, 0]

    def get_num(self):
        return self.__num

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_num(self, num):
        try:
            num = int(num)
            self.__num = num
        except ValueError as e:
            print("Please input a int")

    def set_score(self, score_1, score_2, score_3, score_4):
        self.__score[0] = score_1
        self.__score[1] = score_2
        self.__score[2] = score_3
        self.__score[3] = score_4


def input_stu(n):
    student_list = []
    for i in range(n):
        s = Student()
        s.set_num(input("请输入编号："))
        s.set_name(input("请输入姓名："))
        s.set_score(input("请输入成绩1："), input("请输入成绩2："), input("请输入成绩3："), input("请输入成绩4："))
        student_list.append(s)
    return student_list


def output_stu(student_list):
    for i in range(len(student_list)):
        s = student_list[i]
        print("编号：%s\t姓名：%s\t成绩[%s\t%s\t%s\t%s]" % (
            s.get_num(), s.get_name(), s.get_score()[0], s.get_score()[1], s.get_score()[2], s.get_score()[3]))


if __name__ == '__main__':
    output_stu(input_stu(1))
