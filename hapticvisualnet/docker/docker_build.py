#!/usr/bin/env python
import os

if __name__=="__main__":
    cmd = "docker build -t hapticnet ."
    code = os.system(cmd)
