import time
import os
import shutil
print(time.time())

print(time.asctime(time.localtime(time.time())))
print(os.cpu_count())

from milvus import Milvus, IndexType, MetricType, Status

# milvus = Milvus(host='localhost', port='19530')
# milvus = Milvus(uri='tcp://localhost:19530')

shutil.copy("/home/ybsun/data/1.txt", "/home/ybsun/data/2.txt")

root_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# print(os.path.dirname("/home/ybsun/.ssh/id_rsa.pub"))
print(root_path)
category = os.listdir(root_path)
category_path = os.path.join(root_path, category[0])
print(os.listdir(category_path))

path = "/home/ybsun/milvus_db/embedding.py"
new_path = os.path.dirname(os.path.dirname(path))
print(new_path)


collection_name = "abc"
print("Collection {} existed ,now deleting it".format(collection_name))

a = range(100//3)
print(a)