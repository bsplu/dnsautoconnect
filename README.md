# dnsproxy开机连接dns

---
开机时调用service,会自动尝试连接dns服务器.找到可以链接的服务器后作为本机dns查询的服务器.

---
## 安装说明:
1. 首先要保证安装好了dnsproxy. 测试通过后才可以使用本程序.
2. 将dnscrypt-proxy-v6-python文件拷贝到/etc/ini.d文件夹下. 并更改执行权限.

  > $ sudo cp dnscrypt-proxy-v6-python /etc/ini.d
  > $ sudo chmod 755 /etc/ini.d/dnscrypt-proxy-v6-python

3. 将dnsconnect.py和dnscrypt-resolvers.csv复制到/usr/local/bin下

## 使用说明
1. 在已更改dns地址的情况下("127.0.0.1"和"::1"). 详见dnsproxy说明.
2. 开启dns
  > $ sudo service dnscrypt-proxy-v6-python start
  
  出现success表示连接成功
  
3. 关闭dns

  > $ sudo service dnscrypt-proxy-v6-python stop
  
  *注意:这时仅断开了dns服务器,如果本机的dns服务器地址仍然是"127.0.0.1"和"::1"的话,可能会出现无法上网的情况*
  
4. dns是否连接查询
 
  > $ sudo service dnscrypt-proxy-v6-python status
  
5. 重新启动
 当发现解析不了网址时,可能是dns服务器出现了问题,这时需要重启.
 先关闭,再打开即可.
