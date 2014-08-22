#coding=UTF-8
#将中缀表达式转换成逆波兰表达式
#Author:Yangheng
#Email:vip@jishuniu.com


#Judge the char is "+-*/" or not
def IsSym(ch):
	hh=['+','-','*','/']
	for i in range(len(hh)):
		if ch==hh[i]:
			return True
	return False
	
#Judge the char's priority	
def Predence(sg_1,sg_2):
	if sg_1=='(':
		return -1
	if sg_1=='+' or sg_1=='-':
		if sg_2=='*' or sg_2=='/':
			return -1
		else:
			return 0
	if sg_1=='*' or sg_1=='/':
		if sg_2=='+' or sg_2=='-':
			return 1
		else:
			return 0

#Convert infix expression to postfix expression
def onConvert(inFix):
	mm=[]
	postFix=[]
	for i in range(len(inFix)):
		fg=inFix[i]
		if fg=='(':
			mm.append(fg)
		elif fg==')':
			while mm[-1]!='(':
				postFix.append(mm.pop())
			mm.pop()  
		else:
			if IsSym(fg)==False:
				postFix.append(fg)
			else:
				while len(mm)!=0 and Predence(mm[-1],fg)>=0:
					postFix.append(mm.pop())	
				mm.append(fg)	
	while len(mm)!=0:
		postFix.append(mm.pop())
	return 	postFix

	
if __name__=="__main__":
	import string
	inFix=raw_input("Please enter an expression:")
	mResult=string.join(onConvert(inFix),'')
	print mResult
