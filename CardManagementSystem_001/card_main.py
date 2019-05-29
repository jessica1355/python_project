import card_tool

# 一直循环
while True:

	card_tool.show_mune()
	action_str = input("请选择希望执行的操作")
	print("你选择的操作是%s" % action_str)
	
	if action_str in ["1","2","3"]:  # 成员运算符！！！
		if action_str == "1":
			card_tool.add_card()
		elif action_str == "2":
			card_tool.show_card()
		elif action_str == "3":
			card_tool.search_card()

		
	elif action_str == "0":
		print("欢迎下次使用'名片系统'")
		break
	else:
		print("请输入0-3的数字！")