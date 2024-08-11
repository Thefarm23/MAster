import matplotlib.pylab as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import stats
import math
#Batch HMO Powder
Batch = [16.33333333,
20.36666667,
15.36666667,
18.33333333,
23.13333333,
26.0,]
#Maxad = Batch[-1] + 0.01
BatchTime= [1, 3, 6, 12, 24, 48]
#HMO Powder

#CTS 40

BatchCTS =[0.506666667,
0.546666667,
-2.533333333,
1.413333333,
1.253333333,
2.2,]

Maxad = BatchCTS[-1] + 0.01
###


#CTS 40


# Convert lists to NumPy arrays
x_array = np.array(BatchTime)
y_array = np.array(BatchCTS)
print(Maxad- y_array[1])


def lg(qe):

    return np.log(Maxad-qe)

print(lg(y_array))
def overt(qt,x):
    y = x/qt
    return y 

def k1 (x,k_1):
    y = math.log(Maxad)- (k_1/2.303)*x
    return y 

def k2 (x,k_2):
    y = (1/k_2)*(1/(Maxad)**2) + (1/(Maxad))*x
    return y

def lin(x,a,b):
    return a*x +b
    
    

first_order = curve_fit(k1, x_array , lg(y_array), p0= [0.1])

second_order = curve_fit(k2, x_array, overt(y_array,x_array), p0= [0.1] )

pred_second = lin(x_array, *second_order)

pred_first = lin(x_array, *first_order)

R_value_first = stats.linregress(lg(y_array), pred_first).rvalue

R_value_second = stats.linregress(overt(y_array, x_array),pred_second).rvalue

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(x_array, lg(y_array), label='Experimental Data')
plt.plot(x_array, k1(x_array, *first_order[0]), 'r-', label='Fitted Curve')
plt.xlabel('Time')
plt.ylabel('ln(Q_e-Q_t)[Mg^-1 g] ')
plt.title(f'First-order Kinetics R = {-R_value_first}')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(x_array, overt(y_array, x_array), label='Experimental Data')
plt.plot(x_array, k2(x_array, *second_order[0]), 'g-', label='Fitted Curve')
plt.xlabel('Time')
plt.ylabel('t/Q_t [Mg^-1 g]')
plt.title(f'Second-order Kinetics R ={R_value_second}')
plt.legend()

plt.show()

