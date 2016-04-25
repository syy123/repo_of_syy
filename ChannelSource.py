# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:44:22 2016

@author: Administrator
"""
from config import *
from ChannelSourceFunction import *
import sys
class ChannelSource(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)       
        self.CreateSizer()
        self.CreateElementForLeftSizer()
        self.CreateElementForRightSizer()
        self.AddElementForLeftSizer()
        self.AddElementForRightSizer()
        self.ConfigSizersLayout()
    def CreateSizer(self):
        self.TopSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.left_vsizer = wx.BoxSizer(wx.VERTICAL)
        self.right_hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sub_left_vsizer = wx.BoxSizer(wx.VERTICAL)
    def CreateElementForLeftSizer(self):
        self.SymbolNumberBox()
        self.SymbolRateBox()
        self.SimpleBox()
        self.CarrierBox()
        self.ImpulseChoiceBox()
        self.CodeChoiceBox()
        self.RZRatioBox()
        self.RaisedCosineBox()
        self.PartialResponseBox()
        self.GausseFilterBox()
        self.ModulateChoiceBox()
        self.FigureShowBox()
        self.ButtonBox()
    def CreateElementForRightSizer(self):
        self.leftUpFigure = Figure(figsize = (4, 4))
        self.axes = self.leftUpFigure.add_axes([0.1, 0.1, 0.8, 0.8])
        self.leftUpCanvas = FigureCanvas(self, -1, self.leftUpFigure)
        self.leftUpNavigation = NavigationToolbar(self.leftUpCanvas) 
        self.leftUpCanvas.mpl_connect('motion_notify_event', self.LeftUpCanvasOnMouseMove);
        self.LeftStaticText = wx.StaticText(self, -1, label = 'Mouse Location');
    def LeftUpCanvasOnMouseMove(self, event):
        ex=event.xdata   
        ey=event.ydata   
        if ex and ey:
            self.LeftStaticText.SetLabel('(%s, %s)' % (ex, ey))
    def AddElementForRightSizer(self):
        self.sub_left_vsizer.Add(self.leftUpNavigation, 0, wx.ALL|wx.EXPAND)
        self.sub_left_vsizer.Add(self.LeftStaticText, 0, wx.ALL | wx.EXPAND);
        self.sub_left_vsizer.Add(self.leftUpCanvas, 1, wx.ALL|wx.EXPAND)
        self.right_hsizer.Add(self.sub_left_vsizer, 1, wx.ALL|wx.EXPAND)
    def AddElementForLeftSizer(self):        
        self.left_vsizer.Add(self.symbolNumberBox, 1, wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Add(self.symbolRateBox, 1, wx.ALL|wx.EXPAND, 2)       
        self.left_vsizer.Add(self.sampleBox, 1, wx.ALL|wx.EXPAND, 2)     
        self.left_vsizer.Add(self.ImpulseChoiceSizer, 1, wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Add(self.RaisedCosineSizer, 1,  wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Add(self.partialBox, 1,  wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Add(self.gaussBox, 1,  wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Add(self.CodeChoiceSizer, 1, wx.ALL|wx.EXPAND, 2) 
        self.left_vsizer.Add(self.rectRatioBox, 1,  wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Add(self.ModulateSizer, 1, wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Add(self.carrierBox, 1, wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Add(self.FigureSizer, 1, wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Add(self.buttonBox, 1, wx.ALL|wx.EXPAND, 2)
        self.left_vsizer.Hide(self.RaisedCosineSizer)
        self.left_vsizer.Hide(self.partialBox)
        self.left_vsizer.Hide(self.gaussBox)
        self.left_vsizer.Hide(self.CodeChoiceSizer)
        self.left_vsizer.Hide(self.rectRatioBox)

    def ConfigSizersLayout(self):
        self.TopSizer.Add(self.left_vsizer, 1, wx.ALL|wx.EXPAND, 2)
        self.TopSizer.Add(self.right_hsizer,4, wx.ALL|wx.EXPAND, 2)
        self.SetSizerAndFit(self.TopSizer)
        self.TopSizer.SetSizeHints(self)
    def SymbolNumberBox(self):
        self.staticSymbolNumBox = wx.StaticBox(self, -1, u"码元数量")
        self.symbolNumberBox = wx.StaticBoxSizer(self.staticSymbolNumBox, wx.VERTICAL)      
        self.NumberTextCtrl = wx.TextCtrl(self, -1, "100",style = wx.TE_PROCESS_ENTER)
        self.NumberTextCtrl.SetToolTipString(u"按回车键结束输入")
        self.NumberTextCtrl.Bind(wx.EVT_TEXT_ENTER, self.TextNumber)
        self.symbolNumberBox.Add(self.NumberTextCtrl, 1, wx.ALL|wx.EXPAND, 2)    
    def SymbolRateBox(self):
        self.staticSymbolRateBox = wx.StaticBox(self, -1, u"码元速率(B/s)")
        self.symbolRateBox = wx.StaticBoxSizer(self.staticSymbolRateBox, wx.VERTICAL)
        self.RateTextCtrl = wx.TextCtrl(self, -1, "1", style = wx.TE_PROCESS_ENTER)
        self.RateTextCtrl.SetToolTipString(u"按回车键结束输入")
        self.RateTextCtrl.Bind(wx.EVT_TEXT_ENTER, self.TextNumber)
        self.symbolRateBox.Add(self.RateTextCtrl, 1, wx.ALL|wx.EXPAND, 2)
    def SimpleBox(self):
        self.staticSampleBox = wx.StaticBox(self, -1, u"采样频率")
        self.sampleBox = wx.StaticBoxSizer(self.staticSampleBox, wx.VERTICAL)
        self.SampleTextCtrl = wx.TextCtrl(self, -1, "20", style = wx.TE_PROCESS_ENTER)
        self.SampleTextCtrl.SetToolTipString(u"按回车键结束输入")
        self.SampleTextCtrl.Bind(wx.EVT_TEXT_ENTER, self.TextNumber)
        self.sampleBox.Add(self.SampleTextCtrl, 1, wx.ALL|wx.EXPAND, 2)
    def CarrierBox(self):
        self.statiCarrierBox = wx.StaticBox(self, -1, u"载波频率")
        self.carrierBox = wx.StaticBoxSizer(self.statiCarrierBox, wx.VERTICAL)
        self.CarrierTextCtrl = wx.TextCtrl(self, -1, "0", style = wx.TE_PROCESS_ENTER)
        self.CarrierTextCtrl.SetToolTipString(u"按回车键结束输入")
        self.CarrierTextCtrl.Bind(wx.EVT_TEXT_ENTER, self.TextNumber)
        self.carrierBox.Add(self.CarrierTextCtrl, 1, wx.ALL|wx.EXPAND, 2)
    def TextNumber(self, event):
        self.number = int(self.NumberTextCtrl.GetValue())
        self.rate = int(self.RateTextCtrl.GetValue())
        self.fc = int(self.CarrierTextCtrl.GetValue())
        self.Fs = int(self.SampleTextCtrl.GetValue())
        event.Skip()
    def RZRatioBox(self):
        self.staticRatioBox = wx.StaticBox(self, -1, u"矩形脉冲")
        self.rectRatioBox = wx.StaticBoxSizer(self.staticRatioBox, wx.VERTICAL)
        self.ratioBox = SliderBox(self, -1, u"脉冲宽度", 5, 1, int(self.SampleTextCtrl.GetValue()), 1,1)
        self.ratioBox.slider.Bind(wx.EVT_SLIDER, self.OnRatioSlider)
        self.rectRatioBox.Add(self.ratioBox.staticText, 0, wx.CENTER)
        self.rectRatioBox.Add(self.ratioBox.slider, 1, wx.ALL|wx.EXPAND, 2)
        self.rectRatioBox.Add(self.ratioBox.textCtrl, 1, wx.ALL|wx.EXPAND, 2)
    def OnRatioSlider(self, event):
        self.ratioBox.textCtrl.SetValue(str(int(self.ratioBox.slider.GetValue())/1))
        event.Skip()
    def RaisedCosineBox(self):
        self.alphBox = SliderBox(self, -1, u"滚降系数", 0, 0, 10, 1, 10)      
        self.alphBox.slider.Bind(wx.EVT_SLIDER, self.OnAlphSlider)
        self.staticRaisedBox = wx.StaticBox(self, -1, u"升余弦脉冲")
        self.RaisedCosineSizer = wx.StaticBoxSizer(self.staticRaisedBox, wx.VERTICAL)
        self.RaisedCosineSizer.Add(self.alphBox.staticText, 0, wx.CENTER)
        self.RaisedCosineSizer.Add(self.alphBox.slider, 1, wx.ALL|wx.EXPAND, 2)
        self.RaisedCosineSizer.Add(self.alphBox.textCtrl, 1, wx.ALL|wx.EXPAND, 2)    
    def OnAlphSlider(self, event):
        self.alphBox.textCtrl.SetValue(str(float(self.alphBox.slider.GetValue()) / 10))
        self.alph = float(self.alphBox.slider.GetValue()) / 10          
        event.Skip()
    def PartialResponseBox(self):
        self.staticPartialBox = wx.StaticBox(self, -1, u"部分响应")
        self.partialBox = wx.StaticBoxSizer(self.staticPartialBox, wx.VERTICAL)
        self.typeChoice = wx.Choice(self, -1, choices = GetPartialTypeChoiceList())
        self.typeChoice.Bind(wx.EVT_CHOICE, self.PartialType)
        self.partialBox.Add(self.typeChoice, 1, wx.ALL|wx.EXPAND, 2)
    def PartialType(self, event):
        self.typeChoice.GetSelection()
        print 'type: ',self.typeChoice.GetSelection()
    def GausseFilterBox(self):
        self.staticGaussBox = wx.StaticBox(self, -1, u"高斯滤波")
        self.sigmaBox = SliderBox(self, -1, u"方差", 4, 1, 10, 1, 10)
        self.sigmaBox.slider.Bind(wx.EVT_SLIDER, self.OnSigmaSlider)
        self.gaussBox = wx.StaticBoxSizer(self.staticGaussBox, wx.VERTICAL)
        self.gaussBox.Add(self.sigmaBox.staticText, 0, wx.CENTER)
        self.gaussBox.Add(self.sigmaBox.slider, 1, wx.ALL|wx.EXPAND, 2)
        self.gaussBox.Add(self.sigmaBox.textCtrl, 1, wx.ALL|wx.EXPAND, 2)
    def OnSigmaSlider(self, event):
        self.sigmaBox.textCtrl.SetValue(str(float(self.sigmaBox.slider.GetValue())/10))
        self.sigma = float(self.sigmaBox.slider.GetValue())/10
        event.Skip()
    def ImpulseChoiceBox(self):
        self.impulseChoiceBox = wx.Choice(self, -1, choices = GetImpulseChoiceList())
        self.staticImpulse = wx.StaticBox(self, -1, u"脉冲成型")
        self.ImpulseChoiceSizer = wx.StaticBoxSizer(self.staticImpulse, wx.VERTICAL)
        self.ImpulseChoiceSizer.Add(self.impulseChoiceBox, 1, wx.ALL|wx.EXPAND, 2)
        self.impulseChoiceBox.Bind(wx.EVT_CHOICE, self.ChoiceBoxSwitchFunc)
    def ChoiceBoxSwitchFunc(self, event):
        
        if self.impulseChoiceBox.GetLabelText() == RaisedCosineBoxName():
            print u'升余弦脉冲'
            self.left_vsizer.Show(self.RaisedCosineSizer)
            self.left_vsizer.Hide(self.partialBox)
            self.left_vsizer.Hide(self.gaussBox)
            self.left_vsizer.Hide(self.CodeChoiceSizer)
            self.left_vsizer.Hide(self.rectRatioBox)
            self.left_vsizer.Layout() #强制重绘
        elif self.impulseChoiceBox.GetLabelText() == PartialBoxName():
            print u'部分响应波形'
            self.left_vsizer.Show(self.partialBox)
            self.left_vsizer.Hide(self.RaisedCosineSizer)
            self.left_vsizer.Hide(self.gaussBox)
            self.left_vsizer.Hide(self.CodeChoiceSizer)
            self.left_vsizer.Hide(self.rectRatioBox)
            self.left_vsizer.Layout()
        elif self.impulseChoiceBox.GetLabelText() == GaussBoxName():
            print u'高斯脉冲'
            self.left_vsizer.Show(self.gaussBox)
            self.left_vsizer.Hide(self.RaisedCosineSizer)
            self.left_vsizer.Hide(self.partialBox)
            self.left_vsizer.Hide(self.CodeChoiceSizer)
            self.left_vsizer.Hide(self.rectRatioBox)
            self.left_vsizer.Layout()
        else:
            print u'矩形脉冲'
            self.left_vsizer.Show(self.CodeChoiceSizer)
            self.left_vsizer.Show(self.rectRatioBox)
            self.left_vsizer.Hide(self.RaisedCosineSizer)
            self.left_vsizer.Hide(self.partialBox)
            self.left_vsizer.Hide(self.gaussBox)
            self.left_vsizer.Layout()
            
    def CodeChoiceBox(self):
        self.codeChoiceBox = wx.Choice(self, -1, choices = GetCodeChoiceList())
        self.staticCode = wx.StaticBox(self, -1, u"码型选择")
        self.CodeChoiceSizer = wx.StaticBoxSizer(self.staticCode, wx.VERTICAL)
        self.CodeChoiceSizer.Add(self.codeChoiceBox, 1, wx.ALL|wx.EXPAND, 2)
        self.codeChoiceBox.Bind(wx.EVT_CHOICE, self.Code)
    def Code(self, event):
        self.codeChoiceBox.GetSelection()
    def ModulateChoiceBox(self):
        self.modulateChoiceBox = wx.Choice(self, -1, choices = GetModulateChoiecList())
        self.modulateChoiceBox.SetStringSelection('QPSK')
        self.modulateChoiceBox.Bind(wx.EVT_CHOICE, self.ModulateChoice)
        self.staticModulate = wx.StaticBox(self, -1, u"调制方式")
        self.ModulateSizer = wx.StaticBoxSizer(self.staticModulate, wx.VERTICAL)
        self.ModulateSizer.Add(self.modulateChoiceBox, 1, wx.ALL|wx.EXPAND, 2)
    def ModulateChoice(self, event):    
        self.modulateChoiceBox.GetSelection()
        print 'modulate:',self.modulateChoiceBox.GetSelection()
    def FigureShowBox(self):
        self.figureChoiceBox = wx.CheckListBox(self, -1,size = (100, 150), choices = GetFigureChoiceList())
        self.figureChoiceBox.Bind(wx.EVT_CHECKLISTBOX, self.FigureShow)
        self.staticFigure = wx.StaticBox(self, -1, u"图形显示")
        self.FigureSizer = wx.StaticBoxSizer(self.staticFigure, wx.VERTICAL)
        self.FigureSizer.Add(self.figureChoiceBox, 1, wx.ALL|wx.EXPAND, 2)
    def FigureShow(self, event):
        self.count = 0
        self.shapetime = 0
        self.shapefreq = 0
        self.modutime = 0
        self.modufreq = 0
        self.star = 0
        if self.figureChoiceBox.IsChecked(0):            
            self.count +=1
            self.shapetime = self.count
        if self.figureChoiceBox.IsChecked(1):
            self.count +=1
            self.shapefreq = self.count
        if self.figureChoiceBox.IsChecked(2):          
            self.count +=1
            self.modutime = self.count
        if self.figureChoiceBox.IsChecked(3):
            self.count +=1            
            self.modufreq = self.count
        if self.figureChoiceBox.IsChecked(4):          
            self.count +=1
            self.star = self.count
    def PlotConfig(self, event):
        self.m = 1
        self.n = 1
        if self.count == 1:
            self.m = 1
            self.n = 1
            self.Draw(self)
        elif self.count == 2:
            self.m = 2
            self.n = 1
            self.Draw(self)
        elif self.count == 3:
            self.m = 3
            self.n = 1
            self.Draw(self)
        elif self.count == 4:
            self.m = 2
            self.n = 2
            self.Draw(self)      
    def Draw(self,event):
        self.leftUpFigure.clear()
        self.axes.clear();   
        if self.shapetime: 
            self.axes = self.leftUpFigure.add_subplot(self.m,self.n,self.shapetime)
            self.axes.plot(self.x,self.impulse,label = self.label)
            self.axes.legend(loc='lower right')           
            self.axes.set_xlabel(u"时间/s")
            self.axes.set_title(u"脉冲时域波形")
            self.axes.set_ylabel(u"幅度")
            self.axes.grid(True)
        if self.shapefreq:
            self.axes = self.leftUpFigure.add_subplot(self.m,self.n,self.shapefreq)
            self.axes.plot(self.f1, self.ImpulSpectrum)
            self.axes.set_title(u"脉冲频谱")
            self.axes.set_xlabel(u"频率/f")
            self.axes.set_ylabel(u"幅度")
            self.axes.grid(True)
        if self.modutime:
            self.axes = self.leftUpFigure.add_subplot(self.m,self.n,self.modutime)
            self.x1 = numpy.linspace(-10.0/self.rate, (1.0*self.number/self.div/self.rate)+(10.0/self.rate), len(self.modulateReal))
            self.axes.plot(self.x1,self.Idata,'r',label=u"实部")
            self.axes.plot(self.x1, self.Qdata,'b',label=u"虚部")
            self.axes.legend()
            self.axes.set_title(u"调制信号时域波形")
            self.axes.set_xlabel(u"时间/s")
            self.axes.set_ylabel(u"幅度")
            self.axes.grid(True)    
        if self.modufreq:
            self.axes = self.leftUpFigure.add_subplot(self.m,self.n,self.modufreq)
            self.axes.plot(self.f2,self.Spectrum,'b')
            self.axes.set_title(u"调制信号频谱")
            self.axes.set_xlabel(u"频率/f")
            self.axes.set_ylabel(u"幅度")           
            self.axes.grid(True) 
        if self.star:
            self.axes = self.leftUpFigure.add_subplot(self.m,self.n,self.star)
            self.axes.scatter(self.a,self.b)
            self.axes.plot([-2.0,2],[0,0],'b:',[0,0],[-2.0,2],'b:')
            self.axes.grid(True)
            self.axes.set_title(u"调制信号星座图")           
        self.leftUpCanvas.draw()
    def ButtonBox(self):
        self.buttonBox = wx.BoxSizer(wx.VERTICAL)
        self.static = wx.StaticBox(self, -1, u" ")
        self.buttonBox = wx.StaticBoxSizer(self.static, wx.VERTICAL)
        self.starbutton = wx.Button(self, -1, u"开始")
        self.starbutton.SetToolTipString(u"开始运行")
        self.starbutton.Bind(wx.EVT_BUTTON, self.OnStart)
        self.buttonBox.Add(self.starbutton, 0, wx.ALL|wx.EXPAND, 2)
    def OnStart(self, event):
        if self.count > 4:
            print >> sys.stderr, u"最多选择四副图形，请重新选择..."
        else:
            self.number = int(self.NumberTextCtrl.GetValue())            
            self.codetype = self.codeChoiceBox.GetSelection()
            self.rate = int(self.RateTextCtrl.GetValue())
            self.Fs = int(self.SampleTextCtrl.GetValue()) 
            self.ratio = int(self.ratioBox.slider.GetValue())/1
            self.alph = float(self.alphBox.slider.GetValue()) / 10 
            self.sigma = float(self.sigmaBox.slider.GetValue())/10
            self.fc = int(self.CarrierTextCtrl.GetValue())
            self.x = numpy.arange(-10.0/self.rate,10.0/self.rate,1.0/self.Fs/self.rate)
            self.impulsetype = self.impulseChoiceBox.GetSelection()
            self.partialtype = self.typeChoice.GetSelection()
            self.modulatetype = self.modulateChoiceBox.GetSelection()       
            self.label,self.impulse = Impulse_time(self.impulsetype, self.alph, self.x, self.Fs, self.rate, self.partialtype, self.sigma,self.codetype, self.ratio)
            self.f1,self.ImpulSpectrum = spectrum(self.impulse, self.Fs, self.rate)
            self.real,self.image, self.div = ModulateType(self.modulatetype, self.number, self.Fs)
            self.modulateReal = DoConvolution(self.impulse, self.real)            
            self.modulateImage = DoConvolution(self.impulse, self.image)
            self.signal, self.Idata, self.Qdata = modulate(self.modulateReal, self.modulateImage, self.number, self.Fs, self.rate, self.fc)
            self.f2,self.Spectrum = spectrum(self.signal, self.Fs, self.rate)
            self.a = self.modulateReal[15.0*self.Fs:(self.number*self.Fs/self.div)+5.0*self.Fs:self.Fs]
            self.b = self.modulateImage[15.0*self.Fs:(self.number*self.Fs/self.div)+5.0*self.Fs:self.Fs]           
            self.PlotConfig(self)
              
class NewFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "frame", size = (800, 600))
        self.newPanel = ChannelSource(self)
if __name__ == '__main__':
    app = wx.PySimpleApp()
    NewFrame(None).Show(True)
    app.MainLoop()

