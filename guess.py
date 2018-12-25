# 产生一个随机整数
# 让使用者猜
# 猜对 印出“终于猜对了”
# 猜错 告诉他 比答案大/小

import random
start = input('请决定随机范围开始值')
end = input('请决定随机范围结束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 # 等于 count = count + 1
	num = input("请猜数字")
	num = int(num)
	if num == r:
		print('终于猜对了')
		print('这是你猜的第', count , '次')
		break
	elif num < r:
		print('比答案小')
	else:
		print('比答案大')
	print('这是你猜的第', count , '次')
