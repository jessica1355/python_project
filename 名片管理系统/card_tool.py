# 列表变量，记录所有名片字典
card_list = []


def show_mune():
	print("*" * 50)
	print("欢迎使用【名片管理系统】")
	print("")
	print("1.新建名片")
	print("2.显示全部")
	print("3.查询名片")
	print("")
	print("0.退出系统")
	print("*" * 50)

def add_card():
	print("增加名片")
	print("-" * 50)
	name_str = input("请输入姓名")
	phone_str = input("请输入电话")
	QQ_str = input("请输入QQ")
	mail_str = input("请输入邮箱")

	new_card = {"name": name_str, 
				"phone": phone_str, 
				"QQ": QQ_str, 
				"mail": mail_str}
	card_list.append(new_card)

	print(card_list)
	print("增加%s名片成功" % name_str)
 


def show_card():
	print("显示所有名片")
	print("-" * 50)

    if len(card_list) == 0:

    print("当前没有任何的名片记录，请使用新增功能添加名片！")

    # return 可以返回一个函数的执行结果
    # 下方的代码不会被执行
    # 如果 return 后面没有任何的内容，表示会返回到调用函数的位置
    # 并且不返回任何的结果
    return

	for char1 in ["姓名", "电话", "QQ", "邮箱"]：
		print(char1, end = "\t\t")
	print("")
	print("$" * 50)

	for char2 in card_list:
		print("%s\t\t%s\t\t%s\t\t%s\t\t" % (char2["name"],
									       char2["phone"],
									       char2["QQ"],
									       char2["mail"]))	


def deal_card(card):
	print("1.修改%s的名片" % card["name"])
        print("2.删除%s的名片" % card["name"])
        print("")
		print("0.结束查找")
		print("-" * 50)
		action = input("请输入选项")
		if action == "1":
			card["name"] = input("请重新输入姓名")
			card["phone"] = input("请重新输入电话")
			card["QQ"] = input("请重新输入QQ")
			card["mail"] = input("请重新输入邮箱")
			print("修改名片成功！")
		elif action == "2":
			card_list.remove(card)
			print("删除名片成功！")


def search_card():
	print("查找名片")
	print("-" * 50)

	search_str = input("请输入要查找的姓名")
	for char3 in card_list:
		if char3["name"] != search_str:
			print("你还未存入该名片")
			return
		print("找到啦！")
		deal_card(char3)
			
		


