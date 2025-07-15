# @Filename: 1_simple_factory_idiom.py
# @Author: codists
# @Created: 2025-07-15 16:52:29

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from abc import ABC, abstractmethod


class DataExtractor(ABC):
    @abstractmethod
    def extract(self):
        pass


class JSONDataExtractor(DataExtractor):
    def __init__(self, filepath: Path):
        with open(filepath) as f:
            self.data = json.load(f)

    def extract(self):
        for movie in self.data:
            print(f"- {movie['title']}")
            if director := movie.get("director"):
                print(f"   Director: {director}")
            if genre := movie.get("genre"):
                print(f"   Genre: {genre}")


#
class XMLDataExtractor(DataExtractor):
    def __init__(self, filepath: Path):
        self.tree = ET.parse(filepath)

    def extract(self):
        search_xpath = ".//person[lastName='Liar']"
        items = self.tree.findall(search_xpath)
        for item in items:
            first = item.find("firstName").text
            last = item.find("lastName").text
            print(f"- {first} {last}")
            for pn in item.find("phoneNumbers"):
                print(f"   {pn.attrib['type']}: {pn.text}")


# 简单工厂(功能是: 创建 extractor): 函数实现
# def create_extractor(case: str, base_dir: Path) -> DataExtractor:
#     if case == "json":
#         return JSONDataExtractor(base_dir / "movies.json")
#     elif case == "xml":
#         return XMLDataExtractor(base_dir / "person.xml")
#     else:
#         raise ValueError(f"Unknown extractor type: {case}")


# 简单工厂(功能是: 创建 extractor): 类实现
class DataExtractorFactory:
    @staticmethod
    def create_extractor(case: str, base_dir: Path) -> DataExtractor:
        """
        1.考虑到下面这段代码会复用，所以要抽取出来，个人觉得这是 simple factory idiom 产生的原因。如果不抽取出来就会造成很多个地方有
        if...else...的判断。
        2.假设这段代码不会复用(即只有一个地方会用到)，那么可封装也可不封装, 区别不大。不封装也就没有所谓的"simple factory idiom"了.

        :param case:
        :param base_dir:
        :return:
        """
        if case == "json":
            return JSONDataExtractor(base_dir / "movies.json")
        elif case == "xml":
            return XMLDataExtractor(base_dir / "person.xml")
        else:
            raise ValueError(f"Unknown extractor type: {case}")


# client: 调用 Factory
def extract(case: str):
    base_dir = Path(__file__).parent
    extractor = DataExtractorFactory.create_extractor(case, base_dir)
    extractor.extract()


if __name__ == "__main__":
    print("* JSON case *")
    extract(case="json")

    print("\n* XML case *")
    extract(case="xml")
