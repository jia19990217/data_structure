# encoding:utf-8
# Time:2020/10/8 17:30
# Email:1215399218@qq.com
# Author:Mr.jia
# File:数组1.PY
# Software:PyCharm


class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity  # 数组的长度
        self.size = 0  # 数组有效元素是多少

    def insert(self, index, element):
        if index < 0 or index > self.size :  # 如果插入位置小于0,那么报错
            raise IndexError('越界')
        if index >= len(self.array) or self.size == len(self.array):  # 如果插入位置大于数组的长度,那么扩容
            self.addcapacity()
        for i in range(self.size - 1, index-1, -1):  # 倒着遍历
            self.array[i + 1] = self.array[i]  # 把上一个位置的值赋值给下一个位置
        self.array[index] = element  # 把插入的值赋给插入的位置
        self.size += 1  # 有效元素加1

    # def output(self):
    #     for i in range(self.size):  # 输出
    #         print(self.array[i], end='-->')

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('越界')
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]  # 指定位置的后一个向前覆盖
        self.size -= 1  # 每次减1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2  # 容量为之前的2倍
        for i in range(self.size):
            new_array[i] = self.array[i]  # 把之前的数据放到新的容器里
        self.array = new_array  # 指定为专用空间


a = Array(10)
a.insert(0, 1)
a.insert(1, 2)
a.insert(3, 3)
print(a.array)

