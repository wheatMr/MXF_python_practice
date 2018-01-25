# -*- coding: UTF-8 -*-
# Time : 2018/1/25 9:51
# Author : liang
# 命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city 参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:',name, 'age:', age, 'other:', kw)
person('liang',24,city='shanghai',addr='gaoxin')

