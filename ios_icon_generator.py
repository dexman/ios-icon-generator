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

ICON_SIZES = [
    (57, False), # App iPhone Non-Retina (iOS 6.1 and Prior)
    (114, True), # App iPhone Retina (iOS 6.1 and Prior)
    (120, True), # App iPhone Retina

    (29, False), # Spotlight iPhone Non-Retina (iOS 6.1 and Prior)
    (58, True),  # Spotlight iPhone Retina (iOS 6.1 and Prior)
    (80, True),  # Spotlight iPhone Retina

    (29, False), # Settings iPhone Non-Retina (iOS 6.1 and Prior)
    (58, True),  # Settings iPhone Retina

    (40, False), # iPad Spotlight Non-Retina
    (80, True),  # iPad Spotlight Retina

    (76, False), # iPad App Non-Retina
    (152, True), # iPad App Retina
]

if len(sys.argv) != 3:
    print("Usage: %s <input image> <destination directory>" %
          (sys.argv[0]))
    exit(1)

src_file_path = sys.argv[1]
dst_path = sys.argv[2]

if not os.path.isdir(dst_path):
    os.makedirs(dst_path)

im = Image.open(src_file_path)
for (size, is_retina) in ICON_SIZES:
    im_resized = im.resize((size, size), Image.ANTIALIAS)
    display_size = size / 2 if is_retina else size
    scale_name = "@2x" if is_retina else ""
    dst_name = "Icon-%d%s~iphone.png" % (display_size, scale_name)
    dst_file_path = os.path.join(dst_path, dst_name)
    im_resized.save(dst_file_path)
