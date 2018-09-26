#coding=utf8
#!/usr/bin/python

class Color :
    def inRed(self,output):
        if str  :
            return '\033[1;41m'+str(output)+'\033[0m'
    def inGreen(self,output):
        if str  :
            return '\033[1;42m'+str(output)+'\033[0m'
    def inYellow(self,output):
        if str  :
            return '\033[1;43m'+str(output)+'\033[0m'
    def inBlue(self,output):
        if str  :
            return '\033[1;44m'+str(output)+'\033[0m'

# 实例化对象
colorful_str = Color()

print (colorful_str.inRed('nishi Red'))
print (colorful_str.inGreen('nishi Green'))
print (colorful_str.inYellow('nishi Yellow'))
print (colorful_str.inBlue('nishi Blue'))
