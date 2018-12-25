# 产生一个随机整数
# 让使用者猜
# 猜对 印出“终于猜对了”
# 猜错 告诉他 比答案大/小

import random
r = random.randint(1, 100)
while True:
	num = input("请猜数字")
	num = int(num)
	if num == r:
		print('终于猜对了')
		break
	elif num < r:
		print('比答案小')
	else:
		print('比答案大')
		