#文件的打开或者创建 和关闭
print(1+2)
print('abc')
print('helloword')
print(123)
fp = open('G:\Python1\chap1/text.txt','a+')       #打开或者新建text.txt
print('main',file=fp)
fp.close()      #关闭

#转义字符
print('----------------------------------------------------------------------')
print('hello\nworld')       #换行
print('hello\tworld')       #水平制表符【水平制表符就是按键Tab】
print('hellooo\tworld')
print('helloooo\tworld')
print('helld\rworld')   #回车覆盖
print('hello\bworld')   #退格

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')
print(r'hello\nworld')      #不希望字符串里的转义字符起作用加上r或者R
#注意事项   最后一个字符不能是反斜杠\
#   print(r'hello\nworld\')






