import re


file = open('hotstar.txt','rb').read()

ext = re.compile(r'.*\://www.hotstar.com/.*/.*/.*/.*/(.*)',re.IGNORECASE)
final = re.findall(ext,file)
for a in final:
    print a