#!/user/bin/env python3
# -*- coding: utf-8 -*-

#!/user/bin/env python3
# -*- coding: utf-8 -*-
import pymongo as pymongo

# 1、连接mongodb
client = pymongo.MongoClient('mongodb://localhost:27017/')
# client = pymongo.MongoClient(host='localhost', port=27017) # 跟上面的语句是同个用途，不同的参数传递方式

# 2、指定使用的数据库 Database
databaseName = "dataset"
db = client[databaseName]

# 3、指定使用的集合 Collection
collectionName = "Tasks"
collection = db[collectionName]

# 4、插入数据
dataset1 = {
    "TaskName": "single_task_special",
    "Task_ID": "1823301339096780800",
    "RuleNames": "海阔天空",
    "Status": "ENABLED"
}

collection.insert_one(dataset1) # 插入一条数据

datalist = [
    {"TaskName": "test_dataset_0820-1", "Task_ID": "1823301339096780800-1", "RuleNames": ["服务用语-发送开场白1"], "Status": "ENABLED"},
    {"TaskName": "test_dataset_0820-2", "Task_ID": "1823301339096780800-2", "RuleNames": ["服务用语-发送开场白2"], "Status": "ENABLED"},
    {"TaskName": "test_dataset_0820-3", "Task_ID": "1823301339096780800-3", "RuleNames": ["服务用语-发送开场白3"], "Status": "ENABLED"},
    {"TaskName": "test_dataset_0820-4", "Task_ID": "1823301339096780800-4", "RuleNames": ["服务用语-发送开场白4"], "Status": "ENABLED"},
]
collection.insert_many(datalist)    # 插入多条数据

# 5、查询数据
# 5.1 查询一条数据。默认查询第一条数据
find_one = collection.find_one()
print(find_one)

# 5.2 查询所有数据 => 等同于SELECT *
# find_all = collection.find()
# for data in find_all:
#     print(data)

# 5.3 使用find查询指定筛选条件
# query = {"TaskName": "test_dataset_0820"}
# find_filter = collection.find(query)
# for data in find_filter:
#     print(data)

# 5.4 高级查询 - 使用正则表达式查询
# myquery = {"name": {"$TaskName": "^test"}}    # 查询TaskName以test开头
#
# mydoc = collection.find(myquery)
# for data in mydoc:
#     print(data)

# 6、修改数据
# 6.1 修改一条数据的值
myquery = {"RuleNames": "海阔天空"}
new_values = {"$set": {"RuleNames": "海阔天空1111"}}

collection.update_one(myquery, new_values)

# 6.2 修改多条数据的值
myquery = {"name": {"$regex": "^F"}}
new_values = {"$set": {"alexa": "123"}}

x = collection.update_many(myquery, new_values)