import os 
import sys 
from PIL import Image

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        print(sys.argv[1], sys.argv[2])
        img = Image.open(sys.argv[1])
        img_name = sys.argv[1].split('/')[-1]
        img_name = img_name.split('.')[0]

        output = f'{img_name}.{sys.argv[2]}'
        img.save(output)
        print(f'{img_name} converted to {sys.argv[2]} successfully ...')

    else:
        print(f'Can NOT find {sys.argv[1]} ...')
else:
    print('Correct usage => is_valid_json.py <image> <extension> ...')