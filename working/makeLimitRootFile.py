from ROOT import *

observed_singleBin = TGraph()
observedrounded_singleBin = TGraph()
expected_singleBin = TGraph()
expected68_singleBin = TGraphAsymmErrors()
expected95_singleBin = TGraphAsymmErrors()

observed_singleBin.SetName("observed_singleBin")
observedrounded_singleBin.SetName("observedrounded_singleBin")
expected_singleBin.SetName("expected_singleBin")
expected68_singleBin.SetName("expected68_singleBin")
expected95_singleBin.SetName("expected95_singleBin")

observed_multiBin = TGraph()
observedrounded_multiBin = TGraph()
expected_multiBin = TGraph()
expected68_multiBin = TGraphAsymmErrors()
expected95_multiBin = TGraphAsymmErrors()

observed_multiBin.SetName("observed_multiBin")
observedrounded_multiBin.SetName("observedrounded_multiBin")
expected_multiBin.SetName("expected_multiBin")
expected68_multiBin.SetName("expected68_multiBin")
expected95_multiBin.SetName("expected95_multiBin")

######################
# plot single bin
######################

fobserved_singleBin = open("results_singleBin/observed_singlebin.txt",'r')
fobservedrounded_singleBin = open("results_singleBin/observed_singlebin_observedrounded.txt",'r')
fexpected_singleBin = open("results_singleBin/expected_singlebin_observedrounded.txt",'r')

pointCount = 0
for line in fobserved_singleBin:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        observed_singleBin.SetPoint( pointCount,int(s[0]),float(s[1]) )
        pointCount += 1
fobserved_singleBin.close()

pointCount = 0
for line in fobservedrounded_singleBin:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        observedrounded_singleBin.SetPoint( pointCount,int(s[0]),float(s[1]) )
        pointCount += 1
fobservedrounded_singleBin.close()   

pointCount = 0
for line in fexpected_singleBin:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        for graph in (expected_singleBin,expected68_singleBin,expected95_singleBin):
            graph.SetPoint( pointCount,int(s[0]),float(s[1]) )

        expected68_singleBin.SetPointError( pointCount,0.,0.,float(s[1])-float(s[4]),float(s[5])-float(s[1]) )
        expected95_singleBin.SetPointError( pointCount,0.,0.,float(s[1])-float(s[2]),float(s[3])-float(s[1]) )
        pointCount += 1

#########################
# multibin plots
#########################

fobserved_2500 = open("results_multiBin/observed2500.txt",'r')
fobservedrounded_2500 = open("results_multiBin/observed2500_observedrounded.txt",'r')
fexpected_2500 = open("results_multiBin/expected2500.txt",'r')
fobserved_30003500 = open("results_multiBin/observed30003500.txt",'r')
fobservedrounded_30003500 = open("results_multiBin/observed30003500_observedrounded.txt",'r')
fexpected_30003500 = open("results_multiBin/expected30003500.txt",'r')
fobserved_40007000 = open("results_multiBin/observed4000-7000.txt",'r')
fobservedrounded_40007000 = open("results_multiBin/observed4000-7000_observedrounded.txt",'r')
fexpected_40007000 = open("results_multiBin/expected4000-7000.txt",'r')

pointCount = 0

for line in fobserved_2500:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        observed_multiBin.SetPoint( pointCount,int(s[0]),float(s[1]) )
        pointCount += 1
for line in fobserved_30003500:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        observed_multiBin.SetPoint( pointCount,int(s[0]),float(s[1]) )
        pointCount += 1
for line in fobserved_40007000:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        observed_multiBin.SetPoint( pointCount,int(s[0]),float(s[1]) )
        pointCount += 1


pointCount = 0

for line in fobservedrounded_2500:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        observedrounded_multiBin.SetPoint( pointCount,int(s[0]),float(s[1]) )
        pointCount += 1
for line in fobservedrounded_30003500:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        observedrounded_multiBin.SetPoint( pointCount,int(s[0]),float(s[1]) )
        pointCount += 1
for line in fobservedrounded_40007000:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        observedrounded_multiBin.SetPoint( pointCount,int(s[0]),float(s[1]) )
        pointCount += 1

pointCount = 0

for line in fexpected_2500:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        for graph in (expected_multiBin,expected68_multiBin,expected95_multiBin):
            graph.SetPoint( pointCount,int(s[0]),float(s[1]) )
        expected68_multiBin.SetPointError( pointCount,0.,0.,float(s[1])-float(s[4]),float(s[5])-float(s[1]) )
        expected95_multiBin.SetPointError( pointCount,0.,0.,float(s[1])-float(s[2]),float(s[3])-float(s[1]) )
        pointCount += 1
for line in fexpected_30003500:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        for graph in (expected_multiBin,expected68_multiBin,expected95_multiBin):
            graph.SetPoint( pointCount,int(s[0]),float(s[1]) )
        expected68_multiBin.SetPointError( pointCount,0.,0.,float(s[1])-float(s[4]),float(s[5])-float(s[1]) )
        expected95_multiBin.SetPointError( pointCount,0.,0.,float(s[1])-float(s[2]),float(s[3])-float(s[1]) )
        pointCount += 1
for line in fexpected_40007000:
    s = line.split()
    if s[0] == "#":
        continue
    else:
        for graph in (expected_multiBin,expected68_multiBin,expected95_multiBin):
            graph.SetPoint( pointCount,int(s[0]),float(s[1]) )
        expected68_multiBin.SetPointError( pointCount,0.,0.,float(s[1])-float(s[4]),float(s[5])-float(s[1]) )
        expected95_multiBin.SetPointError( pointCount,0.,0.,float(s[1])-float(s[2]),float(s[3])-float(s[1]) )
        pointCount += 1

########################################
# write out the plots to a root file
########################################

outfile = TFile("limitplots_highstats.root","recreate")
outfile.cd()
for graph in (observed_singleBin,observedrounded_singleBin,expected_singleBin,expected68_singleBin,expected95_singleBin,observed_multiBin,observedrounded_multiBin,expected_multiBin,expected68_multiBin,expected95_multiBin):
    graph.Write()

# raw_input("enter to quit: ")