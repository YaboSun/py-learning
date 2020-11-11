import fileinput

"""
文件读写两种方式
1.传统使用with open打开一个文件，并使用
"""


def file_read(file_path):
    file_content = []
    with open(file_path, 'r', encoding='utf-8') as rf:
        # 这里rf和rf.readlines()有啥区别
        for line in rf:
            file_content.append(line.strip())

    return file_content


def buffered_read(input, buffer_size):
    """
    通过固定大小的buffer读取文件内容
    :param input:
    :param buffer_size:
    :return:
    """
    buffer = []
    with fileinput.input(files=input, openhook=fileinput.hook_encoded('utf-8')) as rf:
        for str_src in rf:
            buffer.append(str_src)
            if len(buffer) >= buffer_size:
                yield buffer
                buffer = []

        if len(buffer) > 0:
            yield buffer


if __name__ == '__main__':
    file_path = "./test.txt"

    buffer_size = 100
    buffered_read(file_path, buffer_size)
