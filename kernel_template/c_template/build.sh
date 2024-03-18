#!/usr/bin/env bash

set -e

echo $buildPhase
eval $buildPhase
cp ./exp ../rootfs/bin/pwn
cd ../rootfs
find . -print0 | cpio --null -ov --format=newc >../rootfs.cpio
cd ..
./run.sh
