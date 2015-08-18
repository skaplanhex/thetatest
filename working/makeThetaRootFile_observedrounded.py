from ROOT import *
import numpy as np

f = TFile("ADDHistos_sherpahighstats.root","read")
outfile = TFile("thetainput_observedrounded_highstats.root","recreate")


h2500 = f.Get("signal_LambdaT2500_sherpa")
h3000 = f.Get("signal_LambdaT3000_sherpa")
h3500 = f.Get("signal_LambdaT3500_sherpa")
h4000 = f.Get("signal_LambdaT4000_sherpa")
h4500 = f.Get("signal_LambdaT4500_sherpa")
h5000 = f.Get("signal_LambdaT5000_sherpa")
h5500 = f.Get("signal_LambdaT5500_sherpa")
h6000 = f.Get("signal_LambdaT6000_sherpa")
h6500 = f.Get("signal_LambdaT6500_sherpa")
h7000 = f.Get("signal_LambdaT7000_sherpa")
hbkg = f.Get("sigplusbkg_LambdaT100000_sherpa")
hvar2500 = f.Get("signal_LambdaT2500_sherpa_varbin")
hvar3000 = f.Get("signal_LambdaT3000_sherpa_varbin")
hvar3500 = f.Get("signal_LambdaT3500_sherpa_varbin")
hvar4000 = f.Get("signal_LambdaT4000_sherpa_varbin")
hvar4500 = f.Get("signal_LambdaT4500_sherpa_varbin")
hvar5000 = f.Get("signal_LambdaT5000_sherpa_varbin")
hvar5500 = f.Get("signal_LambdaT5500_sherpa_varbin")
hvar6000 = f.Get("signal_LambdaT6000_sherpa_varbin")
hvar6500 = f.Get("signal_LambdaT6500_sherpa_varbin")
hvar7000 = f.Get("signal_LambdaT7000_sherpa_varbin")
hbkgvar = f.Get("sigplusbkg_LambdaT100000_sherpa_varbin")

sigDict = {
    2500 : h2500,
    3000 : h3000,
    3500 : h3500,
    4000 : h4000,
    4500 : h4500,
    5000 : h5000,
    5500 : h5500,
    6000 : h6000,
    6500 : h6500,
    7000 : h7000
}
sigDictVar = {
    2500 : hvar2500,
    3000 : hvar3000,
    3500 : hvar3500,
    4000 : hvar4000,
    4500 : hvar4500,
    5000 : hvar5000,
    5500 : hvar5500,
    6000 : hvar6000,
    6500 : hvar6500,
    7000 : hvar7000
}

# write single bin signal histograms
for ms64 in np.arange(2500,7500,500):
    ms = int(ms64)
    print "Now creating single bin histogram for ms = %i"%ms
    htemp = TH1D("singlebin__ADDMs%i"%ms,"",1,2000.,13000.)
    htemp.SetBinContent( 1,sigDict[ms].Integral(41,200) )
    outfile.cd()
    htemp.Write()

htempbkg_singlebin = TH1D("singlebin__SMDiphoton","",1,2000.,13000.)
htempdata = TH1D("singlebin__DATA","",1,2000.,13000.)
htempbkg_singlebin.SetBinContent( 1,hbkg.Integral(41,200) )
htempdata.SetBinContent( 1,round(hbkg.Integral(41,200)) )
outfile.cd()
htempbkg_singlebin.Write()
htempdata.Write()

# write multibin histograms
bins2500 = np.array([650.,1150.,1800.,13000.])
bins30003500 = np.array([650.,1150.,1800.,2600.,13000.])
bins = np.array([650.,1150.,1800.,2600.,3500.,13000.])

for ms64 in np.arange(2500,7500,500):
    ms = int(ms64)
    if ms == 2500:
        for bin in (1,2,3):
            print "Now creating Ms=%i bin=%i"%(ms,bin)
            htemp = TH1D("Ms2500mgg%i__ADDMs%i"%(bin,ms),"",1,bins2500[bin-1],bins2500[bin])
            hdata = TH1D("Ms2500mgg%i__DATA"%(bin),"",1,bins2500[bin-1],bins2500[bin])
            htempbkg = TH1D("Ms2500mgg%i__SMDiphoton"%(bin),"",1,bins2500[bin-1],bins2500[bin])
            if bin < 3:
                htemp.SetBinContent( 1, sigDictVar[ms].GetBinContent(bin+1) )
                htempbkg.SetBinContent( 1, hbkgvar.GetBinContent(bin+1) )
                hdata.SetBinContent(1 , round(hbkgvar.GetBinContent(bin+1)) )
            else:
                htemp.SetBinContent( 1, sigDictVar[ms].Integral(4,6) )
                htempbkg.SetBinContent( 1, hbkgvar.Integral(4,6) )
                hdata.SetBinContent( 1, round(hbkgvar.Integral(4,6)) )
            outfile.cd()
            htemp.Write()
            htempbkg.Write()
            hdata.Write()

    elif ms == 3000 or ms == 3500:
        for bin in (1,2,3,4):
            print "Now creating Ms=%i bin=%i"%(ms,bin)
            htemp = TH1D("Ms30003500mgg%i__ADDMs%i"%(bin,ms),"",1,bins30003500[bin-1],bins30003500[bin])
            htempbkg = TH1D("Ms30003500mgg%i__SMDiphoton"%(bin),"",1,bins30003500[bin-1],bins30003500[bin])
            hdata = TH1D("Ms30003500mgg%i__DATA"%(bin),"",1,bins30003500[bin-1],bins30003500[bin])
            if bin < 4:
                htemp.SetBinContent( 1, sigDictVar[ms].GetBinContent(bin+1) )
                htempbkg.SetBinContent( 1, hbkgvar.GetBinContent(bin+1) )
                hdata.SetBinContent( 1, round(hbkgvar.GetBinContent(bin+1)))
            else:
                htemp.SetBinContent( 1, sigDictVar[ms].Integral(5,6) )
                htempbkg.SetBinContent( 1, hbkgvar.Integral(5,6) )
                hdata.SetBinContent( 1, round(hbkgvar.Integral(5,6)) )
            outfile.cd()
            htemp.Write()
            if ms == 3000:
                hdata.Write()
                htempbkg.Write()
    else:
        for bin in (1,2,3,4,5):
            print "Now creating Ms=%i bin=%i"%(ms,bin)
            htemp = TH1D("mgg%i__ADDMs%i"%(bin,ms),"",1,bins[bin-1],bins[bin])
            # temporary hack for ms = 6000 and 7000
            # if not (bin == 1 and (ms == 6000 or ms == 7000)):
            htemp.SetBinContent( 1, sigDictVar[ms].GetBinContent(bin+1) )
            outfile.cd()
            htemp.Write()

# write multibin background and data histograms
for bin in (1,2,3,4,5):
    print "Now creating background and data histograms for bin=%i"%bin
    htemp = TH1D("mgg%i__SMDiphoton"%(bin),"",1,bins[bin-1],bins[bin])
    hdata = TH1D("mgg%i__DATA"%(bin),"",1,bins[bin-1],bins[bin])
    htemp.SetBinContent( 1, hbkgvar.GetBinContent(bin+1) )
    hdata.SetBinContent( 1, round(hbkgvar.GetBinContent(bin+1)) )
    outfile.cd()
    htemp.Write()
    hdata.Write()

outfile.Close()
f.Close()
