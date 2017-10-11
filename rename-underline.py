#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil


def scan(path):
    names = []
    for fn in os.listdir(path):
        if fn.startswith('_'):
            names.append(fn[:-4])
            shutil.move(os.path.join(path, fn), os.path.join(path, fn[1:]))
    for fn in os.listdir(path):
        if fn.endswith('.htm'):
            filename = os.path.join(path, fn)
            with open(filename) as f:
                old = text = f.read()
            count = 0
            for name in names:
                text = text.replace(name, name[1:])
                count += 1
            if old != text:
                print('%s\t%d' % (fn, count))
                open(filename, 'w').write(text)


if __name__ == '__main__':
    scan('doc')
