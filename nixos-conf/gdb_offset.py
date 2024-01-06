# offsets.py
import gdb

def search(strList, search_patt):
    for i in strList:
        if search_patt in i:
            return i

class Offset(gdb.Command):
    def __init__(self):
        super(self.__class__, self).__init__("Offset", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        #if len(argv) != 2:
        #    raise gdb.GdbError('invalid argcount.')
        vmmap_res = gdb.execute("vmmap", to_string=True).split('\n')[1:]
        elf_base_list = vmmap_res[0].split(" ")
        for i in elf_base_list:
            if "0x" in i:
                elf_base = i
                break
        gdb.execute("set $elf_base=" + elf_base)
        for i in vmmap_res:
            if "libc" in i:
                libc_base_list = i.split(" ")
                break
        for i in libc_base_list:
            if "0x" in i:
                libc_base = i
                break
        gdb.execute("set $libc_base=" + libc_base)

class elf_base(gdb.Command):
    def __init__(self):
        super(self.__class__, self).__init__("elf_base", gdb.COMMAND_USER)
    
    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        gdb.execute("Offset")
        res = search(gdb.execute("p /x $elf_base", to_string=True).split(" "), "0x")
        print("$elf_base = " + res)

class libc_base(gdb.Command):
    def __init__(self):
        super(self.__class__, self).__init__("libc_base", gdb.COMMAND_USER)
    
    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        gdb.execute("Offset")
        res = search(gdb.execute("p /x $libc_base", to_string=True).split(" "), "0x")
        print("$libc_base = " + res)

class createList(gdb.Command):
    def __init__(self):
        super(self.__class__, self).__init__("createList", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        if len(argv) != 1:
            fileName = "./.sym"
        else:
            fileName = argv[0]
        with open(fileName, "r+") as fd:
            while True:
                
                text = fd.readline().split(" ")
                
                if (not text) or len(text) != 3:
                    break
                off = int(text[0], 16)
                name = text[1]
                if "elf" in text[2]:
                    base_chosen = int(search(gdb.execute("elf_base", to_string=True).split(" "), "0x"), 16)
                elif "libc" in text[2]:
                    base_chosen = int(search(gdb.execute("libc_base", to_string=True).split(" "), "0x"), 16)
                gdb.execute("set $" + name + "=" + str(off + base_chosen))


Offset()
elf_base()
libc_base()
createList()
