#!/usr/bin/env python
# coding:utf-8
#编程之美之寻找最大的连续子序列
#注意当都是负数的情况下返回0
#如果都是负数的情况下返回负数的最大值，则需要先找最小的连续子序列
A1 = [1,-1,3,0,7,-10,4,5,-5,6]

def find_max_sub_array(A):
	f = []
	Last = []
	f.append(A[0])
	Last.append(A[0])

	for i in range(1,len(A)):
		Last.append(max(Last[i - 1] + A[i], 0))
		f.append(max(f[i-1], Last[i]))
	print(f[len(A) - 1])

def main():
	find_max_sub_array(A1)

if __name__ == '__main__':
	main()
