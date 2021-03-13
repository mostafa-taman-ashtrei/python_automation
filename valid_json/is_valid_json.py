import os 
import sys
import json

if len(sys.argv) > 1:
	if os.path.exists(sys.argv[1]):
		try:
			file = open(sys.argv[1], 'r')
			json.load(file)
			file.close()
			print(f'{sys.argv[1]} is a valid json file ...')
		except:
			print(f'{sys.argv[1]} is an invalid json file ...')
		
	else:
		print(f'Can NOT find {sys.argv[1]} ...')
else:
	print('Correct usage => is_valid_json.py <file> ...')
