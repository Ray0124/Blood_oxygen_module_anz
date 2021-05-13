from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure
from PyQt5 import QtWidgets
import pywt
import numpy as np
from matplotlib import cm
from scipy import signal,fft
import time

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=6, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes=  self.fig.add_subplot(1, 1, 1)
        self.cb=0
        self.sc_line=0
        self.sc_point=0
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)



    def chart_update(self,value):
        if self.cb != 0:
            self.cb.remove()
            self.cb = 0
        self.axes.clear()
        self.axes.plot(value, 'r')
        self.axes.set_xlabel('Points')
        self.axes.set_ylabel('Magnitude')
        self.draw()


    def chart_update_time(self,x,y):
        if self.cb != 0:
            self.cb.remove()
            self.cb = 0
        self.axes.clear()
        self.axes.plot(x,y, 'r')
        self.axes.set_xlabel('time')
        self.axes.set_ylabel('Magnitude')
        self.draw()


    def fft_chart(self,x,y):
        if self.cb != 0:
            self.cb.remove()
            self.cb=0
        self.axes.clear()

        peaks, _ = signal.find_peaks(y, height=25)
        re_Data_s = []
        for i in peaks:
            re_Data_s.append(y[i])
        peak_time = []
        for i in peaks:
            peak_time.append(x[i])
        self.axes.plot(x,y, 'r')
        self.axes.scatter(peak_time, re_Data_s, color='b',s=20)
        for i in range(len(peak_time)):
            self.axes.text(peak_time[i],re_Data_s[i]+1,s='('+str(round(peak_time[i],2))+','+str(round(re_Data_s[i],2))+')')
        self.axes.set_xlabel('Frequency [Hz]')
        self.axes.set_ylabel('Magnitude')
        self.draw()


    def plot_map(self, num, time, data, f):
        wcf = pywt.central_frequency(wavelet='cgau8')
        totalscal = num
        cparam = 2 * wcf * totalscal
        scales = cparam / np.arange(totalscal, 1, -1)
        [cwtmatr, frequencies] = pywt.cwt(data, scales, 'cgau8', 1.0 / f)
        self.axes.clear()
        target = self.axes.contourf(time, frequencies, abs(cwtmatr))
        self.axes.set_ylabel(u"freq(Hz)")
        self.axes.set_xlabel(u"time(s)")
        if self.cb == 0:
            self.cb= self.fig.colorbar(target, shrink=0.5, aspect=20)

        self.draw()

    def plot_map_db(self, num, time, data, f):
        wcf = pywt.central_frequency(wavelet='cgau8')
        totalscal = num
        cparam = 2 * wcf * totalscal
        scales = cparam / np.arange(totalscal, 1, -1)
        [cwtmatr, frequencies] = pywt.cwt(data, scales, 'cgau8', 1.0 / f)
        self.axes.clear()
        target = self.axes.contourf(time, frequencies, 20 * np.log10(abs(cwtmatr)))
        self.axes.set_ylabel(u"freq(db)")
        self.axes.set_xlabel(u"time(s)")
        if self.cb == 0:
            self.cb=self.fig.colorbar(target, shrink=0.5, aspect=20)
        self.draw()

    def plot_vline(self,x,y_m,yM,shift):
        if self.sc_line == 0:
            self.sc_line=self.axes.axvline(x,y_m,yM,color='b')
            self.sc_line_2 = self.axes.axvline(x+shift, y_m, yM, color='b')
        else:
            self.sc_line.remove()
            self.sc_line_2.remove()
            self.sc_line = self.axes.axvline(x, y_m, yM, color='b')
            self.sc_line_2 = self.axes.axvline(x + shift, y_m, yM, color='b')
        self.draw()

    def plot_point(self, x_peak, y_peak, x_va, y_va):
        self.sc_point = self.axes.scatter(x_peak, y_peak ,color='b')
        self.sc_point_2 = self.axes.scatter(x_va, y_va, color='g')
        self.draw()








    def chart_update_time_dc(self,x,y):
        if self.cb != 0:
            self.cb.remove()
            self.cb = 0

        self.axes.plot(x,y, 'r')
        self.axes.set_xlabel('time')
        self.axes.set_ylabel('Magnitude')

        self.draw()

    def chart_clear(self):
        self.axes.clear()
        self.draw()

    def chart_update_scatter(self,x_high,y_high,ori_y,x_low,y_low):
        if self.cb != 0:
            self.cb.remove()
            self.cb = 0
        self.axes.clear()
        self.axes.plot(ori_y, c='r')
        self.axes.scatter(x_high,y_high, c='b')
        self.axes.scatter(x_low, y_low, c='g')
        self.axes.set_xlabel('Points')
        self.axes.set_ylabel('Magnitude')
        self.draw()

    def SPO2_data_plot(self,time,y):
        self.axes.clear()
        self.axes.plot(time,y, c='r',label='Red')
        self.axes.set_xlabel('Time(s)')
        self.axes.set_ylabel('Magnitude')
        self.draw()

    def SpO2_plot(self, cnt,value,x,y):
        self.axes.plot(x, y, color='r')
        self.axes.scatter(cnt,value, color='b',s=50)
        self.axes.set_xlabel('Set')
        self.axes.set_ylabel('%')
        self.draw()



    def HR_plot(self,x,y,x_peak,y_peak):
        self.axes.clear()
        self.axes.plot(x,y, c='r')
        self.axes.scatter(x_peak, y_peak, c='b')
        self.axes.set_xlabel('Time(s)')
        self.axes.set_ylabel('Magnitude')
        self.draw()


    def welch_power_plot(self,x,y,left,right):
        self.axes.clear()
        self.axes.plot(x,y, c='r')
        self.axes.set_xlabel('frequency [Hz]')
        self.axes.set_ylabel('Linear spectrum [V RMS]')
        _,ymax=self.axes.get_ylim()
        ymin=0
        self.axes.axvline(left,ymin,ymax,alpha=0.3,linestyle='--')
        self.axes.axvline(right,ymin,ymax,alpha=0.3,linestyle='--')
        self.axes.text((left+right)/2, (ymin+ymax)/2, 'signal range')
        # self.fig.tight_layout()
        self.draw()

    def FFT_power_plot(self, x, y, left, right):
        self.axes.clear()
        self.axes.plot(x, y, c='r')
        self.axes.set_xlabel('Hz')
        self.axes.set_ylabel('Magnitude')
        _, ymax = self.axes.get_ylim()
        ymin = 0
        self.axes.axvline(left, ymin, ymax, alpha=0.3, linestyle='--')
        self.axes.axvline(right, ymin, ymax, alpha=0.3, linestyle='--')
        self.axes.text((left + right) / 2, (ymin + ymax) / 2, 'signal range')
        # self.axes.tick_params(direction='out', length=1, width=1, colors='black',
        #             grid_color='black', grid_alpha=0.5)

        self.draw()





class MyMplCanvas_3D(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111, projection='3d')



        self.cb = 0
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def stft_chart_update(self,X,Y,Z):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(X, Y)
        surf = self.ax.plot_surface(X, Y, Z, cmap=cm.plasma, linewidth=0, antialiased=False)
        # self.ax.set_zlim(60, 170)
        self.ax.set_xlabel('time')
        self.ax.set_ylabel('freq')
        self.ax.set_zlabel('db')
        if self.cb == 0:
            self.fig.colorbar(surf, shrink=0.5, aspect=20)
        self.draw()


