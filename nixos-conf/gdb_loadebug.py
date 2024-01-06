import gdb

# 获取当前的 debug-file-directory 设置
current_directory = gdb.execute("show debug-file-directory", to_string=True).split('"')[
    1
]

# 在当前设置之前添加当前目录
new_directory = "./.debug:" + current_directory

# 设置新的 debug-file-directory
gdb.execute("set debug-file-directory " + new_directory)
