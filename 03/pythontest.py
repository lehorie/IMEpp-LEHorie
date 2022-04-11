from matplotlib.pyplot import xlabel, ylabel
import numpy as np
import scipy.optimize

def fit_sin(tt, yy):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    tt = np.array(tt)
    yy = np.array(yy)
    ff = np.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(np.fft.fft(yy))
    guess_freq = 0.00845   # excluding the zero frequency "peak", which is related to offset
    guess_amp = 55.
    #guess_offset = np.mean(yy)
    guess = np.array([guess_amp, 2.*np.pi*guess_freq, np.pi/3])

    def sinfunc(t, A, w, p):  return A * abs(np.sin(w*t + p))
    popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yy, p0=guess)
    A, w, p= popt
    f = w/(2.*np.pi)
    fitfunc = lambda t: A * abs(np.cos(w*t + p))
    return {"amp": A, "omega": w, "phase": p, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": np.max(pcov), "rawres": (guess,popt,pcov)}
import pylab as plt

N = 43
#N, amp, omega, phase, offset, noise = 50, 1., .4, .5, 4., .2
#N, amp, omega, phase, offset, noise = 200, 1., 20, .5, 4., 1
tt = np.linspace(0, 210, N)
tt_ticks = []
for i in range(len(tt)):
    tt_ticks.append(str(tt[i]))
tt2 = np.linspace(0, 210, 1000*N)
yData = np.array([26.99,32.49,41.49,53.28,55.23, 57.82,51.98,50.03,40.94,27.29,11.05,6.62,21.18,35.74,44.4,56.67,57.76,58.48,58.12,52.34,40.07,29.6,17.69,3.91,16.61,31.49,42.6,49.82,57.4,57.76,57.4,53.43,44.76,38.26,18.77,6.31,7.95,25.49,37.74,48.23,60.1,54.53,55.88])
res = fit_sin(tt, yData)
print( "Amplitude=%(amp)s, Angular freq.=%(omega)s, phase=%(phase)s, Max. Cov.=%(maxcov)s" % res )

#plt.plot(tt, yy, "-k", label="y", linewidth=2)
xlabel('x (cm)')
ylabel('I (W/m^2)')
#plt.xticks(tt, tt_ticks)
plt.plot(tt, yData, "ok", label="Points")
plt.plot(tt2, res["fitfunc"](tt2), "r-", label="y fit curve", linewidth=2)
plt.legend(loc="best")
plt.savefig('plot.png')