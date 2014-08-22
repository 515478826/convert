#coding=UTF-8
#将中缀表达式转换成逆波兰表达式unittest模块
#Author:Yangheng
#Email:vip@jishuniu.com

import unittest
import convert

class mytest(unittest.TestCase):
	
	#初始化工作
	def setUp(self):
		pass 
	
	#退出清理工作  
        def tearDown(self):  
                pass
       
        #具体的测试用例
        def testconvert1(self):
        	self.assertEqual(convert.onConvert('a+b*c+(d*e+f)*g'), ['a','b','c','*','+','d','e','*','f','+','g','*','+'],'test convert fail')

        def testconvert2(self):
		self.assertTrue(convert.IsSym('*'), 'test convert fail')
	
	def testconvert3(self):
		self.assertEqual(convert.Predence('+', '*'), -1,'test convert fail')

	
    
  
if __name__ =='__main__':
    unittest.main()
