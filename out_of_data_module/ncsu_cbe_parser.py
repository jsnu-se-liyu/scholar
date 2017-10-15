#coding:utf-8
"""
@file:      ncsu_cbe_parser
@author:    YuLi
@contact:   1595230056@qq.com
@python:    3.6.2
@editor:    PyCharm
@create:    2017/10/15 22:46
@description:
            --
"""
from utils.connection import *
from utils.set_value import *
def web1():
    html=fetch("https://www.cbe.ncsu.edu/directory/faculty/")
    main_class=extract("//div[@class='directory_entry']",html,True)
    for i in main_class[:]:
        name=extract("//p[@class='name']/b/text()",str(etree.tostring(i)))
        #print(name)
        website=extract("//div[@class='person_info']/a/@href",str(etree.tostring(i)))
        #print(website )
        email=extract("//p[@class='email']/text()",str(etree.tostring(i)))
        #print(email)
        org='NC STATE UNIVERSITY'
        major=extract("//*[@id='main-content']/div/div/div[2]/header/div/div/p/text()",html)
        avatar=extract("//img/@src",str(etree.tostring(i)))
        # print(major)
        # print(avatar)
        print(set_value(name,website,email,org,major,avatar))
web1()