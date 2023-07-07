# 打开文件
import json
import os, shutil
import time
with open("config.json", "r",encoding="utf-8") as f:
    config_dict = json.loads(f.read())
    # print(config_dict)

# 用户名输入
botUserName = input("请输入需要创建机器人的用户名称(英文或者拼音): ")
if botUserName == "":
    print("没有输入,程序退出")

#openai的apiKey输入
openApiKey = input("请输入openai的apikey: ")
if openApiKey == "":
    print("没有输入,程序退出")

# 进行apiKey赋值处理
config_dict["open_ai_api_key"] = openApiKey

# 生成新的配置文件到代码目录chatpt-on-wechat
with open("chatgpt-on-wechat/config.json","w",encoding="utf-8") as f:
    f.write(json.dumps(config_dict,ensure_ascii=False))
    print("新配置文件写入完成")

# 存在删除
if os.path.exists("botUser/{}".format(botUserName)):
    shutil.rmtree("botUser/{}".format(botUserName))

# 文件夹copy到个人用户启动文件夹
shutil.copytree("chatgpt-on-wechat","botUser/{}/chatgpt-on-wechat".format(botUserName))

# 判断容器是否存在
docker_id = os.popen("docker ps -a|grep %s|grep -v 'grep' |awk '{print $1}'"%(botUserName)).read().strip()
if docker_id != "":
    stop_status=os.system("docker stop {}".format(botUserName))
    if stop_status!=0:
        print("关闭历史容器失败请手动关闭再重新运行脚本")
        raise "关闭历史容器异常"
    rm_status=os.system("docker rm {}".format(botUserName))
    if rm_status!=0:
        print("删除历史容器失败请手动删除再重新运行脚本")
        raise "删除历史容器异常"

# docker ps -a|grep testpython|grep -v 'grep' |awk '{print $1}'
# 启动容器的命令
# 这里cmd还没有替换
cmd = 'docker run -itd --name {} -v /root/python/botUser/{}/chatgpt-on-wechat:/root/chatgpt-on-wechat  chatgpt/wechat/env:latest  bash -c "cd /root/chatgpt-on-wechat/scripts && bash start.sh"'.format(botUserName,botUserName)
# 执行创建命令
code  = os.system(cmd)
if code==0:
    print("用户容器创建成功")
    time.sleep(12)
    # 显示出二维码
    os.system("cat /root/python/botUser/{}/chatgpt-on-wechat/nohup.out".format(botUserName))

# 启动容器的命令
# docker run -itd --name testpython -v /root/python/botUser/{}/chatgpt-on-wechat:/root/chatgpt-on-wechat  58d8fd9767c5  bash -c "cd /root/chatgpt-on-wechat/scripts && bash start.sh"
