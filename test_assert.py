#coding=utf-8
import pytest

# 功能
def add(a,b):
	return a + b

# 测试相等
def test_add():
	assert add(3,4) == 7 

# 测试不相等
def test_add2():
	assert add(17,22) != 50

# 测试大于
def test_add3():
	assert add(17,22) <= 50

# 测试小于
def test_add4():
	assert add(17,22) >= 50


# 测试相等
def test_in():
	a = "hello"
	b = "he"
	assert b in a 

# 测试不相等
def test_not_in():
	a = "hello"
	b = "hi"
	assert b not in a


#用于判断素数
def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
		return True

# 判断是否为素数
def test_true():
	assert is_prime(13)

# 判断是否不为素数
def test_nottrue():
	assert not is_prime(7)

