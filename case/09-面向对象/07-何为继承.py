"""
    1、什么是继承

    2、继承的语法
        01）单继承
            class 类型(父类名)
                类内容体

        01）多继承
            class 类型(父类名, 父类名, 父类名, ...)
                类内容体

            对于多继承来说，如果两个类含有同名方法或者属性，那么最左边的类优先级最高，即：左边覆盖右边
"""


class Phone:
    # 序列号
    imei = None
    # 厂商
    producer = None

    def __init__(self, imei, producer):
        self.imei = imei
        self.producer = producer

    def call_by_4g(self):
        print("4g 通话")


class Phone2023(Phone):
    # 面容识别
    face_id = None

    def __init__(self, imei, producer, face_id):
        self.imei = imei
        self.producer = producer
        self.face_id = face_id

    def call_by_5g(self):
        print("5g 通话")

    def __str__(self):
        return f"imie = {self.imei}，producer = {self.producer}，face_id = {self.face_id}"


phone = Phone2023("apple101", "apple", "face101")
print(phone)
phone.call_by_4g()
phone.call_by_5g()
