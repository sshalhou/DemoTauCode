import time
import sys
import os
import math
from array import array
from ROOT import *
import ROOT

from python.Settings import VETO_NAME_CONTENT as VETO
from python.Settings import DEMAND_NAME_CONTENT as ONLY


def FormatHist(HIST,MARKERSTYLE,COLOR):
	HIST.SetTitleOffset(0.9,"X")
	HIST.SetTitleOffset(0.75,"Y")
	HIST.SetTitleSize(0.08,"XYZ")
	HIST.SetLabelSize(0.065,"XYZ")
	HIST.GetXaxis().CenterTitle(1)
	HIST.GetYaxis().CenterTitle(1)
	HIST.SetMarkerStyle(MARKERSTYLE)
	HIST.SetLineColor(COLOR)
	HIST.SetMarkerColor(COLOR)
	return

def ScanFile(FILE, OBJECT_DICT, OBJ_NAME_LIST):
	for key in FILE.GetListOfKeys():
		FILE.cd(key.GetName())
		for hist in gDirectory.GetListOfKeys():
			histname = key.GetName()+"/"+hist.GetName()
			CHECK = 1
			DEMAND = 0
			MET_DEMAND = False
			for z in range(0,len(VETO)):
				if VETO[z] in histname:
					CHECK = 0
					break
			if len(ONLY) == 0 : MET_DEMAND = True
			else :
				for z in range(0, len(ONLY)):
					if ONLY[z] in histname:
						DEMAND += 1
						
			if DEMAND == len(ONLY): MET_DEMAND = True

			if 'TH1F' in str(type(FILE.Get(histname))) and CHECK and MET_DEMAND:
				OBJECT_DICT[histname] = FILE.Get(histname).Clone()
				OBJ_NAME_LIST.append(histname)
	return

def GetCommonList(LIST1, LIST2):
	return list(set(LIST1).intersection(LIST2))

def GetDiffList(LIST1, LIST2):	
	return list(set(LIST1).symmetric_difference(LIST2))

def CompareNormalizations(LIST,DICT1,DICT2,THRESHOLD,LESS_or_GREATER):

	FLAGGED = []
	for i in range(0,len(LIST)):
		A = DICT1[LIST[i]].GetSumOfWeights()
		B = DICT2[LIST[i]].GetSumOfWeights()
		X = PercentDiff(A,B)
		if LESS_or_GREATER == 'GREATER':
			if X > THRESHOLD and A>0 and B>0:
				FLAGGED.append(LIST[i])
		elif LESS_or_GREATER == 'LESS':		
			if X < THRESHOLD and A>0 and B>0:
				FLAGGED.append(LIST[i])
		else: # greater by default
			if X > THRESHOLD and A>0 and B>0:
				FLAGGED.append(LIST[i])	


	return FLAGGED

def PercentDiff(a,b):
	if a+b > 0:
		return 100*abs(a-b)/(0.5*(a+b))
	else :		
		return 0.0

def f(A):
	return "{:.1f}".format(A)

def ff(A):
	return "{:.2f}".format(A)

def fff(A):
	return "{:.3f}".format(A)	


def PLOT_HIST_DIFF(instA,H1,instB,H2,LOW,HIGH):
	gROOT.SetBatch(True)
	gStyle.SetOptStat(000000)
	C = TCanvas("C"+H1.GetTitle(),"C"+H1.GetTitle(),1000,600)
	C.Divide(1,2)
	C.cd(1)

	max_bin = H1.GetXaxis().FindBin(HIGH)
	low_bin = H1.GetXaxis().FindBin(LOW)
	H1.GetXaxis().SetRange(low_bin,max_bin)

	FormatHist(H1,8,2)
	#H1.SetTitle(";M_{#tau#tau}[GeV]"+";"+instA+"/"+instB)

	H1.DrawCopy("PE").SetTitle(H1.GetTitle()+";M_{#tau#tau}[GeV]"+";"+instA+"/"+instB)
	H1.Draw("histsames")
	FormatHist(H2,22,1)
	H2.Draw("PEsames")
	H2.Draw("histsames")


	C.cd(2)
	DIFF = H1.Clone()
	DIFF.Divide(H1,H2,1.,1.,"B")
	DIFF.SetTitle(";M_{#tau#tau}[GeV]"+";"+instA+"/"+instB)
	FormatHist(DIFF,8,1)
	DIFF.Draw("PE")
	DIFF.GetXaxis().SetRange(low_bin,max_bin)
	L = TLine()
	L.SetLineColor(2)
	END = DIFF.GetBinCenter(max_bin) + 0.5*DIFF.GetBinWidth(max_bin)
	L.DrawLine(LOW,1.0,END,1.0)
	DIFF.Draw("PEsames")

	C.cd().SaveAs(("./PLOTS/DIFF_"+(H1.GetTitle().replace('/','-'))+".png"))
	return 



def PLOT_SYSTEMATCIS(instA,instB,NOMINAL_NAME,SYS_NAME,DICT1,DICT2,LOW,HIGH):
	gROOT.SetBatch(True)
	gStyle.SetOptStat(000000)
	C = TCanvas("C"+SYS_NAME,"C"+SYS_NAME,1000,600)
	C.cd()

	HA = DICT1[SYS_NAME].Clone()
	HA.Divide(DICT1[SYS_NAME],DICT1[NOMINAL_NAME],1,1,"B")


	HB = DICT2[SYS_NAME].Clone()
	HB.Divide(DICT2[SYS_NAME],DICT2[NOMINAL_NAME],1,1,"B")

	FormatHist(HA,8,2)
	FormatHist(HB,8,1)
	#HB.SetMarkerSize(2)
	max_bin = HA.GetXaxis().FindBin(HIGH)
	low_bin = HA.GetXaxis().FindBin(LOW)
	HA.GetXaxis().SetRange(low_bin,max_bin)


	#HA.SetTitle(SYS_NAME+";M_{#tau#tau}[GeV]"+"; [(sys)"+instA+"]/[(nom)"+instB+"]")

	HA.DrawCopy("PE").SetTitle(SYS_NAME+";M_{#tau#tau}[GeV]"+"; [ varied ]/[ nominal ]")
	HB.Draw("PEsames")

	L = TLine()
	L.SetLineColor(3)
	END = HA.GetBinCenter(max_bin) + 0.5*HA.GetBinWidth(max_bin)
	L.DrawLine(LOW,1.0,END,1.0)
	HA.Draw("PEsames")

	leg1 =  TLegend(0.75,0.75,0.85,.85)
	leg1.SetTextSize(0.05)
	leg1.SetTextFont(42)
	leg1.SetBorderSize(0)
	leg1.SetFillColor(kWhite)
	leg1.AddEntry(HA,instA)
	leg1.AddEntry(HB,instB)
	leg1.Draw()

	C.cd().SaveAs(("./PLOTS/SYS_"+(SYS_NAME.replace('/','-'))+".png"))

	return


