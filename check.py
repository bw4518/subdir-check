from __future__ import print_function

import os

root = 'd:/test/'
out_path = 'd:/test/output.txt'


with open(out_path, 'w') as fp:
    for item in os.listdir(root):
        pth = os.path.join(root, item)

        if os.path.isdir(pth):
            for item2 in os.listdir(pth):
                pth2 = os.path.join(pth, item2)

                if os.path.isdir(pth2):
                    print(pth2)
                    fp.write(pth + '\n')
                    break