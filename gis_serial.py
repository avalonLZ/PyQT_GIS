# -*- coding: utf-8 -*-
import sys
import time
from gis_form import *
from PyQt4 import QtCore, QtGui
import serial
import serial.tools.list_ports

#$GNGGA,033723.000,2308.9503,N,11325.9527,E,6,06,4.1,30.6,M,0.0,M,,*40
#$GNRMC,033723.000,A,2308.9503,N,11325.9527,E,999.00,103.94,261017,,,E*72

#GIS信息校验
def GIS_Check(temstr):
    checksum = 0

    for i in temstr:
        checksum = checksum ^ ord(str(i))#注意需要一个str
    return checksum

#串口扫描，返回存在的COM口
def serial_ports(open_com = None):
    ports = []
    port_list = list(serial.tools.list_ports.comports())
    for i in port_list:
        ports.append(str(i.device))
    return ports

class Thread_SendData(QtCore.QThread):

    def __init__(self, temstr = '', parent=None, obj = None):
        super(Thread_SendData, self).__init__(parent)
        self.temstr = temstr
        self.serial = obj.ser
        self.interval = obj.return_interval()
        self.display = obj.return_ui_display()
        self.nostop = 1

    def run(self):
        while self.nostop:#while结束线程也就退出了
            self.serial.write(str(self.temstr))
            self.display.append(str(self.temstr))
            self.display.currentFont()
            time.sleep(int(self.interval))

    def senddata_stop(self):#被外信号绑定的函数不能写为私有函数
        self.nostop = 0

old_port = []#保证不一致刷新com口数量
class Thread_ScanCom(QtCore.QThread):
    #信号初始化时可以带类型参数表示，使用信号并传递一个指定类型的参数
    sinOut = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(Thread_ScanCom, self).__init__(parent)
        self.new_port = []

    def run(self):
        while 1:
             old_port = self.new_port
             self.new_port = serial_ports()

             if self.new_port != old_port:
                self.sinOut.emit(self.new_port)#发送信号到主线程

class MainWindow(QtGui.QWidget):
    sin2senddatastop = QtCore.pyqtSignal()#类变量，可由类名直接调用，也可由实例调用。一个线程只能绑定一个信号量
    ser = serial.Serial()

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.__ui = Ui_Windows()
        self.__ui.setupUi(self)

        self.__param_init()
        self.__solt_init()

        # 创建线程扫描com变化
        self.thread_scancom = Thread_ScanCom()
        self.thread_scancom.sinOut.connect(self.__scancom)
        self.thread_scancom.start()

    def __click_start(self):
        if self.__ui.comboBox.currentText() == '' or str(self.__ui.serial.currentText()) == '':
            QtGui.QMessageBox.warning(self, u"错误" ,u"串口或波特率错误，请检查")
            return
        self.__ui_disable(self.__ui.start)
        self.__ui_disable(self.__ui.clean)
        self.__serial_config(serial = self.ser, port = str(self.__ui.serial.currentText()),
                             baudrate = int(self.__ui.comboBox.currentText()))
        #若已经打开，关闭前将无法再次打开，此后的程序不再执行
        self.ser.open()

        self.__gis_fill()

        #创建线程按1秒间隔发送gis信息
        self.__thread_senddata = Thread_SendData(temstr = self.gga + '\r\n' + self.rmc + '\r\n', obj = self)
        self.sin2senddatastop.connect(self.__thread_senddata.senddata_stop)  # 绑定信号
        self.__thread_senddata.start()

    def __click_end(self):
        self.__ui_enable(self.__ui.start)
        self.__ui_enable(self.__ui.clean)
        self.sin2senddatastop.emit()
        self.ser.close()

    def __click_cleandisplay(self):
        self.__ui.display.clear()

    def __click_about(self):
        QtGui.QMessageBox.about(self, u"关于", u"0183协议生成器\r\n从指定串口输出0183协议数据\r\n"
                                             u"                                 by:lz")

    def __scancom(self, com_list):
        self.__ui.serial.clear()
        self.__ui.serial.addItems(com_list)

    def __param_init(self):
        self.gga1 = "$GNGGA,033723.000,"
        self.latitudenum = "2308.9503"  # 纬度
        self.gga2 = ",N,"
        self.longitudenum = "11325.9527"  # 经度
        self.gga3 = ",E,6,06,4.1,30.6,M,0.0,M,,*"
        self.ggachecknum = "0"
        self.gga = ""

        self.rmc1 = "$GNRMC,033723.000,A,"
        self.rmc2 = ",N,"
        self.rmc3 = ",E,"
        self.speednum = "999.00"
        self.rmc4 = ",103.94,261017,,,E*"
        self.rmcchecknum = "0"
        self.rmc = ""

        self.interval = ""

    def __solt_init(self):
        self.connect(self.__ui.start, QtCore.SIGNAL("clicked()"), self.__click_start)
        self.connect(self.__ui.end, QtCore.SIGNAL("clicked()"), self.__click_end)
        self.connect(self.__ui.clean, QtCore.SIGNAL("clicked()"), self.__click_cleandisplay)
        self.connect(self.__ui.about, QtCore.SIGNAL("clicked()"), self.__click_about)

    def __serial_config(self, serial = None, port = None, baudrate = None, bytesize = 8, stopbits = 1, parity = 'N'):
        serial.port = port
        serial.baudrate = baudrate
        serial.bytesize = bytesize
        serial.stopbits = stopbits
        serial.parity = parity

    def __gis_fill(self):
        self.longitudenum = self.__ui.longutide.text()
        self.latitudenum = self.__ui.latitude.text()
        self.speednum = self.__ui.speed.text()
        self.gga = self.gga1 + self.latitudenum + self.gga2 + self.longitudenum + self.gga3
        self.ggachecknum = GIS_Check(self.gga)
        self.gga += hex(self.ggachecknum)[2:]

        self.rmc = self.rmc1 + self.latitudenum + self.rmc2 + self.longitudenum + self.rmc3 + self.speednum + self.rmc4
        self.rmcchecknum = GIS_Check(self.rmc)
        self.rmc += hex(self.rmcchecknum)[2:]

        self.interval = self.__ui.interval.text()

    def __ui_disable(self, obj = None):
        obj.setDisabled(True)

    def __ui_enable(self, obj = None):
        obj.setDisabled(False)

    def return_ui_display(self):
        return self.__ui.display

    def return_interval(self):
        return self.interval

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp=MainWindow()

    #窗口最大化按键无效
    myapp.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

    #锁定窗口大小
    myapp.setFixedSize(myapp.width(), myapp.height())
    myapp.show()
    app.exec_()