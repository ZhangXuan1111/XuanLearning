# 1、简介
关系型数据库，
# 2、内连接、外连接、交叉连接、笛卡尔积
- 内连接（inner join）：返回两个表中连接字段匹配的行。如果一个表中的行在另一个表中没有匹配的行，则这些行不会出现在查询结果中
```mysql
SELECT Employees.Name, Departments.DeptName
FROM Employees
INNER JOIN Departments ON Employees.DeptID = Departments.DeptID;
```

- 外连接（outer join）：不仅返回两个表中匹配的行，还返回左表、右表或两者中未匹配的行
```mysql
SELECT Employees.Name, Departments.DeptName
FROM Employees
LEFT OUTER JOIN Departments ON Employees.DeptID = Departments.DeptID;
```
- 交叉连接（cross join）：返回第一个表中的每一行与第二个表中的每一行的组合，这种类型的连接通常用于生成笛卡尔积
```mysql
SELECT Employees.Name, Departments.DeptName
FROM Employees
CROSS JOIN Departments;
```
- 笛卡尔积：数学中的一个概念，例如集合 A={a,b}，集合 B={0,1,2}，那么 A✖️B={<a,0>,<a,1>,<a,2>,<b,0>,<b,1>,<b,2>,}

# 3、varchar和char的区别
- varchar: 变长字符串，长度是可变的;varchar 在存取方面与 char 相反，它存取慢，因为长度不固定，但正因如此，不占据多余的空间，是时间换空间的做法
- char: 定长字符串，长度是固定;长度固定，所以存取速度要比 varchar 快很多
# 4\