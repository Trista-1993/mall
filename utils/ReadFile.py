import os
from configparser import ConfigParser
import yaml
import xlrd
from utils.logger import logger


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData():

    def __init__(self):
        pass

    def load_yaml(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_excel(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        workbook = xlrd.open_workbook(file_path, encoding_override='utf-8')
        sheet = workbook.sheet_by_index(0)
        rows = sheet.nrows
        cols = sheet.ncols
        data = []
        for row in range(rows):
            rowdata = []
            for col in range(cols):
                cell_data = sheet.cell_value(row, col)
                rowdata.append(cell_data)
            data.append(rowdata)
        return data

    def load_json(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_ini(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data


data = ReadFileData()
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

Config_PATH = os.path.join(BASE_PATH, "data/setting.ini")
Config_Data = data.load_ini(Config_PATH)

Api_Data = data.load_yaml(os.path.join(BASE_PATH, "data/api_test_data.yml"))


if __name__ == '__main__':
    print(Config_Data)
    print(Config_Data['mall']['url'])
    print(Api_Data["test_cart_add"])

    # root_url = Config_Data['mall']['url']
    # corp_id = Config_Data['wework']['corpid']
    # corp_secret = Config_Data['wework']['corpsecret']
    # print(root_url)
    # print(corp_id)
    # print(corp_secret)
