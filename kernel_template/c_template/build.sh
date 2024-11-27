#!/usr/bin/env bash

set -e

export buildPhase="gcc -static $LIBLIAN_LD $LIBLIAN_INC -lLian ./exp.c -o ../exploit"
eval $buildPhase
# cp ./exp ../rootfs/bin/pwn
# cd ../rootfs
# find . -print0 | cpio --null -ov --format=newc >../rootfs.cpio
cd ..
./run.sh
