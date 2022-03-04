# An Example

Here is a real-case example of input several lines of data, plot the data and do linear regression, and generate a printable docx document containing plot and analyse results. 

If you really want to know, the experiment is about verifying the relativistic kinetic energy vs. momentum relationship of electron(beta-ray) and measuring the extraction of beta-ray by aluminum pieces of different thickness. 

**First, put your data in `data.txt`**, like this:

```
# 位置x
e -2
23.     24.2    25.5    26.5    27.7    29.     30.5    31.8
# 峰位N
245.77  291.79  336.40  378.52  417.94  456.14  510.12  544.95
# 铝片数量M
0       1       2       3       4       5
# 选区计数N
43901   34258   28725   23670   19386   16866
```

You can use `#` to comment a line, and `e *` to specify the order of magnitude. 

**Then it's time to write python**

Headers & imports

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *
```

Read the file easily with the `readoneline` function

```python
fin = open('./data.txt', 'r', encoding='utf-8')
pos = readoneline(fin)
N = readoneline(fin)
Al_num = readoneline(fin)
Cnt = readoneline(fin)
fin.close()
```

Calculate and print some results. This is python, you can do whatever you like easily. (This part is not related to the library, you can skip this)

```python
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
```

**Now, plot!**

First graph: three curve in one figure. Using `simple_plot`. You can use LaTeX in plot labels. Graph is saved to `1.png`

```python
simple_plot(Momentum, Emeasure, show=0, issetrange=0, dot='+', lab='测量动能')
simple_plot(Momentum, Eclassic, show=0, issetrange=0, dot='*', lab='经典动能')
simple_plot(Momentum, Erela, dot='o', save='1.png', issetrange=0, xlab='$pc/MeV$', ylab='$E/MeV$', title='电子动能随动量变化曲线', lab='相对论动能')
```

Second graph, a simple curve, saved to `2.png`:

```python
Len = 150
Cnt = Cnt / Len
simple_plot(Al_num, Cnt, xlab='铝片数', ylab='选区计数率(射线强度)', title='$\\beta$射线强度随铝片数衰减曲线', save='2.png')
```

Third graph, a curve with a linear fit, using `simple_linear_plot`, saved to `3.png`:

```python
CntLn = np.log(Cnt)
d = 50
Al_Real = Al_num * d
slope, intercept = simple_linear_plot(Al_Real, CntLn, xlab='质量厚度$g/cm^{-2}$', ylab='选区计数率对数(射线强度)', title='半对数曲线曲线', save='3.png')
print(-slope)
print(math.log(1e4) / (-slope))
print((math.log(Cnt[0]) - 4 * math.log(10) - intercept) / slope)
```

**Don't bother putting pictures in documents yourself!**

With a single line of code, generate a printable docx document with the above three pictures and the fit results. 

```python
gendocx('gen.docx', '1.png', '2.png', '3.png', 'slope, intercept: %f %f' % (slope, intercept))
```

**Results**

Output:

```
pos	 [0.23  0.242 0.255 0.265 0.277 0.29  0.305 0.318]
R	 [ 6.5   7.1   7.75  8.25  8.85  9.5  10.25 10.9 ]
pc	 [1.2480195  1.3632213  1.48802325 1.58402475 1.69922655 1.8240285
 1.96803075 2.0928327 ]
N	 [245.77 291.79 336.4  378.52 417.94 456.14 510.12 544.95]
Eclas	 [1.52375616 1.81804848 2.16616816 2.45469003 2.82471934 3.25488743
 3.78910372 4.28491053]
Erela	 [0.83752628 0.94478965 1.0622588  1.15334615 1.26333503 1.3831891
 1.52222218 1.64324566]
Emes	 [0.76711221 0.87631767 0.9821772  1.08212796 1.17567162 1.26632022
 1.39441476 1.47706635]
0.0038199159787357996
2411.136900195471
2402.45428200782
```

Generated docx: 

![](./gen.png)

