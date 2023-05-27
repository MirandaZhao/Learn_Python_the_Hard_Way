#复习各种符号

#关键字
#assert: 断言某东西为真：assert False, "Error!"
#break：立即停止循环：while True: break
#continue: 停止当前循环的后续步骤，再做一次循环：while True: continue
#del: 从字典中删除：del X[Y]
#except: 如发生异常，运行此处代码：except ValueError, e: print(e)
#exec: 将字符串作为python脚本运行：finally: pass
#global: 声明全局变量：global # X
#in: for循环的一部分，也可以X是否在Y中的条件判断：for X in Y: pass以及 1 in [1] == True
#lambda: 创建短匿名函数  s = lambda y: y ** y; s(3)
#pass: 表示空代码块：def empty(): pass
#raise: 出错后引发异常：raise ValueError("No")
#return: 返回值并退出函数：def X(): return Y
#yield: 暂停函数，返回到调用函数的代码中: def X(): yield y; X().next()

#数据类型：
#booleen
#strings: x = 'hello'
#lists: j = [1,2,3,4]
#dicts: e = {'x':1, 'y':2}

#转义字符：
#\":"
#\n:换行符
#\r:回车
#\t:制表符

#老式字符串格式：
#%d/ %i: 十进制整数  "%d" % 45 = '45'

#运算符:
#**: 幂
#//: 除后向下取整
#%：求余数： 2 % 4 = 2
#{}: {'x':5, 'y':10}
#@修饰器符：@classmethod
