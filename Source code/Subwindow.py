from w1 import *
from w_s import *
from w_p import *
from PI import *
from power import *
from SPO2 import *
from HR import *
from Mpl import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from sfft import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtCore import QTimer
import scipy












class SubWindow(QWidget):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.ui_sub = Ui_Form_1()
        self.ui_sub.setupUi(self)
        self.main_widget = QtWidgets.QWidget(self)
        self.ui_sub.canvas = MyMplCanvas(self.main_widget, width=6, height=6, dpi=100)
        self.toolbar = NavigationToolbar(self.ui_sub.canvas, self)
        self.ui_sub.verticalLayout.addWidget(self.toolbar)
        self.ui_sub.verticalLayout.addWidget(self.ui_sub.canvas)





class SubWindow_STFT(QWidget):
    data_stft=pyqtSignal(object,object,object)
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.ui_sub_stft = Ui_Form_STFT()
        self.ui_sub_stft.setupUi(self)
        self.main_widget = QtWidgets.QWidget(self)
        self.ui_sub_stft.canvas = MyMplCanvas_3D(self.main_widget, width=6, height=6, dpi=100)
        self.toolbar = NavigationToolbar(self.ui_sub_stft.canvas, self)
        self.ui_sub_stft.verticalLayout.addWidget(self.toolbar)
        self.ui_sub_stft.verticalLayout.addWidget(self.ui_sub_stft.canvas)
        self.ui_sub_stft.pushButton.clicked.connect(self.plot_map)
        self.data_stft.connect(self.ui_sub_stft.canvas.stft_chart_update)


    def receive_data(self,data,fs):
        self.Data=data
        self.fs=fs

    def plot_map(self):
        win_size = self.ui_sub_stft.lineEdit.text()
        overlap_fac = self.ui_sub_stft.lineEdit_2.text()

        if win_size  == '':
            win_size=200

        if overlap_fac == '':
            overlap_fac=0.5

        win_size = int(win_size)
        overlap_fac = float(overlap_fac)
        ft = STFT(self.Data, self.fs,Block_size=win_size, overlap_fac=overlap_fac)
        freqs, times, Sxx  = ft.stft()
        # print(Sxx)
        self.data_stft.emit(times,freqs,20 * np.log10(Sxx / 1e-06))




class SubWindow_DC(QWidget):
    data_scan_line=pyqtSignal(object, object,object,object)
    data_wave = pyqtSignal(object, object)
    data_scan_line_dc=pyqtSignal(object,object)
    clear_sig=pyqtSignal()
    stop_sig=pyqtSignal()
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        # 时间
        self.timer = QTimer(self)
        self.cnt=0
        self.ymax=0
        self.sel=0
        self.cnt_window=0
        self.start=0
        self.dc_value=[]
        self.dc_time_index=[]
        self.ui_sub_dc = Ui_DC_anz()
        self.record_dc=[]
        self.record_time = []
        self.ui_sub_dc.setupUi(self)
        self.main_widget = QtWidgets.QWidget(self)
        self.ui_sub_dc.canvas = MyMplCanvas(self.main_widget, width=10, height=8, dpi=80)
        self.ui_sub_dc.canvas_2 = MyMplCanvas(self.main_widget, width=10, height=8, dpi=80)
        self.ui_sub_dc.verticalLayout.addWidget(self.ui_sub_dc.canvas)
        self.ui_sub_dc.verticalLayout_2.addWidget(self.ui_sub_dc.canvas_2)
        self.ui_sub_dc.pushButton.clicked.connect(self.startTimer)
        self.ui_sub_dc.pushButton_2.clicked.connect(self.Load_data)
        self.data_wave.connect(self.ui_sub_dc.canvas.chart_update_time)
        self.data_scan_line.connect(self.ui_sub_dc.canvas.plot_vline)
        self.data_scan_line_dc.connect(self.ui_sub_dc.canvas_2.chart_update_time_dc)
        self.stop_sig.connect(self.endTimer)
        self.timer.timeout.connect(self.plot_mapping)
        self.clear_sig.connect(self.ui_sub_dc.canvas_2.chart_clear)
        self.ui_sub_dc.pushButton_3.clicked.connect(self.endTimer)

        self.ui_sub_dc.pushButton.setEnabled(False)
        self.ui_sub_dc.pushButton_2.setEnabled(True)
        self.ui_sub_dc.pushButton_3.setEnabled(False)

    def receive_data(self,data,fs,N,time):
        self.Data=data
        self.fs=fs
        self.N=N
        self.time = time



    def Load_data(self):
        self.clear_sig.emit()
        self.record_dc = []
        self.record_time = []
        self.dc_value = []
        self.dc_time_index = []
        self.cnt = 0
        self.start = 0
        self.data_wave.emit(self.time, self.Data)
        none, self.ymax = self.ui_sub_dc.canvas.axes.get_ylim()
        self.sel=self.ui_sub_dc.lineEdit.text()
        if self.sel=='':
            self.sel=0.1
        self.sel = float(self.sel)

        self.cnt_window=int(self.time[-1]/self.sel)
        self.ui_sub_dc.pushButton_2.setEnabled(False)

        self.ui_sub_dc.pushButton.setEnabled(True)



    def plot_mapping(self):
        self.data_scan_line.emit(self.start,0,self.ymax,self.sel)
        self.cnt=self.cnt+1
        if self.cnt == self.cnt_window:
            self.stop_sig.emit()
            self.ui_sub_dc.pushButton_3.setEnabled(False)

        self.dc_time_index = []
        for i in self.time:
            if self.start<=i<=self.start+self.sel:
                self.dc_value.append(self.Data[self.time.index(i)])
                self.dc_time_index.append(self.time.index(i))


        avg=np.mean(self.dc_value)
        self.dc_value=[]

        for i in range(len(self.dc_time_index)):
            self.dc_value.append(avg)

        self.data_scan_line_dc.emit(self.dc_time_index, self.dc_value)
        self.start=self.start+self.sel
        self.ui_sub_dc.pushButton_3.setEnabled(True)



    def startTimer(self):

        self.timer.start(1000)
        self.ui_sub_dc.pushButton.setEnabled(False)


    def endTimer(self):
        self.timer.stop()
        self.ui_sub_dc.pushButton_2.setEnabled(True)






class SubWindow_PI(QWidget):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.ui_sub_pi = Ui_Form_PI()
        self.ui_sub_pi.setupUi(self)
        self.main_widget = QtWidgets.QWidget(self)
        self.ui_sub_pi.canvas = MyMplCanvas(self.main_widget, width=8, height=6, dpi=80)
        self.toolbar = NavigationToolbar(self.ui_sub_pi.canvas, self)
        self.ui_sub_pi.verticalLayout.addWidget(self.toolbar)
        self.ui_sub_pi.verticalLayout.addWidget(self.ui_sub_pi.canvas)



class SubWindow_SPO2(QWidget):
    scan_IR=pyqtSignal(object,object,object,object)
    scan_Red = pyqtSignal(object, object, object, object)
    data_plot_IR = pyqtSignal(object,object)
    data_plot_Red = pyqtSignal(object, object)
    SpO2_sig=pyqtSignal(object,object,object,object)
    data_sp_avg = pyqtSignal(object)
    data_sp_std = pyqtSignal(object)
    clear_sig=pyqtSignal()
    stop_sig=pyqtSignal()
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.timer = QTimer(self)
        self.time = []

        self.cnt=0
        self.cnt_window=0


        self.data_IR = []
        self.data_Red = []

        self.ui_sub_SPO2 = Ui_Form_SPO2()
        self.ui_sub_SPO2.setupUi(self)
        self.main_widget = QtWidgets.QWidget(self)
        self.ui_sub_SPO2.canvas = MyMplCanvas(self.main_widget, width=8, height=6, dpi=60)
        self.ui_sub_SPO2.verticalLayout.addWidget(self.ui_sub_SPO2.canvas)
        self.ui_sub_SPO2.canvas_2 = MyMplCanvas(self.main_widget, width=8, height=6, dpi=60)
        self.ui_sub_SPO2.verticalLayout_2.addWidget(self.ui_sub_SPO2.canvas_2)
        self.ui_sub_SPO2.canvas_3 = MyMplCanvas(self.main_widget, width=8, height=6, dpi=50)
        self.ui_sub_SPO2.verticalLayout_3.addWidget(self.ui_sub_SPO2.canvas_3)

        self.ui_sub_SPO2.pushButton.clicked.connect(self.startTimer)
        self.ui_sub_SPO2.pushButton_2.clicked.connect(self.endTimer)
        self.data_plot_IR.connect(self.ui_sub_SPO2.canvas.SPO2_data_plot)
        self.data_plot_Red.connect(self.ui_sub_SPO2.canvas_2.SPO2_data_plot)
        self.SpO2_sig.connect(self.ui_sub_SPO2.canvas_3.SpO2_plot)
        self.scan_IR.connect(self.ui_sub_SPO2.canvas.plot_point)
        self.scan_Red.connect(self.ui_sub_SPO2.canvas_2.plot_point)
        self.timer.timeout.connect(self.plot_mapping)
        self.stop_sig.connect(self.endTimer)
        self.data_sp_avg.connect(self.ui_sub_SPO2.lineEdit.setText)
        self.data_sp_std.connect(self.ui_sub_SPO2.lineEdit_2.setText)
        self.clear_sig.connect(self.ui_sub_SPO2.canvas.chart_clear)
        self.clear_sig.connect(self.ui_sub_SPO2.canvas_2.chart_clear)
        self.clear_sig.connect(self.ui_sub_SPO2.canvas_3.chart_clear)
        self.ui_sub_SPO2.pushButton_2.setEnabled(False)


    def receive_data(self,data_IR,data_Red,fs,N,time):
        self.clear_sig.emit()
        self.time = time
        self.record_x = []
        self.record_y = []
        self.data_IR = []
        self.data_Red = []
        self.data_IR = data_IR
        self.data_Red = data_Red
        self.data_IR_peak_x = []
        self.data_IR_peak_y = []
        self.data_IR_va_x = []
        self.data_IR_va_y = []
        self.data_Red_peak_x = []
        self.data_Red_peak_y = []
        self.data_Red_va_x = []
        self.data_Red_va_y = []
        self.data_plot_IR.emit(self.time,data_IR)
        self.data_plot_Red.emit(self.time,data_Red)



        #peak IR
        peaks, _ = signal.find_peaks(data_IR, distance=50)
        for i in peaks:
            self.data_IR_peak_x.append(self.time[i])
            self.data_IR_peak_y.append(self.data_IR[i])



        # peak Red
        peaks, _ = signal.find_peaks(data_Red, distance=50)
        for i in peaks:
            self.data_Red_peak_x.append(self.time[i])
            self.data_Red_peak_y.append(self.data_Red[i])

        # val IR
        tmp_tem = []
        for i in data_IR:
            tmp_tem.append(-i)
        valley_indexes, _ = signal.find_peaks(tmp_tem, distance=50)

        for i in valley_indexes:
            self.data_IR_va_x.append(self.time[i])
            self.data_IR_va_y.append(data_IR[i])

        # val Red
        tmp_tem = []
        for i in data_Red:
            tmp_tem.append(-i)
        for i in valley_indexes:
            self.data_Red_va_x.append(self.time[i])
            self.data_Red_va_y.append(data_Red[i])

        if self.data_IR_va_x[0]<self.data_IR_peak_x[0]:
            self.data_IR_va_x=self.data_IR_va_x[1:]
            self.data_IR_va_y = self.data_IR_va_y[1:]

        if self.data_Red_va_x[0] < self.data_Red_peak_x[0]:
            self.data_Red_va_x = self.data_Red_va_x[1:]
            self.data_Red_va_y = self.data_Red_va_y[1:]

        if self.data_IR_va_x[-1] < self.data_IR_peak_x[-1]:
            self.data_IR_peak_x = self.data_IR_peak_x[:len(self.data_IR_peak_x)-1]
            self.data_IR_peak_y = self.data_IR_peak_y[:len(self.data_IR_peak_x)-1]

        if self.data_Red_va_x[-1] < self.data_Red_peak_x[-1]:
            self.data_Red_peak_x = self.data_Red_peak_x[:len(self.data_Red_peak_x)-1]
            self.data_Red_peak_y = self.data_Red_peak_y[:len(self.data_Red_peak_x)-1]


        a=min(len(self.data_IR_peak_x),len(self.data_IR_va_x))
        b=min(len(self.data_Red_peak_x),len(self.data_Red_va_x))
        self.cnt_window=min(a,b)
        # print(self.cnt_window)
        self.a = 1.5958422
        self.b = -34.6596622
        self.c = 112.6898759




    def startTimer(self):
        self.cnt = 0
        self.ui_sub_SPO2.canvas_3.axes.clear()
        self.ui_sub_SPO2.pushButton_2.setEnabled(True)
        self.ui_sub_SPO2.pushButton.setEnabled(False)


        self.timer.start(300)






    def plot_mapping(self):

        self.scan_IR.emit(self.data_IR_peak_x[self.cnt],self.data_IR_peak_y[self.cnt], self.data_IR_va_x[self.cnt], self.data_IR_va_y[self.cnt])
        self.scan_Red.emit(self.data_Red_peak_x[self.cnt], self.data_Red_peak_y[self.cnt], self.data_Red_va_x[self.cnt], self.data_Red_va_y[self.cnt])
        R = ((self.data_Red_peak_y[self.cnt] - self.data_Red_va_y[self.cnt]) / self.data_Red_va_y[self.cnt]) / ((self.data_IR_peak_y[self.cnt] - self.data_IR_va_y[self.cnt]) / self.data_IR_va_y[self.cnt])
        SPO2=self.a*R*R+self.b*R+self.c

        self.record_x.append(self.cnt)
        self.record_y.append(SPO2)
        self.SpO2_sig.emit(self.cnt,SPO2,self.record_x,self.record_y)



        self.cnt = self.cnt + 1
        if self.cnt == self.cnt_window-1:
            avg_d=round(np.mean(self.record_y),3)
            std_d=round(np.std(self.record_y),3)

            self.data_sp_avg.emit(str(avg_d))
            self.data_sp_std.emit(str(std_d))
            self.stop_sig.emit()


    def endTimer(self):
        self.ui_sub_SPO2.pushButton_2.setEnabled(False)
        self.ui_sub_SPO2.pushButton.setEnabled(True)
        self.timer.stop()




class SubWindow_HR(QWidget):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.ui_sub_HR = Ui_Form_HR()
        self.ui_sub_HR.setupUi(self)
        self.main_widget = QtWidgets.QWidget(self)
        self.ui_sub_HR.canvas = MyMplCanvas(self.main_widget, width=8, height=6, dpi=100)
        self.toolbar = NavigationToolbar(self.ui_sub_HR.canvas, self)
        self.ui_sub_HR.verticalLayout.addWidget(self.toolbar)
        self.ui_sub_HR.verticalLayout.addWidget(self.ui_sub_HR.canvas)
        self.ui_sub_HR.lineEdit.setEnabled(False)



class SubWindow_power(QWidget):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.ui_sub_power = Ui_Form_power()
        self.ui_sub_power.setupUi(self)
        self.main_widget = QtWidgets.QWidget(self)
        self.ui_sub_power.canvas = MyMplCanvas(self.main_widget, width=8, height=6, dpi=100)
        self.toolbar = NavigationToolbar(self.ui_sub_power.canvas, self)
        self.ui_sub_power.verticalLayout.addWidget(self.toolbar)
        self.ui_sub_power.horizontalLayout.addWidget(self.ui_sub_power.canvas)



