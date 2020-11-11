import os
import xml.dom.minidom

"""
数据类型处理，将不同类型数据合并成统一的上下中英对应
"""
doc_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
data_path = os.path.join(doc_path, 'data')


def write2file():
    pass


def tsv2txt():
    pass


def xml_process(raw_xml_file):
    # with open(raw_xml_file, 'r', encoding='utf-8') as xmlin:
    dom = xml.dom.minidom.parse(raw_xml_file)
    root = dom.documentElement
    desc = dom.getElementsByTagName('description')
    pass


def combine2one():
    pass


def json2txt():
    pass
