# RuijieAutoLogin
可以实现的功能：

  自动登入锐捷认证的校园网(废话)

  如果没有设备连接wifi则登出校园网并等待设备连接

  登入后每25秒发一次心跳包(指ping谷歌的web)保持在线，如果ping没了则会重连


使用方法：python RuijieAutoLogin.py user password

适用于openwrt(其他设备没测试）

需要在代码里设置你自己的Clien服务端所用的网卡以做设备检测（就是你wifi服务端用的网卡名,可以用命令iwinfo查看）


#其他readme都在代码注释里

