"""
    文件读取相关的类定义
"""
import json

from data_define import Record


# 定义一个文件读取的抽象类作为顶层设计，用于确定有哪些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:
        # 读文文件的数据，读取到的每条数据都转为 Record 对象，然后将它们转为 list 返回
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path    # 定义成员变量用于几率文件的路径

    # 复写父类的方法
    def read_data(self) -> list[Record]:
        file = open(self.path, "r", encoding="UTF-8")
        data_lines = file.readlines()
        file.close()
        record_list = []
        for data_line in data_lines:
            data_line = data_line.strip()   # 消除每一行数据中的 \n
            data_list = data_line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path    # 定义成员变量用于几率文件的路径

    # 复写父类的方法
    def read_data(self) -> list[Record]:
        file = open(self.path, "r", encoding="UTF-8")
        data_lines = file.readlines()
        file.close()
        record_list = []
        for data_line in data_lines:
            data_dict = json.loads(data_line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)
        return record_list


if __name__ == '__main__':
    # text_file = TextFileReader("/Users/terry/Documents/Workspace/PythonProjects/Python/data/销售.txt")
    # text_file.read_data()
    text_file = JsonFileReader("/Users/terry/Documents/Workspace/PythonProjects/Python/data/销售的JSON.txt")
    text_file.read_data()



