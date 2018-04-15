#!/usr/bin/env  python3
# -*- coding: utf-8 -*-

__author__ = 'GB'
'''
for test orm,models
'''

import orm,asyncio,time
from models import User,Blog,Comment

async def test():
    await  orm.create_pool(lp,host='192.168.145.158',user='www-data',password='www-data',db='awesome')
    # for i in range(10):
    #     aa = input('请输入邮箱地址编号:')
    #     u = User(name = 'Test',email = 'test'+str(aa)+'@example.com',passwd = '1234567890',image = 'about:blank',aa=8)
    #     await u.save()
    aa =await  User.findall()
    await orm.close_pool()

    print(aa[0])

lp = asyncio.get_event_loop()
lp.run_until_complete(test())
# lp.run_forever()
lp.close()
