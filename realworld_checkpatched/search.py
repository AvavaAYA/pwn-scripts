#!/usr/bin/python3

# Used when libc isn's provided

import requests
import json

item_name = "main_arena"
item_offs = "c40"

test_item = "system"

headers = {'Content-Type':'application/json'}
url = "https://libc.rip/api/find"

for test2bits in range(0xff):
	test_bits = hex(test2bits << 4).replace("0x", "").rjust(3, "0")
	query_json = {"symbols": {item_name: item_offs, test_item: test_bits}}
	res = requests.post(url, headers=headers, json=query_json)
	res = json.loads(res.content)
	for i in range(len(res)):
		# new_url = "https://libc.rip/api/libc/" + res[i]["id"]
		# new_query_json = {"symbols": ["strcat", "_IO_2_1_stderr_"]}
		# new_res = requests.post(new_url, headers=headers, json=new_query_json)
		# new_res = json.loads(new_res.content)
		print(res[i]["id"])
		print(res[i]["symbols"])
		print(new_res)
	print(test_bits)

