#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# # 2
fin = open('./data.txt', 'r', encoding='utf-8')
pos = readoneline(fin)
N = readoneline(fin)
Al_num = readoneline(fin)
Cnt = readoneline(fin)
fin.close()

# data process

# calculated calibration values in class
a = 2.373e-3
b = -.0161
dEk = .20

c0 = 299792458.
MeV = 1e6 * electron

Emeasure = a * N + b + dEk
x0 = .10
R = (pos - x0) / 2
B = 640.01e-4
Momentum = 300 * B * R
Eclassic = ((Momentum * MeV)**2 / (2 * me * c0**2)) / MeV
Erela = np.array([math.sqrt((i * MeV)**2 + (me * c0**2)**2) - me * c0**2 for i in Momentum]) / MeV
print('pos\t', pos)
print('R\t', R*100)
print('pc\t', Momentum)
print('N\t', N)
print('Eclas\t', Eclassic)
print('Erela\t', Erela)
print('Emes\t', Emeasure)

simple_plot(Momentum, Emeasure, show=0, issetrange=0, dot='+', lab='测量动能')
simple_plot(Momentum, Eclassic, show=0, issetrange=0, dot='*', lab='经典动能')
simple_plot(Momentum, Erela, dot='o', save='1.png', issetrange=0,
            xlab='$pc/MeV$', ylab='$E/MeV$', title='电子动能随动量变化曲线', lab='相对论动能')
# simple_plot(Momentum, Emeasure / Erela, dot='+', lab='测量动能', save='2.png')

Len = 150
Cnt = Cnt / Len
simple_plot(Al_num, Cnt, xlab='铝片数', ylab='选区计数率(射线强度)',
            title='$\\beta$射线强度随铝片数衰减曲线', save='2.png')
CntLn = np.log(Cnt)
# d = 50 mg / cm^2
d = 50
Al_Real = Al_num * d
slope, intercept = simple_linear_plot(Al_Real, CntLn, xlab='质量厚度$g/cm^{-2}$', ylab='选区计数率对数(射线强度)',
                                      title='半对数曲线曲线', save='3.png')
print(-slope)
print(math.log(1e4) / (-slope))
print((math.log(Cnt[0]) - 4 * math.log(10) - intercept) / slope)

gendocx('gen.docx', '1.png', '2.png', '3.png', 'slope, intercept: %f %f' % (slope, intercept))
# linear regression and plot
# #1
# result = linear_regression(x, y)
# setrange(x, y)
# plt.scatter(x, y, marker='o', color='black', label='原始数据')
# plt.plot(x, result['intercept'] + result['slope'] * x, 'r', label='拟合直线')
# plt.xlabel('')
# plt.ylabel('')
# plt.legend(loc=4)
# plt.title('')
# plt.savefig('pic.png')
# plt.show()

# #2
# use automate tool
# simple_linear_plot(x, y, xlab='x axis', ylab='y axis', title='my pic', save='pic.png')


# generate docx #1
# gendocx('gen.docx', 'pic.png', result['string'])

# generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


