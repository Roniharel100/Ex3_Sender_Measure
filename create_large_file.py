#!/usr/bin/python3

with open("1mb.txt", "wb") as out:
    out.seek((1024 * 1024) - 1)
    out.write(b'\0')
