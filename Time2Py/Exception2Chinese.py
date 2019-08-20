# -*- coding: utf-8 -*-

def trans_exception_to_chinese(exce_str):
	exce_list = exce_str.strip("\n").split("\n")
	length = len(exce_list)
	if length < 1:
		return exce_str	
	exce_list[0] = exce_list[0].replace("Traceback (most recent call last):", "具体错误情况如下：")
	exce_list[length -1] = trans_exception_details(exce_list[length - 1])
	for i in range(0, length-1):
		# exce_list[i] = exce_list[i].replace("File", "文件")
		pos = exce_list[i].find("line")
		pos = 0 if pos == -1 else pos
		if i == 0:
			exce_list[i] = exce_list[i][pos:]
		else:
			exce_list[i] = "  " + exce_list[i][pos:]
		exce_list[i] = exce_list[i].replace("line", "行数")
		exce_list[i] = exce_list[i].replace(", in <", ", 在 <")

	exce_str = "\n".join(exce_list)
	return exce_str + "\n"


def trans_exception_details(err):

	err = err.replace("SyntaxError", "语法错误")
	err = err.replace("invalid syntax", "无效的语法")
	err = err.replace("NameError", "命名错误")
	err = err.replace(" name ", " 名字 ")
	err = err.replace("is not defined", "没有声明(定义)")
	err = err.replace("ZeroDivisionError", "除0错误")
	err = err.replace("division by zero", "除数不能为0")
	err = err.replace("IndexError", "索引错误")
	err = err.replace("list index out of range", "索引超出范围")
	err = err.replace("KeyError", "关键字错误")
	err = err.replace("IOError", "输入输出错误")
	err = err.replace("FileNotFoundError", "未找到文件错误")
	err = err.replace("Errno", "错误编号")
	err = err.replace("No such file or directory", "没有这个文件或文件夹")
	err = err.replace("AttributeError", "属性错误")
	err = err.replace("object has no attribute", "对象没有属性")
	err = err.replace("ValueError", "数值错误")
	err = err.replace("invalid literal for int() with base 10", "int()内文本无效")
	err = err.replace("TypeError", "类型错误")
	err = err.replace("must be", "应该是")
	err = err.replace(", not ", ", 不是 ")
	err = err.replace("Can't convert", "不能转换")
	err = err.replace("object to", "对象到")
	err = err.replace("implicitly", "")
	err = err.replace("AssertionError", "断言错误")
	err = err.replace("MemoryError", "内存耗尽错误")
	err = err.replace("NotImplementedError", "方法没实现错误")
	err = err.replace("LookupError", "键、值不存在错误")
	err = err.replace("StandardError ", "标准异常")
	err = err.replace("ImportError", "导入异常")
	err = err.replace("UnboundLocalError", "试图访问一个还未被设置的局部变量错误")
	err = err.replace("can't assign to function call", "不能对函数调用进行赋值")
	return err


if __name__ == '__main__':

	try:
				
		a = "aa" + 10
	except:
		import traceback, sys
		# traceback.print_exc()  # 打印异常信息
    
		exc_type, exc_value, exc_traceback = sys.exc_info()
		error = traceback.format_exception(exc_type, exc_value, exc_traceback)  # 将异常信息转为字符串
		error = "".join(error)
		print(error)
		print()
		error = trans_exception_to_chinese(error)
		print(error)
