# 产生一个随机整数
# 让使用者猜
# 猜对 印出“终于猜对了”
# 猜错 告诉他 比答案大/小

import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # 等于 count = count + 1
	num = input("请猜数字")
	num = int(num)
	if num == r:
		print('终于猜对了')
		print('这是你的第', count , '次')
		break
	elif num < r:
		print('比答案小')
	else:
		print('比答案大')
	print('这是你猜的第', count , '次')
