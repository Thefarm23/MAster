#MIT License
#
#Copyright (c) 2022 Amvro23
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import pandas as pd
import matplotlib.pyplot as plt



isotherms = Isotherms()

HmoPowy = np.array([15.2183908,
19.35632184,
25.49425287,
25.56321839,
40.29885057,
34.18390805,
34.62068966])

X= np.array([46.23333333,
68.86666667,
141.0333333,
157.8333333,
246.3666667,
279.4333333,
379.3333333])

CTS40y = np.array([0.586666667,
0.533333333,
3.06,
3.653333333,
3.28,
4,
4.52,]) 

isotherms.set_inlet(X,CTS40y)

isotherms.plot_langmuir_fit()

isotherms.plot_freundlich_fit()

print(isotherms.assess_fit())

plt.show()