#!/usr/bin/env python
import subprocess
import sys

def main():
    args = ["streamlit", "run", "app.py"] + sys.argv[1:]
    subprocess.check_call(args)

if __name__ == '__main__':
    main()
