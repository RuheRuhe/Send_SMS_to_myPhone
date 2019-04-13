#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Ruhr's SMS
# @Author : chariebin

from twilio.rest import Client
import time

# Your Account SID from twilio.com/console
#account_sid = "AC51f39bf7a01cefbad88e4aeaf22a1b109276"
account_sid = "ACa6899234d014d2f1043416b609b4eb35620a"
# Your Auth Token from twilio.com/console
#auth_token  = "991ecfa4dd1b05e0e0acf04e59018913"
auth_token  = "d71ef640b5e25561652721e5e476f7e1"
client = Client(account_sid, auth_token)

message = client.messages.create(
    #to="+86155****1942",     # 接受短信的手机号，也就是注册界面验证过的那个自己的手机号，注意 写中国区号  +86
    to="+86187****8220",
    #from_="+1 2038720992",   # 发送短信的美国手机号  区号 +1
    from_="+12015540923",
    #body="生活总是让我们遍体鳞伤，但到后来，那些受伤的地方一定会变成我们最强壮的地方。")
    #body="“OK”可以说是世界上用得最多、知道最多的词语之一。事实上，“OK”历史已很悠久。在貌似简单的外形背后，“OK”也有许多故事。")
    #body="没有阳光，就听风吹，看雨落；没有鲜花，就嗅泥土的芬芳，效小草的坚强；没有掌声，就享受生活的平淡，独处的清宁。心灵有家，生命才会有路，守好心，走好路，珍惜最真的情感，感受最近的幸福，享受最美的心情。")
    #body="陪伴，是两情相悦的一种习惯；懂得，是两心互通的一种眷恋。相聚的时光总太短，走得最快的不是时间，而是两个人在一起时的快乐。人，总要有一个家遮风避雨；心，总要有一个港湾休憩靠岸。因为懂得，所以包容；因为懂得，所以心同。最长久的情，是平淡中的不离不弃；最贴心的暖，是风雨中的相依相伴。")
    #body="注意保暖，中午记得提前订外卖噢")
    #body="我不喜欢这世界，只喜欢你。不偏不倚，刚好是你")
    #body="朝夕是你;白天你是我最美的念想，夜晚你是我最美的梦境，而当你和我在一起时，是我最美好的时刻。")
    body = "Am Tag bist du mein schönster Gedanke, in der Nacht bist du mein schönster Traum, und wenn du bei mir bist - der schönste Moment. ")
print(message.sid)
print(message.body)
print(time.clock())