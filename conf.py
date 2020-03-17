# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "discodyer/@gh-pages"
}
# 站点设置
site_name = "Codyの杂货铺"
site_logo = "${static_prefix}LOGO.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Cody"
email = "cody23333@gmail.com"
author_homepage = "https://blog.codynet.work"
description = "即使你缩成一团 现实也不会有所改变哦"
key_words = ['Cody', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "三無計劃",
        "url": "https://www.imalan.cn",
        "brief": "熊猫小A的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/Cody2333",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GayHub",
        "url": "https://github.com/discodyer",
        "icon": "gi gi-github"
    },
    {
        "name": "Telegram",
        "url": "https://t.me/cody2333",
        "icon": "gi gi-telegram"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
