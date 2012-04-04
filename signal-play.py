from scipy import fft
from matplotlib.pyplot import *
from numpy import *
ion()

def gaussian(x):
    return exp(-x**2/10)

k = 200
nsamples = 1024

bitdepth = 8
noise = lambda x: random.normal(.1,.01,(len(x)))
f = lambda x: gaussian(x)*sin(k*x)#*noise(x) 

def digitize(x):
    if bitdepth is 0:
        return x
    a = (2**bitdepth-1)
    return float64(int32(a*x/max(x)))/a

def dB(x):
    return 10*log10(x)
         

def add_detail(x):
    if x =='0':
        return 'non-digitalized'
    return x+' bit'
X = linspace(-7, 7, nsamples)
#plot(X,f(X))
bds = [0, 8, 12, 16]
for bitdepth in bds:
    plot(dB(abs(fft.fftshift(fft.fft(digitize(f(X)))))))
legend(map(lambda x:add_detail(str(x)),bds),loc='upper left')
xlabel('frequency domain (a.u.)')
ylabel('signal (dB)')

#ns = [512, 1024, 2048]
#bitdepth = 8
#for nsamples in ns:
#    X = linspace(-7, 7, nsamples)
#    K = X*nsamples/512.0 
#    plot(K,dB(abs(fft.fftshift(fft.fft(digitize(f(X)))))))
#legend(map(str,ns))
