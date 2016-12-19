#! /usr/local/python3
#! -*- conding:utf-8 _*_

__author__ = 'z'

#测试插入数据

import orm
import asyncio
from models import User, Blog, Comment

@asyncio.coroutine
def test():
	yield from orm.create_pool(loop, user='wwwdata', password='wwwdata', database='awesome', host='192.168.182.132')
	u = User(name='Test', email='test5@example.com', passwd='123', image='about:blank'
			)	
	yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
