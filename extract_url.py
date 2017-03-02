import re

file = open('hotstar.txt','rb').read()#open file

#regular expression to extract from url
ext = re.compile(r'.*\://www.hotstar.com/.*/.*/.*/.*/(.*)',re.IGNORECASE)
final = re.findall(ext,file)
for a in final:
    print a