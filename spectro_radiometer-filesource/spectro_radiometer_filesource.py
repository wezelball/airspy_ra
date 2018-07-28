#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Spectral and Radiometry Receiver
# Description: Testing with file source
# Generated: Sat Jul 28 07:40:26 2018
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import sip
import spectro_helper  # embedded python module
import sys
import threading
import time
from gnuradio import qtgui


class spectro_radiometer_filesource(gr.top_block, Qt.QWidget):

    def __init__(self, abw=4.0e6, antenna='RX2', baseline=99.3, bbgain=5, bw=-1.0e6, clock='default', dcg=100, decln=0, device="rtl=0 file=/dev/zero,rate=5e6", fftsize=2048, frequency=1420.4058e6, gain=30, ifgain=5, latitude=44.9, longitude=-76.03, mode="total", ppstime='internal', prefix="h1", ra=12.0, rfilist="", srate=2.56e6, zerotime=99.3):
        gr.top_block.__init__(self, "Spectral and Radiometry Receiver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Spectral and Radiometry Receiver")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "spectro_radiometer_filesource")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Parameters
        ##################################################
        self.abw = abw
        self.antenna = antenna
        self.baseline = baseline
        self.bbgain = bbgain
        self.bw = bw
        self.clock = clock
        self.dcg = dcg
        self.decln = decln
        self.device = device
        self.fftsize = fftsize
        self.frequency = frequency
        self.gain = gain
        self.ifgain = ifgain
        self.latitude = latitude
        self.longitude = longitude
        self.mode = mode
        self.ppstime = ppstime
        self.prefix = prefix
        self.ra = ra
        self.rfilist = rfilist
        self.srate = srate
        self.zerotime = zerotime

        ##################################################
        # Variables
        ##################################################
        self.ifreq = ifreq = frequency
        self.wlam = wlam = 299792000.0/ifreq
        self.tp_pacer = tp_pacer = [-100.0]*fftsize
        self.time_pacer = time_pacer = [-100.0]*fftsize
        self.set_baseline = set_baseline = 0
        self.samp_rate = samp_rate = int(srate)
        self.ira = ira = ra
        self.fstop = fstop = False
        self.frate = frate = ((180.0/3.14159)*wlam/baseline)/math.cos(math.radians(decln))
        self.fft_probed = fft_probed = [-100.0]*fftsize
        self.fft_avg = fft_avg = 4
        self.fft2_probed = fft2_probed = [-100.0]*fftsize
        self.enable_normalize = enable_normalize = 0
        self.declination = declination = decln
        self.dcgain = dcgain = dcg
        self.corr_probed = corr_probed = complex(0.0,0.0)
        self.clear_baseline = clear_baseline = 0
        self.annotation = annotation = ""
        self.ang = ang = 0
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = spectro_helper.lmst_string(time_pacer,longitude)
        self.start_km = start_km = ((samp_rate/2)/ifreq)*299792
        self.secondary_lmst_label = secondary_lmst_label = spectro_helper.lmst_string(time_pacer,longitude)
        self.mode_map = mode_map = {"total" : "Continuum Power", "tp" : "Continuum Power", "diff" : "Differential Power", "differential" : "Differential Power", "correlator" : "Cross  Power", "interferometer": "Cross Power", "corr" : "Cross Power"}
        self.km_incr = km_incr = (((samp_rate/fftsize)/ifreq)*299792)*-1.0
        self.igain = igain = gain
        self.ifilt = ifilt = firdes.low_pass(1.0,samp_rate,bw/2.0,samp_rate/8) if bw > 0.0 else [1.0]
        self.frotate = frotate = spectro_helper.fringe_stop (tp_pacer, ra, decln, longitude, latitude, baseline, fstop, ang, ifreq)
        self.fringe_label = fringe_label = frate*240.0
        self.fincr = fincr = (samp_rate/1.0e6)/fftsize
        self.fft_log_status = fft_log_status = spectro_helper.fft_log(fft_probed,fft2_probed,corr_probed,ifreq,samp_rate,longitude,enable_normalize,prefix,declination,rfilist,dcgain,fft_avg,mode,zerotime)
        self.dcblock = dcblock = True
        self.curr_tp_vect = curr_tp_vect = spectro_helper.get_tp_vect(tp_pacer)
        self.curr_dx = curr_dx = spectro_helper.curr_diff(fft_probed,enable_normalize)
        self.baseline_set_status = baseline_set_status = spectro_helper.baseline_setter(set_baseline)
        self.baseline_clear_status = baseline_clear_status = spectro_helper.baseline_clearer(clear_baseline)
        self.anno_status = anno_status = spectro_helper.do_annotation(ira,declination,baseline,annotation,bw,abw,ifreq,srate,prefix)
        self.ONvec = ONvec = [1.0]*fftsize
        self.OFFvec = OFFvec = [0.0]*fftsize

        ##################################################
        # Blocks
        ##################################################
        self.main_tab = Qt.QTabWidget()
        self.main_tab_widget_0 = Qt.QWidget()
        self.main_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_0)
        self.main_tab_grid_layout_0 = Qt.QGridLayout()
        self.main_tab_layout_0.addLayout(self.main_tab_grid_layout_0)
        self.main_tab.addTab(self.main_tab_widget_0, 'Spectral')
        self.main_tab_widget_1 = Qt.QWidget()
        self.main_tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_1)
        self.main_tab_grid_layout_1 = Qt.QGridLayout()
        self.main_tab_layout_1.addLayout(self.main_tab_grid_layout_1)
        self.main_tab.addTab(self.main_tab_widget_1, 'Continuum')
        self.top_layout.addWidget(self.main_tab)
        self.spec_tab = Qt.QTabWidget()
        self.spec_tab_widget_0 = Qt.QWidget()
        self.spec_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.spec_tab_widget_0)
        self.spec_tab_grid_layout_0 = Qt.QGridLayout()
        self.spec_tab_layout_0.addLayout(self.spec_tab_grid_layout_0)
        self.spec_tab.addTab(self.spec_tab_widget_0, 'Doppler')
        self.spec_tab_widget_1 = Qt.QWidget()
        self.spec_tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.spec_tab_widget_1)
        self.spec_tab_grid_layout_1 = Qt.QGridLayout()
        self.spec_tab_layout_1.addLayout(self.spec_tab_grid_layout_1)
        self.spec_tab.addTab(self.spec_tab_widget_1, 'Frequency')
        self.spec_tab_widget_2 = Qt.QWidget()
        self.spec_tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.spec_tab_widget_2)
        self.spec_tab_grid_layout_2 = Qt.QGridLayout()
        self.spec_tab_layout_2.addLayout(self.spec_tab_grid_layout_2)
        self.spec_tab.addTab(self.spec_tab_widget_2, 'Raw input(s)')
        self.main_tab_grid_layout_0.addWidget(self.spec_tab, 3, 0, 1, 4)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(3,4)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(0,4)]
        self._ifreq_tool_bar = Qt.QToolBar(self)
        self._ifreq_tool_bar.addWidget(Qt.QLabel('Frequency'+": "))
        self._ifreq_line_edit = Qt.QLineEdit(str(self.ifreq))
        self._ifreq_tool_bar.addWidget(self._ifreq_line_edit)
        self._ifreq_line_edit.returnPressed.connect(
        	lambda: self.set_ifreq(eng_notation.str_to_num(str(self._ifreq_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._ifreq_tool_bar, 0, 2, 1, 1)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(0,1)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self.fft_probe = blocks.probe_signal_vf(fftsize)
        self.fft2_probe = blocks.probe_signal_vf(fftsize)
        _dcblock_check_box = Qt.QCheckBox('Enable DC block')
        self._dcblock_choices = {True: 1, False: 0}
        self._dcblock_choices_inv = dict((v,k) for k,v in self._dcblock_choices.iteritems())
        self._dcblock_callback = lambda i: Qt.QMetaObject.invokeMethod(_dcblock_check_box, "setChecked", Qt.Q_ARG("bool", self._dcblock_choices_inv[i]))
        self._dcblock_callback(self.dcblock)
        _dcblock_check_box.stateChanged.connect(lambda i: self.set_dcblock(self._dcblock_choices[bool(i)]))
        self.main_tab_grid_layout_1.addWidget(_dcblock_check_box, 2, 0, 1, 1)
        [self.main_tab_grid_layout_1.setRowStretch(r,1) for r in range(2,3)]
        [self.main_tab_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self.corr_probe = blocks.probe_signal_c()
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Local Mean Sidereal Time'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.main_tab_grid_layout_0.addWidget(self._variable_qtgui_label_0_tool_bar, 1, 3, 1, 1)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(1,2)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(3,4)]

        def _tp_pacer_probe():
            while True:
                val = self.fft_probe.level()
                try:
                    self.set_tp_pacer(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (1))
        _tp_pacer_thread = threading.Thread(target=_tp_pacer_probe)
        _tp_pacer_thread.daemon = True
        _tp_pacer_thread.start()


        def _time_pacer_probe():
            while True:
                val = self.fft_probe.level()
                try:
                    self.set_time_pacer(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (2))
        _time_pacer_thread = threading.Thread(target=_time_pacer_probe)
        _time_pacer_thread.daemon = True
        _time_pacer_thread.start()

        self.single_pole_iir_filter_xx_3_0 = filter.single_pole_iir_filter_ff(0.25, fftsize)
        self.single_pole_iir_filter_xx_3 = filter.single_pole_iir_filter_ff(0.25, fftsize)
        self.single_pole_iir_filter_xx_2 = filter.single_pole_iir_filter_cc(1.0/((frate*240)*1.25*5), 1)
        self.single_pole_iir_filter_xx_1 = filter.single_pole_iir_filter_cc(1.0/(samp_rate*25), 1)
        self.single_pole_iir_filter_xx_0_0 = filter.single_pole_iir_filter_ff(0.01, fftsize)
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(0.01, fftsize)
        _set_baseline_push_button = Qt.QPushButton('Set Baseline')
        self._set_baseline_choices = {'Pressed': 1, 'Released': 0}
        _set_baseline_push_button.pressed.connect(lambda: self.set_set_baseline(self._set_baseline_choices['Pressed']))
        _set_baseline_push_button.released.connect(lambda: self.set_set_baseline(self._set_baseline_choices['Released']))
        self.main_tab_grid_layout_0.addWidget(_set_baseline_push_button, 0, 0, 1, 1)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(0,1)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self._secondary_lmst_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._secondary_lmst_label_formatter = None
        else:
          self._secondary_lmst_label_formatter = lambda x: str(x)

        self._secondary_lmst_label_tool_bar.addWidget(Qt.QLabel('LMST'+": "))
        self._secondary_lmst_label_label = Qt.QLabel(str(self._secondary_lmst_label_formatter(self.secondary_lmst_label)))
        self._secondary_lmst_label_tool_bar.addWidget(self._secondary_lmst_label_label)
        self.main_tab_grid_layout_1.addWidget(self._secondary_lmst_label_tool_bar, 0, 0, 1, 1)
        [self.main_tab_grid_layout_1.setRowStretch(r,1) for r in range(0,1)]
        [self.main_tab_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_vector_sink_f_1 = qtgui.vector_sink_f(
            fftsize,
            (ifreq-samp_rate/2)/1.0e6,
            fincr,
            "Frequency (MHz)",
            "Rel. Power(dB)",
            'Raw input spectra',
            2 # Number of inputs
        )
        self.qtgui_vector_sink_f_1.set_update_time(0.10)
        self.qtgui_vector_sink_f_1.set_y_axis(-120, 10)
        self.qtgui_vector_sink_f_1.enable_autoscale(True)
        self.qtgui_vector_sink_f_1.enable_grid(True)
        self.qtgui_vector_sink_f_1.set_x_axis_units("MHz")
        self.qtgui_vector_sink_f_1.set_y_axis_units("dB")
        self.qtgui_vector_sink_f_1.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_1.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_1.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_1.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_1.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_1_win = sip.wrapinstance(self.qtgui_vector_sink_f_1.pyqwidget(), Qt.QWidget)
        self.spec_tab_layout_2.addWidget(self._qtgui_vector_sink_f_1_win)
        self.qtgui_vector_sink_f_0_1 = qtgui.vector_sink_f(
            fftsize,
            (ifreq-samp_rate/2)/1.0e6,
            fincr,
            "Frequency (MHz)",
            "Rel. Power (dB)",
            "Frequency (MHz)",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_1.set_update_time(1.0/15)
        self.qtgui_vector_sink_f_0_1.set_y_axis(-1, +5)
        self.qtgui_vector_sink_f_0_1.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_1.enable_grid(True)
        self.qtgui_vector_sink_f_0_1.set_x_axis_units("MHz")
        self.qtgui_vector_sink_f_0_1.set_y_axis_units("dB")
        self.qtgui_vector_sink_f_0_1.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_1.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_1.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_1.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_1_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_1.pyqwidget(), Qt.QWidget)
        self.spec_tab_layout_1.addWidget(self._qtgui_vector_sink_f_0_1_win)
        self.qtgui_vector_sink_f_0_0 = qtgui.vector_sink_f(
            3600,
            0,
            -(1.0/60.0),
            "Time (Minutes)",
            "Deteced Power (arb units)",
            mode_map[mode],
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0.set_update_time(1.0/5.0)
        self.qtgui_vector_sink_f_0_0.set_y_axis(0.0, 1.5)
        self.qtgui_vector_sink_f_0_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_0.enable_grid(True)
        self.qtgui_vector_sink_f_0_0.set_x_axis_units("Mins")
        self.qtgui_vector_sink_f_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_layout_1.addWidget(self._qtgui_vector_sink_f_0_0_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            fftsize,
            start_km,
            km_incr,
            "Doppler Velocity (km/s)",
            "Rel. Power (dB)",
            "Doppler Velocity",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(1.0/15)
        self.qtgui_vector_sink_f_0.set_y_axis(-1, +5)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("km/s")
        self.qtgui_vector_sink_f_0.set_y_axis_units("dB")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.spec_tab_layout_0.addWidget(self._qtgui_vector_sink_f_0_win)
        self._ira_tool_bar = Qt.QToolBar(self)
        self._ira_tool_bar.addWidget(Qt.QLabel('Target Right Ascension'+": "))
        self._ira_line_edit = Qt.QLineEdit(str(self.ira))
        self._ira_tool_bar.addWidget(self._ira_line_edit)
        self._ira_line_edit.returnPressed.connect(
        	lambda: self.set_ira(eng_notation.str_to_num(str(self._ira_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._ira_tool_bar, 2, 0, 1, 1)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(2,3)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self._igain_tool_bar = Qt.QToolBar(self)
        self._igain_tool_bar.addWidget(Qt.QLabel('RF Gain'+": "))
        self._igain_line_edit = Qt.QLineEdit(str(self.igain))
        self._igain_tool_bar.addWidget(self._igain_line_edit)
        self._igain_line_edit.returnPressed.connect(
        	lambda: self.set_igain(eng_notation.str_to_num(str(self._igain_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._igain_tool_bar, 0, 3, 1, 1)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(0,1)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(3,4)]
        _fstop_check_box = Qt.QCheckBox('Fringe Stop')
        self._fstop_choices = {True: True, False: False}
        self._fstop_choices_inv = dict((v,k) for k,v in self._fstop_choices.iteritems())
        self._fstop_callback = lambda i: Qt.QMetaObject.invokeMethod(_fstop_check_box, "setChecked", Qt.Q_ARG("bool", self._fstop_choices_inv[i]))
        self._fstop_callback(self.fstop)
        _fstop_check_box.stateChanged.connect(lambda i: self.set_fstop(self._fstop_choices[bool(i)]))
        self.main_tab_grid_layout_1.addWidget(_fstop_check_box, 2, 1, 1, 1)
        [self.main_tab_grid_layout_1.setRowStretch(r,1) for r in range(2,3)]
        [self.main_tab_grid_layout_1.setColumnStretch(c,1) for c in range(1,2)]
        self._fringe_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._fringe_label_formatter = None
        else:
          self._fringe_label_formatter = lambda x: eng_notation.num_to_str(x)

        self._fringe_label_tool_bar.addWidget(Qt.QLabel('Fringe Period(secs)'+": "))
        self._fringe_label_label = Qt.QLabel(str(self._fringe_label_formatter(self.fringe_label)))
        self._fringe_label_tool_bar.addWidget(self._fringe_label_label)
        self.main_tab_grid_layout_1.addWidget(self._fringe_label_tool_bar, 0, 1, 1, 1)
        [self.main_tab_grid_layout_1.setRowStretch(r,1) for r in range(0,1)]
        [self.main_tab_grid_layout_1.setColumnStretch(c,1) for c in range(1,2)]
        self.fft_vxx_0_0 = fft.fft_vcc(fftsize, True, (window.blackmanharris(fftsize)), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(fftsize, True, (window.blackmanharris(fftsize)), True, 1)

        def _fft_probed_probe():
            while True:
                val = self.fft_probe.level()
                try:
                    self.set_fft_probed(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (15))
        _fft_probed_thread = threading.Thread(target=_fft_probed_probe)
        _fft_probed_thread.daemon = True
        _fft_probed_thread.start()

        self.fft_filter_xxx_0_0 = filter.fft_filter_ccf(1, (ifilt), 1)
        self.fft_filter_xxx_0_0.declare_sample_delay(0)
        self.fft_filter_xxx_0 = filter.fft_filter_ccf(1, (ifilt), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self._fft_avg_options = (4, 2, 1, )
        self._fft_avg_labels = ('Low', 'Medium', 'High', )
        self._fft_avg_tool_bar = Qt.QToolBar(self)
        self._fft_avg_tool_bar.addWidget(Qt.QLabel('FFT Averaging'+": "))
        self._fft_avg_combo_box = Qt.QComboBox()
        self._fft_avg_tool_bar.addWidget(self._fft_avg_combo_box)
        for label in self._fft_avg_labels: self._fft_avg_combo_box.addItem(label)
        self._fft_avg_callback = lambda i: Qt.QMetaObject.invokeMethod(self._fft_avg_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._fft_avg_options.index(i)))
        self._fft_avg_callback(self.fft_avg)
        self._fft_avg_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_fft_avg(self._fft_avg_options[i]))
        self.main_tab_grid_layout_0.addWidget(self._fft_avg_tool_bar, 1, 2, 1, 1)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(1,2)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]

        def _fft2_probed_probe():
            while True:
                val = self.fft2_probe.level()
                try:
                    self.set_fft2_probed(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (15))
        _fft2_probed_thread = threading.Thread(target=_fft2_probed_probe)
        _fft2_probed_thread.daemon = True
        _fft2_probed_thread.start()

        self._declination_tool_bar = Qt.QToolBar(self)
        self._declination_tool_bar.addWidget(Qt.QLabel('Declination'+": "))
        self._declination_line_edit = Qt.QLineEdit(str(self.declination))
        self._declination_tool_bar.addWidget(self._declination_line_edit)
        self._declination_line_edit.returnPressed.connect(
        	lambda: self.set_declination(eng_notation.str_to_num(str(self._declination_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._declination_tool_bar, 1, 0, 1, 1)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(1,2)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self._dcgain_options = (100, 1000, 10000, 100000, 1000000, )
        self._dcgain_labels = ('1e2', '1e3', '1e4', '1e5', '1e6', )
        self._dcgain_group_box = Qt.QGroupBox('Detector Gain')
        self._dcgain_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._dcgain_button_group = variable_chooser_button_group()
        self._dcgain_group_box.setLayout(self._dcgain_box)
        for i, label in enumerate(self._dcgain_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._dcgain_box.addWidget(radio_button)
        	self._dcgain_button_group.addButton(radio_button, i)
        self._dcgain_callback = lambda i: Qt.QMetaObject.invokeMethod(self._dcgain_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._dcgain_options.index(i)))
        self._dcgain_callback(self.dcgain)
        self._dcgain_button_group.buttonClicked[int].connect(
        	lambda i: self.set_dcgain(self._dcgain_options[i]))
        self.main_tab_grid_layout_1.addWidget(self._dcgain_group_box, 0, 2, 1, 1)
        [self.main_tab_grid_layout_1.setRowStretch(r,1) for r in range(0,1)]
        [self.main_tab_grid_layout_1.setColumnStretch(c,1) for c in range(2,3)]

        def _corr_probed_probe():
            while True:
                val = self.corr_probe.level()
                try:
                    self.set_corr_probed(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (15))
        _corr_probed_thread = threading.Thread(target=_corr_probed_probe)
        _corr_probed_thread.daemon = True
        _corr_probed_thread.start()

        _clear_baseline_push_button = Qt.QPushButton('Clear Baseline')
        self._clear_baseline_choices = {'Pressed': 1, 'Released': 0}
        _clear_baseline_push_button.pressed.connect(lambda: self.set_clear_baseline(self._clear_baseline_choices['Pressed']))
        _clear_baseline_push_button.released.connect(lambda: self.set_clear_baseline(self._clear_baseline_choices['Released']))
        self.main_tab_grid_layout_0.addWidget(_clear_baseline_push_button, 0, 1, 1, 1)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(0,1)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(1,2)]
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*3600, 40,True)
        self.blocks_sub_xx_0 = blocks.sub_cc(1)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fftsize)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fftsize)
        self.blocks_stream_to_streams_0 = blocks.stream_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*3600)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, fftsize, -20*math.log10(fftsize))
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, fftsize, -20*math.log10(fftsize))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((dcblock, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff(([0.0]*fftsize))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((frotate, ))
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_keep_one_in_n_1 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, int(samp_rate/10))
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_float*fftsize, (samp_rate/fftsize)/50)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*fftsize, (samp_rate/fftsize)/50)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/dcohen/airspyiq.dat', False)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(fftsize)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(fftsize)
        self.blocks_add_const_vxx_1 = blocks.add_const_vcc((1.0e-14, ))
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((curr_tp_vect))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((curr_dx))
        self._annotation_tool_bar = Qt.QToolBar(self)
        self._annotation_tool_bar.addWidget(Qt.QLabel('Quick Annotation'+": "))
        self._annotation_line_edit = Qt.QLineEdit(str(self.annotation))
        self._annotation_tool_bar.addWidget(self._annotation_line_edit)
        self._annotation_line_edit.returnPressed.connect(
        	lambda: self.set_annotation(str(str(self._annotation_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._annotation_tool_bar, 2, 1, 1, 3)
        [self.main_tab_grid_layout_0.setRowStretch(r,1) for r in range(2,3)]
        [self.main_tab_grid_layout_0.setColumnStretch(c,1) for c in range(1,4)]
        self._ang_range = Range(-180, 180, 2, 0, 200)
        self._ang_win = RangeWidget(self._ang_range, self.set_ang, 'Phase Angle Adjust', "slider", float)
        self.main_tab_grid_layout_1.addWidget(self._ang_win, 1, 0, 1, 1)
        [self.main_tab_grid_layout_1.setRowStretch(r,1) for r in range(1,2)]
        [self.main_tab_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_vector_sink_f_0_1, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.qtgui_vector_sink_f_0_0, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.single_pole_iir_filter_xx_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_streams_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_keep_one_in_n_1, 0), (self.single_pole_iir_filter_xx_2, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.single_pole_iir_filter_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.fft_probe, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.single_pole_iir_filter_xx_3, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.fft2_probe, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.single_pole_iir_filter_xx_3_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_stream_to_streams_0, 0), (self.fft_filter_xxx_0, 0))
        self.connect((self.blocks_stream_to_streams_0, 1), (self.fft_filter_xxx_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.corr_probe, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.fft_filter_xxx_0_0, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.fft_filter_xxx_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_1, 0), (self.blocks_keep_one_in_n_1, 0))
        self.connect((self.single_pole_iir_filter_xx_2, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.single_pole_iir_filter_xx_3, 0), (self.qtgui_vector_sink_f_1, 0))
        self.connect((self.single_pole_iir_filter_xx_3_0, 0), (self.qtgui_vector_sink_f_1, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "spectro_radiometer_filesource")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_abw(self):
        return self.abw

    def set_abw(self, abw):
        self.abw = abw
        self.set_anno_status(spectro_helper.do_annotation(self.ira,self.declination,self.baseline,self.annotation,self.bw,self.abw,self.ifreq,self.srate,self.prefix))

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna

    def get_baseline(self):
        return self.baseline

    def set_baseline(self, baseline):
        self.baseline = baseline
        self.set_frotate(spectro_helper.fringe_stop (self.tp_pacer, self.ra, self.decln, self.longitude, self.latitude, self.baseline, self.fstop, self.ang, self.ifreq))
        self.set_frate(((180.0/3.14159)*self.wlam/self.baseline)/math.cos(math.radians(self.decln)))
        self.set_anno_status(spectro_helper.do_annotation(self.ira,self.declination,self.baseline,self.annotation,self.bw,self.abw,self.ifreq,self.srate,self.prefix))

    def get_bbgain(self):
        return self.bbgain

    def set_bbgain(self, bbgain):
        self.bbgain = bbgain

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_ifilt(firdes.low_pass(1.0,self.samp_rate,self.bw/2.0,self.samp_rate/8) if self.bw > 0.0 else [1.0])
        self.set_anno_status(spectro_helper.do_annotation(self.ira,self.declination,self.baseline,self.annotation,self.bw,self.abw,self.ifreq,self.srate,self.prefix))

    def get_clock(self):
        return self.clock

    def set_clock(self, clock):
        self.clock = clock

    def get_dcg(self):
        return self.dcg

    def set_dcg(self, dcg):
        self.dcg = dcg
        self.set_dcgain(self.dcg)

    def get_decln(self):
        return self.decln

    def set_decln(self, decln):
        self.decln = decln
        self.set_frotate(spectro_helper.fringe_stop (self.tp_pacer, self.ra, self.decln, self.longitude, self.latitude, self.baseline, self.fstop, self.ang, self.ifreq))
        self.set_frate(((180.0/3.14159)*self.wlam/self.baseline)/math.cos(math.radians(self.decln)))
        self.set_declination(self.decln)

    def get_device(self):
        return self.device

    def set_device(self, device):
        self.device = device

    def get_fftsize(self):
        return self.fftsize

    def set_fftsize(self, fftsize):
        self.fftsize = fftsize
        self.set_km_incr((((self.samp_rate/self.fftsize)/self.ifreq)*299792)*-1.0)
        self.set_fincr((self.samp_rate/1.0e6)/self.fftsize)
        self.set_tp_pacer([-100.0]*self.fftsize)
        self.set_time_pacer([-100.0]*self.fftsize)
        self.set_fft_probed([-100.0]*self.fftsize)
        self.set_fft2_probed([-100.0]*self.fftsize)
        self.blocks_multiply_const_vxx_1.set_k(([0.0]*self.fftsize))
        self.blocks_keep_one_in_n_0_0.set_n((self.samp_rate/self.fftsize)/50)
        self.blocks_keep_one_in_n_0.set_n((self.samp_rate/self.fftsize)/50)
        self.set_ONvec([1.0]*self.fftsize)
        self.set_OFFvec([0.0]*self.fftsize)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.set_ifreq(self.frequency)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_igain(self.gain)

    def get_ifgain(self):
        return self.ifgain

    def set_ifgain(self, ifgain):
        self.ifgain = ifgain

    def get_latitude(self):
        return self.latitude

    def set_latitude(self, latitude):
        self.latitude = latitude
        self.set_frotate(spectro_helper.fringe_stop (self.tp_pacer, self.ra, self.decln, self.longitude, self.latitude, self.baseline, self.fstop, self.ang, self.ifreq))

    def get_longitude(self):
        return self.longitude

    def set_longitude(self, longitude):
        self.longitude = longitude
        self.set_frotate(spectro_helper.fringe_stop (self.tp_pacer, self.ra, self.decln, self.longitude, self.latitude, self.baseline, self.fstop, self.ang, self.ifreq))
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(spectro_helper.lmst_string(self.time_pacer,self.longitude)))
        self.set_secondary_lmst_label(self._secondary_lmst_label_formatter(spectro_helper.lmst_string(self.time_pacer,self.longitude)))
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))

    def get_ppstime(self):
        return self.ppstime

    def set_ppstime(self, ppstime):
        self.ppstime = ppstime

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))
        self.set_anno_status(spectro_helper.do_annotation(self.ira,self.declination,self.baseline,self.annotation,self.bw,self.abw,self.ifreq,self.srate,self.prefix))

    def get_ra(self):
        return self.ra

    def set_ra(self, ra):
        self.ra = ra
        self.set_frotate(spectro_helper.fringe_stop (self.tp_pacer, self.ra, self.decln, self.longitude, self.latitude, self.baseline, self.fstop, self.ang, self.ifreq))
        self.set_ira(self.ra)

    def get_rfilist(self):
        return self.rfilist

    def set_rfilist(self, rfilist):
        self.rfilist = rfilist
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))

    def get_srate(self):
        return self.srate

    def set_srate(self, srate):
        self.srate = srate
        self.set_samp_rate(int(self.srate))
        self.set_anno_status(spectro_helper.do_annotation(self.ira,self.declination,self.baseline,self.annotation,self.bw,self.abw,self.ifreq,self.srate,self.prefix))

    def get_zerotime(self):
        return self.zerotime

    def set_zerotime(self, zerotime):
        self.zerotime = zerotime
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))

    def get_ifreq(self):
        return self.ifreq

    def set_ifreq(self, ifreq):
        self.ifreq = ifreq
        self.set_start_km(((self.samp_rate/2)/self.ifreq)*299792)
        self.set_km_incr((((self.samp_rate/self.fftsize)/self.ifreq)*299792)*-1.0)
        Qt.QMetaObject.invokeMethod(self._ifreq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ifreq)))
        self.set_frotate(spectro_helper.fringe_stop (self.tp_pacer, self.ra, self.decln, self.longitude, self.latitude, self.baseline, self.fstop, self.ang, self.ifreq))
        self.set_wlam(299792000.0/self.ifreq)
        self.qtgui_vector_sink_f_1.set_x_axis((self.ifreq-self.samp_rate/2)/1.0e6, self.fincr)
        self.qtgui_vector_sink_f_0_1.set_x_axis((self.ifreq-self.samp_rate/2)/1.0e6, self.fincr)
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))
        self.set_anno_status(spectro_helper.do_annotation(self.ira,self.declination,self.baseline,self.annotation,self.bw,self.abw,self.ifreq,self.srate,self.prefix))

    def get_wlam(self):
        return self.wlam

    def set_wlam(self, wlam):
        self.wlam = wlam
        self.set_frate(((180.0/3.14159)*self.wlam/self.baseline)/math.cos(math.radians(self.decln)))

    def get_tp_pacer(self):
        return self.tp_pacer

    def set_tp_pacer(self, tp_pacer):
        self.tp_pacer = tp_pacer
        self.set_frotate(spectro_helper.fringe_stop (self.tp_pacer, self.ra, self.decln, self.longitude, self.latitude, self.baseline, self.fstop, self.ang, self.ifreq))
        self.set_curr_tp_vect(spectro_helper.get_tp_vect(self.tp_pacer))

    def get_time_pacer(self):
        return self.time_pacer

    def set_time_pacer(self, time_pacer):
        self.time_pacer = time_pacer
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(spectro_helper.lmst_string(self.time_pacer,self.longitude)))
        self.set_secondary_lmst_label(self._secondary_lmst_label_formatter(spectro_helper.lmst_string(self.time_pacer,self.longitude)))

    def get_set_baseline(self):
        return self.set_baseline

    def set_set_baseline(self, set_baseline):
        self.set_baseline = set_baseline
        self.set_baseline_set_status(spectro_helper.baseline_setter(self.set_baseline))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_start_km(((self.samp_rate/2)/self.ifreq)*299792)
        self.set_km_incr((((self.samp_rate/self.fftsize)/self.ifreq)*299792)*-1.0)
        self.set_ifilt(firdes.low_pass(1.0,self.samp_rate,self.bw/2.0,self.samp_rate/8) if self.bw > 0.0 else [1.0])
        self.set_fincr((self.samp_rate/1.0e6)/self.fftsize)
        self.single_pole_iir_filter_xx_1.set_taps(1.0/(self.samp_rate*25))
        self.qtgui_vector_sink_f_1.set_x_axis((self.ifreq-self.samp_rate/2)/1.0e6, self.fincr)
        self.qtgui_vector_sink_f_0_1.set_x_axis((self.ifreq-self.samp_rate/2)/1.0e6, self.fincr)
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))
        self.blocks_keep_one_in_n_1.set_n(int(self.samp_rate/10))
        self.blocks_keep_one_in_n_0_0.set_n((self.samp_rate/self.fftsize)/50)
        self.blocks_keep_one_in_n_0.set_n((self.samp_rate/self.fftsize)/50)

    def get_ira(self):
        return self.ira

    def set_ira(self, ira):
        self.ira = ira
        Qt.QMetaObject.invokeMethod(self._ira_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ira)))
        self.set_anno_status(spectro_helper.do_annotation(self.ira,self.declination,self.baseline,self.annotation,self.bw,self.abw,self.ifreq,self.srate,self.prefix))

    def get_fstop(self):
        return self.fstop

    def set_fstop(self, fstop):
        self.fstop = fstop
        self.set_frotate(spectro_helper.fringe_stop (self.tp_pacer, self.ra, self.decln, self.longitude, self.latitude, self.baseline, self.fstop, self.ang, self.ifreq))
        self._fstop_callback(self.fstop)

    def get_frate(self):
        return self.frate

    def set_frate(self, frate):
        self.frate = frate
        self.single_pole_iir_filter_xx_2.set_taps(1.0/((self.frate*240)*1.25*5))
        self.set_fringe_label(self._fringe_label_formatter(self.frate*240.0))

    def get_fft_probed(self):
        return self.fft_probed

    def set_fft_probed(self, fft_probed):
        self.fft_probed = fft_probed
        self.set_curr_dx(spectro_helper.curr_diff(self.fft_probed,self.enable_normalize))
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))

    def get_fft_avg(self):
        return self.fft_avg

    def set_fft_avg(self, fft_avg):
        self.fft_avg = fft_avg
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))
        self._fft_avg_callback(self.fft_avg)

    def get_fft2_probed(self):
        return self.fft2_probed

    def set_fft2_probed(self, fft2_probed):
        self.fft2_probed = fft2_probed
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))

    def get_enable_normalize(self):
        return self.enable_normalize

    def set_enable_normalize(self, enable_normalize):
        self.enable_normalize = enable_normalize
        self.set_curr_dx(spectro_helper.curr_diff(self.fft_probed,self.enable_normalize))
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))

    def get_declination(self):
        return self.declination

    def set_declination(self, declination):
        self.declination = declination
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))
        Qt.QMetaObject.invokeMethod(self._declination_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.declination)))
        self.set_anno_status(spectro_helper.do_annotation(self.ira,self.declination,self.baseline,self.annotation,self.bw,self.abw,self.ifreq,self.srate,self.prefix))

    def get_dcgain(self):
        return self.dcgain

    def set_dcgain(self, dcgain):
        self.dcgain = dcgain
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))
        self._dcgain_callback(self.dcgain)

    def get_corr_probed(self):
        return self.corr_probed

    def set_corr_probed(self, corr_probed):
        self.corr_probed = corr_probed
        self.set_fft_log_status(spectro_helper.fft_log(self.fft_probed,self.fft2_probed,self.corr_probed,self.ifreq,self.samp_rate,self.longitude,self.enable_normalize,self.prefix,self.declination,self.rfilist,self.dcgain,self.fft_avg,self.mode,self.zerotime))

    def get_clear_baseline(self):
        return self.clear_baseline

    def set_clear_baseline(self, clear_baseline):
        self.clear_baseline = clear_baseline
        self.set_baseline_clear_status(spectro_helper.baseline_clearer(self.clear_baseline))

    def get_annotation(self):
        return self.annotation

    def set_annotation(self, annotation):
        self.annotation = annotation
        Qt.QMetaObject.invokeMethod(self._annotation_line_edit, "setText", Qt.Q_ARG("QString", str(self.annotation)))
        self.set_anno_status(spectro_helper.do_annotation(self.ira,self.declination,self.baseline,self.annotation,self.bw,self.abw,self.ifreq,self.srate,self.prefix))

    def get_ang(self):
        return self.ang

    def set_ang(self, ang):
        self.ang = ang
        self.set_frotate(spectro_helper.fringe_stop (self.tp_pacer, self.ra, self.decln, self.longitude, self.latitude, self.baseline, self.fstop, self.ang, self.ifreq))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_start_km(self):
        return self.start_km

    def set_start_km(self, start_km):
        self.start_km = start_km
        self.qtgui_vector_sink_f_0.set_x_axis(self.start_km, self.km_incr)

    def get_secondary_lmst_label(self):
        return self.secondary_lmst_label

    def set_secondary_lmst_label(self, secondary_lmst_label):
        self.secondary_lmst_label = secondary_lmst_label
        Qt.QMetaObject.invokeMethod(self._secondary_lmst_label_label, "setText", Qt.Q_ARG("QString", self.secondary_lmst_label))

    def get_mode_map(self):
        return self.mode_map

    def set_mode_map(self, mode_map):
        self.mode_map = mode_map

    def get_km_incr(self):
        return self.km_incr

    def set_km_incr(self, km_incr):
        self.km_incr = km_incr
        self.qtgui_vector_sink_f_0.set_x_axis(self.start_km, self.km_incr)

    def get_igain(self):
        return self.igain

    def set_igain(self, igain):
        self.igain = igain
        Qt.QMetaObject.invokeMethod(self._igain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.igain)))

    def get_ifilt(self):
        return self.ifilt

    def set_ifilt(self, ifilt):
        self.ifilt = ifilt
        self.fft_filter_xxx_0_0.set_taps((self.ifilt))
        self.fft_filter_xxx_0.set_taps((self.ifilt))

    def get_frotate(self):
        return self.frotate

    def set_frotate(self, frotate):
        self.frotate = frotate
        self.blocks_multiply_const_vxx_0.set_k((self.frotate, ))

    def get_fringe_label(self):
        return self.fringe_label

    def set_fringe_label(self, fringe_label):
        self.fringe_label = fringe_label
        Qt.QMetaObject.invokeMethod(self._fringe_label_label, "setText", Qt.Q_ARG("QString", self.fringe_label))

    def get_fincr(self):
        return self.fincr

    def set_fincr(self, fincr):
        self.fincr = fincr
        self.qtgui_vector_sink_f_1.set_x_axis((self.ifreq-self.samp_rate/2)/1.0e6, self.fincr)
        self.qtgui_vector_sink_f_0_1.set_x_axis((self.ifreq-self.samp_rate/2)/1.0e6, self.fincr)

    def get_fft_log_status(self):
        return self.fft_log_status

    def set_fft_log_status(self, fft_log_status):
        self.fft_log_status = fft_log_status

    def get_dcblock(self):
        return self.dcblock

    def set_dcblock(self, dcblock):
        self.dcblock = dcblock
        self._dcblock_callback(self.dcblock)
        self.blocks_multiply_const_vxx_2.set_k((self.dcblock, ))

    def get_curr_tp_vect(self):
        return self.curr_tp_vect

    def set_curr_tp_vect(self, curr_tp_vect):
        self.curr_tp_vect = curr_tp_vect
        self.blocks_add_const_vxx_0_0.set_k((self.curr_tp_vect))

    def get_curr_dx(self):
        return self.curr_dx

    def set_curr_dx(self, curr_dx):
        self.curr_dx = curr_dx
        self.blocks_add_const_vxx_0.set_k((self.curr_dx))

    def get_baseline_set_status(self):
        return self.baseline_set_status

    def set_baseline_set_status(self, baseline_set_status):
        self.baseline_set_status = baseline_set_status

    def get_baseline_clear_status(self):
        return self.baseline_clear_status

    def set_baseline_clear_status(self, baseline_clear_status):
        self.baseline_clear_status = baseline_clear_status

    def get_anno_status(self):
        return self.anno_status

    def set_anno_status(self, anno_status):
        self.anno_status = anno_status

    def get_ONvec(self):
        return self.ONvec

    def set_ONvec(self, ONvec):
        self.ONvec = ONvec

    def get_OFFvec(self):
        return self.OFFvec

    def set_OFFvec(self, OFFvec):
        self.OFFvec = OFFvec


def argument_parser():
    description = 'Testing with file source'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "", "--abw", dest="abw", type="eng_float", default=eng_notation.num_to_str(4.0e6),
        help="Set Analog  bandwidth [default=%default]")
    parser.add_option(
        "", "--antenna", dest="antenna", type="string", default='RX2',
        help="Set Antenna [default=%default]")
    parser.add_option(
        "", "--baseline", dest="baseline", type="eng_float", default=eng_notation.num_to_str(99.3),
        help="Set Baseline length [default=%default]")
    parser.add_option(
        "", "--bbgain", dest="bbgain", type="eng_float", default=eng_notation.num_to_str(5),
        help="Set Baseband Gain [default=%default]")
    parser.add_option(
        "", "--bw", dest="bw", type="eng_float", default=eng_notation.num_to_str(-1.0e6),
        help="Set Bandwidth [default=%default]")
    parser.add_option(
        "", "--clock", dest="clock", type="string", default='default',
        help="Set Clock Source [default=%default]")
    parser.add_option(
        "", "--dcg", dest="dcg", type="intx", default=100,
        help="Set Detector DC Gain [default=%default]")
    parser.add_option(
        "", "--decln", dest="decln", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Observing Declination [default=%default]")
    parser.add_option(
        "", "--device", dest="device", type="string", default="rtl=0 file=/dev/zero,rate=5e6",
        help="Set SDR Device Name [default=%default]")
    parser.add_option(
        "", "--fftsize", dest="fftsize", type="intx", default=2048,
        help="Set FFT size [default=%default]")
    parser.add_option(
        "", "--frequency", dest="frequency", type="eng_float", default=eng_notation.num_to_str(1420.4058e6),
        help="Set Center Frequency [default=%default]")
    parser.add_option(
        "", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(30),
        help="Set RF Gain [default=%default]")
    parser.add_option(
        "", "--ifgain", dest="ifgain", type="eng_float", default=eng_notation.num_to_str(5),
        help="Set IF Gain [default=%default]")
    parser.add_option(
        "", "--latitude", dest="latitude", type="eng_float", default=eng_notation.num_to_str(44.9),
        help="Set Local Latitude [default=%default]")
    parser.add_option(
        "", "--longitude", dest="longitude", type="eng_float", default=eng_notation.num_to_str(-76.03),
        help="Set Local Longitude [default=%default]")
    parser.add_option(
        "", "--mode", dest="mode", type="string", default="total",
        help="Set Operation Mode [default=%default]")
    parser.add_option(
        "", "--ppstime", dest="ppstime", type="string", default='internal',
        help="Set Time Source [default=%default]")
    parser.add_option(
        "", "--prefix", dest="prefix", type="string", default="h1",
        help="Set Data File Prefix [default=%default]")
    parser.add_option(
        "", "--ra", dest="ra", type="eng_float", default=eng_notation.num_to_str(12.0),
        help="Set Target RA [default=%default]")
    parser.add_option(
        "", "--rfilist", dest="rfilist", type="string", default="",
        help="Set RFI Frequency List [default=%default]")
    parser.add_option(
        "", "--srate", dest="srate", type="eng_float", default=eng_notation.num_to_str(2.56e6),
        help="Set Sample rate [default=%default]")
    parser.add_option(
        "", "--zerotime", dest="zerotime", type="eng_float", default=eng_notation.num_to_str(99.3),
        help="Set SIdereal time for auto baseline set [default=%default]")
    return parser


def main(top_block_cls=spectro_radiometer_filesource, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(abw=options.abw, antenna=options.antenna, baseline=options.baseline, bbgain=options.bbgain, bw=options.bw, clock=options.clock, dcg=options.dcg, decln=options.decln, device=options.device, fftsize=options.fftsize, frequency=options.frequency, gain=options.gain, ifgain=options.ifgain, latitude=options.latitude, longitude=options.longitude, mode=options.mode, ppstime=options.ppstime, prefix=options.prefix, ra=options.ra, rfilist=options.rfilist, srate=options.srate, zerotime=options.zerotime)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
