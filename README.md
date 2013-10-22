ios-icon-generator
==================

Small python script to generate all the various iOS icon sizes (iPhone
only right now).

Requirements
------------

Requires the Python Imaging Library (PIL) to be installed.

Usage
-----

Given an input image file, generates all the variants of the
application icon necessary for an iOS app (iPhone only for now). The
input image should be at least 120x120 pixels, as that is the largest
application icon size currently required.

`ios_icon_generator.py <input image> <destination directory>`

