#!/usr/bin/python3

enc_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"
flag = []

for i in range(0, len(enc_flag)):
	flag.append(chr(ord(enc_flag[i]) >> 8))
	flag.append(chr(ord(enc_flag[i]) - ((ord(enc_flag[i]) >> 8)<<8)))
print("".join(flag))