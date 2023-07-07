# 自定义docker批量化部署脚本

### 食用方法
* 环境要求
  * linux 环境支持bash
  * python3任意版本
  * docker.io或者docker.ce
* 运行方法
  * 上传python.zip 到/root目录
  * 解压项目到/root目录下,解压完成后项目路径市/root/python/....
  * docker配置镜像源 vim /etc/docker/daemon.json 复制粘贴内容入下 {
  "registry-mirrors":["https://yxzrazem.mirror.aliyuncs.com"]
}
  * systemct restart docker 让配置文件生效
  * cd /root 编译生成部署使用的环境镜像 docker build -t chatgpt/wechat/env:latest .
  * 替换/root/python下的chatgpt-on-wechat代码文件夹（换成实际项目使用的）
  * config.json 复制一份当前实际项目部署使用配置文件，后面部署会根据此配置文件自动生成其他用户配置
  * 运行bash addBot.sh生成新用户部署


### 功能说明

* 通过python封装liunx和docker命令实现chatgpt-on-wechat 批量化部署
* 输入用户名称（拼音或者英文）
* 输入为用户分配的openaikey

### 系统说明

* 原始项目chatgpt-on-wechat

* docker环境 docker.io或者docker.ce

* chatgpt-on-wechat的最小docker环境镜像

### 补充说明
* 需要将项目压缩包解压到linux系统，解压后路径应该是 /root/python/.....
* cd /root/python 目录 编译环境镜像 docker build -t chatgpt/wechat/env:latest  .
* botUser下放着所有创建用户的项目源码
* chatgpt-on-wechat 官方源码或者二次开发的源码
* config.json 配置文件范例,所有的不变参数默认都需要配置完成,需要改变的参数值随意填充
* addBot.sh 创建一个机器人的脚本运行方法 bash addBot.sh 创建的用户名必须是唯一的
* 程序运行完成后二维码自动输出到控制台查看

