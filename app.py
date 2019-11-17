#coding=utf8

import json
from constance import *

def display(name, domain, description, head):
    res = "<li><a href=\"" + (domain) + "\" title=\"" + (description) + "\" target=\"_blank\">"
    res += "<img src=\"" + (head) + "\"><span>" + (name) + "</span></a></li>"
    return res

def main():
    file = open("./output.md", mode="w+")
    file.write(prevcss)

    file.write(ulprev + "\n")

    with open("links.json", 'r') as f:
        data = json.load(f)
        for link in data['list']:
            file.write(display(link['name'], link['domain'], link['desc'], link['head']) + "\n")
    
    file.write(ultail + "\n\n")

if __name__ == "__main__":
    main()
