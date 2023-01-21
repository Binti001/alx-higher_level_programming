#!/usr/bin/python3




def lookup(obj):
    attr_meth = []
    for i in dir(obj):
        attr_meth.append(i)
    return attr_meth
