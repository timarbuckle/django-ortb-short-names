#!/usr/bin/env python

import json


class JsonPath:

    def __init__(self):
        self.out = []

    def walk(self, node, name):
        for key, item in node.items():
            n = '%s.%s' % (name, key) if len(name) > 0 else key
            if isinstance(item, dict):
                self.walk(item, n)
            elif isinstance(item, list) and isinstance(item[0], dict):
                self.walkaofd(item, n)
            else:
                self.out.append([n, item])

    def walkaofd(self, node, name):
        for item in node:
            self.walk(item, name)

    def convert(self, jdata):
        self.walk(jdata, 'bidrequest')
        return self.out

    def convert_file(self, filename):
        with open(filename) as data_file:
            data = json.load(data_file)
        return self.convert(data)


if __name__ == '__main__':
    from sys import argv
    if len(argv) > 1:
        jp = JsonPath()
        a = jp.convert_file(argv[1])
        for e in a:
            print '%s,  %s' % (e[0], e[1])
    else:
        print 'Usage: %s <filename>' % argv[0]
