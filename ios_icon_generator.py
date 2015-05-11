#!/usr/bin/env python

# Copyright (c) 2013 Arthur Dexter

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import os.path
from PIL import Image
import sys

ICONS = {
    'iphone': {
        'Settings': (29, [1, 2, 3]),
        'Spotlight': (40, [2, 3]),
        'App-5-6': (57, [1, 2]),
        'App-7-8': (60, [2, 3]),
    },
    'ipad': {
        'Settings': (29, [1, 2]),
        'Spotlight-5-6': (50, [1, 2]),
        'Spotlight-7-8': (40, [1, 2]),
        'App-5-6': (72, [1, 2]),
        'App-7-8': (76, [1, 2]),
    },
    'carplay': {
        '8': (120, [1]),
    },
    'applewatch': {
        'Notification-Center-38mm': (24, [1]),
        'Notification-Center-42mm': (28, [1]),  # 27.5pt in xcode, ceiling to 28pt
        'Companion-Settings': (29, [2, 3]),
        'Home-Screen-Long-Look': (40, [2]),
        'Long-Look': (44, [1]),
        'Short-Look-38mm': (86, [1]),
        'Short-Look-42mm': (98, [1]),
    },
}

def image_name(image_type, device_name, scale):
    scale_string = '' if scale == 1 else "-@%dx" % (scale)
    return 'Icon-%s%s~%s.png' % (image_type, scale_string, device_name)

def iter_icons():
    for device_name, device_icons in ICONS.items():
        for image_type, image_specs in device_icons.items():
            size = image_specs[0]
            scales = image_specs[1]
            for scale in scales:
                yield image_type, device_name, size, scale

if len(sys.argv) != 3:
    print("Usage: %s <input image> <destination directory>" %
          (sys.argv[0]))
    exit(1)

src_file_path = sys.argv[1]
dst_path = sys.argv[2]

if not os.path.isdir(dst_path):
    os.makedirs(dst_path)

im = Image.open(src_file_path)
for image_type, device_name, size, scale in iter_icons():
    new_size = size * scale
    im_resized = im.resize((new_size, new_size), Image.ANTIALIAS)

    dst_name = image_name(image_type, device_name, scale)
    dst_file_path = os.path.join(dst_path, dst_name)
    im_resized.save(dst_file_path)
