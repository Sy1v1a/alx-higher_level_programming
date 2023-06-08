#!/usr/bin/python3
import hidden_4
j = dir(hidden_4)
sortt = sorted(name for name in j if not name.startswith('__') )
for name in sortt:
    print(name)
