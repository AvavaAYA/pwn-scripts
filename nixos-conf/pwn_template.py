#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  author: @eastXueLian

from pwn import *
from lianpwn.nocli import *
import sys

context.log_level = "debug"
context.arch = "amd64"
context.terminal = ["tmux", "sp", "-h", "-l", "120"]

LOCAL = 1
filename = "./pwn"
if LOCAL:
    io = process(filename)
else:
    remote_service = ""
    remote_service = remote_service.strip().split(":")
    io = remote(remote_service[0], int(remote_service[1]))
elf = ELF(filename, checksec=False)
libc = ELF(elf.libc.path, checksec=False)


debugPID()


ia()
