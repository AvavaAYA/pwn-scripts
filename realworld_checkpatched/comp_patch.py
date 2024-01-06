#coding:utf8
import os

src_dir = u'C:\\Users\\inva1id\\Desktop\\qwb\\RW\\RDP\\orig' # 源文件目录地址

comp_dest = u'C:\\Users\\inva1id\\Desktop\\qwb\\RW\\RDP\\patc'

def list_all_files(rootdir):
	_files = []

	#列出文件夹下所有的目录与文件
	list_file = os.listdir(rootdir)

	for i in range(0,len(list_file)):
		# 构造路径
		path = os.path.join(rootdir,list_file[i])

		# 判断路径是否是一个文件目录或者文件
		# 如果是文件目录，继续递归
		if os.path.isdir(path):
			_files.extend(list_all_files(path))
		if os.path.isfile(path):
			_files.append(path)
	return _files

files = list_all_files(src_dir)
for path in files:
	path2 = comp_dest + '\\' + path[len(src_dir)+1:]
	# print(path2)
	f = open(path,'rb')
	content1 = f.read()
	f.close()
	try:
		f = open(path2,'rb')
		content2 = f.read()
		f.close()
	except:
		continue
	if content1 != content2:
		print(path)