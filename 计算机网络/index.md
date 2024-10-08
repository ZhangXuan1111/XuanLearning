# 1、OSI 七层模型 以及 TCP/IP四层模型
## OSI
- 应用层 -- HTTP DNS FTP SMTP
- 表示层 
- 会话层
- 传输层 -- TCP UDP
- 网络层 -- IP
- 数据链路层
- 物理层
## TCP/IP
- 应用层
- 传输层
- 网络层
- 网络接口层

# 2、浏览器输入URL到显示网页的过程
- DNS解析：将域名解析为服务器IP
- TCP连接：三次握手
- 发送HTTP请求
- 服务器处理请求信息
- 浏览器接收http响应：渲染、解析css、js等
- 断开连接：四次挥手

# 3、DNS域名解析过程
- 检查浏览器缓存，是否能找到对应的ip
- 请求根服务器，返回顶级域名服务器
- 请求顶级域名服务器，返回权威域名服务器
- 请求权威域名服务器，返回对应的ip地址

# 4、状态码
- 1xx
- 2xx
- 3xx：重定向
  - 301：请求资源永久移动，返回新url
  - 302：请求资源暂时移动，返回原始url
- 4xx
  - 400：
  - 401：请求需要认证
  - 403：服务器拒绝执行
  - 404：请求的资源不存在
- 5xx
  - 500：服务器内部错误

# 5、HTTP有哪些请求方式
- GET
- POST
- DELETE
- PUT

> GET方法可以实现写操作吗？-- 可以，但是不推荐
> 
# 6、Http 和 Https的区别？
- 默认端口：http - 80；https - 443
- http - 明文传输，容易被窃取/篡改；https - 加密传输SSL，安全

# 7、https传输流程是怎样？
- 客户端发送https请求
- 服务器收到请求后，发送自己的数字证书，包含公钥、颁发机构等信息
- 客户端收到服务器的数字证书后，先验证证书的合法性。如果合法，会生成一个随机秘钥，用公钥加密发送给服务器
- 服务器收到会话秘钥后，用私钥解密

> 客户端和服务器通过这种加密解密的方式(客户端用公钥加密，服务器用私钥解密)，保证通信内容的安全性
> 
# 7、Session 和 Cookie的区别
- 存储位置不同：Cookie保存在客户端浏览器；Session保存在服务端
- 存储数据类型不同：cookie - AScII，session-任意数据类型
- 隐私策略不同：cookie容易被窃取；session安全性较高
- 存储大小不同：cookie不能超过4k；session更多

# 8、TCP三次握手
- 客户端发请求，SYN=1，seq=x（验证客户端的发送请求的能力
- 服务器收到请求，回复SYN+ACK包 (SYN=1;ACK=1;seq=y;ack=x+1 =》验证服务器接收请求的能力

# 9、TCP四次挥手
- 客户端发送FIN中断请求，表示不再有数据传输
- 服务器收到请求后发送ACK=1，表示确认已收到客户端的FIN请求
- 服务器向客户端发送FIN请求，表示没有数据再传输了
- 客户端向服务器发送ACK

# 10、TCP如何保证可靠连接
- 连接管理：三次握手 & 四次挥手
- 校验和：
- 序列号/确认应答：
- 流量控制：TCP连接的每一方都有固定大小的缓冲空间，只能发送接收方所能容纳范围内的数据；滑动窗口实现流量控制
- 最大消息长度
- 超时重传
- 拥塞控制：避免由于网络拥堵导致数据丢包问题，引入了慢启动机制 -- 即先传输一小部分数据(探探路)，再决定按照多大的流量来传输数据
- 
- 客户端收到服务器的SYN+ACK包，回复一个ACK包，完成三次握手
