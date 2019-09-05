'''
实现图片转字符画的小工具
实现原理：
字符画是一系列字符的组合，用一个字符来体现一种颜色，字符种类代表原图的颜色种类和层次
灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像
运用灰度值公式将像素的RGB值映射到灰度值(此处用一简化公式):
gray = 0.2126*r + 0.7152*g + 0.0722*b
将图片的每一个像素提取其rgb值通过计算转换为相应字符
用到im.getpixel((j,i))放放，获取对应坐标
'''

from PIL import Image
import argparse
# 构建命令行输入参数处理ArgumentParser 实例
parse = argparse.ArgumentParser()

#定义输入文件、输出文件、输出字符画的宽和高
parse.add_argument('file')  # 输入文件
parse.add_argument('-o','--output') #输出文件
parse.add_argument('--width',type=int,default=80)# 输出字符画宽
parse.add_argument('--height',type=int,default=80)#输出字符画高

#解析并获取参数
args = parse.parse_args()
#输入图片文件路径
IMG = args.file
#输出字符画的宽度
WIDTH = args.width
#输出字符画的高度
HEIGHT = args.height
#输出字符画的路径
OUTPUT = args.output

#设置字符画所使用的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    #判断alpha值
    if alpha ==0:
        return ' '
    #获取字符集的宽度
    length = len(ascii_char)
    #将rgb值转为灰度值gray,灰度值范围是0-255
    gray = int(0.2126*r +0.7152*g + 0.0722*b)
    #灰度值范围是0-255 ，而字符集只有70
    #需要平均细分一下灰度值使其映射到指定字符上
    unit = (256.0+1)/length

    #返回灰度值队形的字符
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im =  Image.open(IMG)
    # im.resize的第二个参数中,Image.NEAREST表示输出低质量的图片
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    #初始化输出的字符串
    txt= ''

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        #遍历完一行后增加换行符
        txt += '\n'

    print(txt)
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('output.txt','w') as f:
            f.write(txt)