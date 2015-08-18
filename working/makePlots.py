from ROOT import *
gROOT.SetBatch()

infile = TFile("limitplots_highstats.root","read")

observed_singleBin = infile.Get("observed_singleBin")
observedrounded_singleBin = infile.Get("observedrounded_singleBin")
expected_singleBin = infile.Get("expected_singleBin")
expected68_singleBin = infile.Get("expected68_singleBin")
expected95_singleBin = infile.Get("expected95_singleBin")

observed_multiBin = infile.Get("observed_multiBin")
observedrounded_multiBin = infile.Get("observedrounded_multiBin")
expected_multiBin = infile.Get("expected_multiBin")
expected68_multiBin = infile.Get("expected68_multiBin")
expected95_multiBin = infile.Get("expected95_multiBin")

c = TCanvas("c","",1200,800)

observed_singleBin.SetLineWidth(2)
observed_multiBin.SetLineWidth(2)

observedrounded_singleBin.SetLineWidth(2)
observedrounded_multiBin.SetLineWidth(2)
observedrounded_singleBin.SetLineStyle(4)
observedrounded_multiBin.SetLineStyle(4)
observedrounded_singleBin.SetLineColor(kRed)
observedrounded_multiBin.SetLineColor(kRed)

for g in (expected_singleBin,expected_multiBin):
    g.SetLineStyle(2)
for g in (expected68_singleBin,expected68_multiBin):
    g.SetFillColor(kGreen)
    g.SetLineColor(kGreen)
for g in (expected95_singleBin,expected95_multiBin):
    g.SetFillColor(kYellow)
    g.SetLineColor(kYellow)
    g.GetXaxis().SetTitle("M_{S} (GeV)")
    g.GetYaxis().SetTitle("95% Upper Limit On r")
for g in (expected_singleBin,expected_multiBin,expected68_singleBin,expected68_multiBin,expected95_singleBin,expected95_multiBin):
    g.SetFillStyle(1001)


# single bin plot
expected95_singleBin.Draw("A3")
expected68_singleBin.Draw("3")
expected_singleBin.Draw("L")
observed_singleBin.Draw("L")
observedrounded_singleBin.Draw("L")

leg = TLegend(.28,.59,.55,.82)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.025)
leg.AddEntry(observed_singleBin,"Observed = 0","L")
leg.AddEntry(observedrounded_singleBin,"Observed = round(bkg)","L")
leg.AddEntry(expected_singleBin,"ADD G->#gamma#gamma","L")
leg.AddEntry(expected68_singleBin,"#pm 1#sigma","F")
leg.AddEntry(expected95_singleBin,"#pm 2#sigma","F")
leg.Draw()

c.SetLogy()
c.SaveAs("limit_singleBin_highstats.pdf")
c.Clear()

expected95_multiBin.Draw("A3")
expected68_multiBin.Draw("3")
expected_multiBin.Draw("L")
observed_multiBin.Draw("L")
observedrounded_multiBin.Draw("L")

leg = TLegend(.28,.59,.55,.82)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.025)
leg.AddEntry(observed_multiBin,"Observed = 0","L")
leg.AddEntry(observedrounded_multiBin,"Observed = round(bkg)","L")
leg.AddEntry(expected_multiBin,"ADD G->#gamma#gamma","L")
leg.AddEntry(expected68_multiBin,"#pm 1#sigma","F")
leg.AddEntry(expected95_multiBin,"#pm 2#sigma","F")
leg.Draw()

c.SetLogy()
c.SaveAs("limit_multiBin_highstats.pdf")
c.Clear()

########################
# plot band sizes
########################
band68size_singleBin = TGraph()
band95size_singleBin = TGraph()
band68size_multiBin = TGraph()
band95size_multiBin = TGraph()

band68size_singleBin.SetName("band68size_singleBin")
band95size_singleBin.SetName("band95size_singleBin")
band68size_multiBin.SetName("band68size_multiBin")
band95size_multiBin.SetName("band95size_multiBin")

for i,ms in enumerate((2500.,3000.,3500.,4000.,4500.,5000.,5500.,6000.,6500.,7000.)):

    # get band sizes
    single68 = expected68_singleBin.GetErrorYhigh(i) + expected68_singleBin.GetErrorYlow(i)
    single95 = expected95_singleBin.GetErrorYhigh(i) + expected95_singleBin.GetErrorYlow(i)
    multi68 = expected68_multiBin.GetErrorYhigh(i) + expected68_multiBin.GetErrorYlow(i)
    multi95 = expected95_multiBin.GetErrorYhigh(i) + expected95_multiBin.GetErrorYlow(i)

    # fill the TGraphs
    band68size_singleBin.SetPoint(i,ms,single68)
    band95size_singleBin.SetPoint(i,ms,single95)
    band68size_multiBin.SetPoint(i,ms,multi68)
    band95size_multiBin.SetPoint(i,ms,multi95)

c.cd()

band68size_singleBin.GetXaxis().SetTitle("M_{S} (GeV)")
band68size_singleBin.GetYaxis().SetTitle("1#sigma Band Width")
band68size_singleBin.SetLineWidth(2)
band68size_multiBin.SetLineWidth(2)
band68size_multiBin.SetLineStyle(2)
band68size_multiBin.SetLineColor(kBlue)

band95size_singleBin.GetXaxis().SetTitle("M_{S} (GeV)")
band95size_singleBin.GetYaxis().SetTitle("2#sigma Band Width")
band95size_singleBin.SetLineWidth(2)
band95size_multiBin.SetLineWidth(2)
band95size_multiBin.SetLineStyle(2)
band95size_multiBin.SetLineColor(kBlue)

band68size_singleBin.Draw("AL")
band68size_multiBin.Draw("L")
leg = TLegend(.28,.59,.55,.82)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.025)
leg.AddEntry(band68size_singleBin,"Single Bin","L")
leg.AddEntry(band68size_multiBin,"Multi Bin","L")
leg.Draw()
c.SaveAs("bandsize_1sigma.pdf")
c.Clear()

band95size_singleBin.Draw("AL")
band95size_multiBin.Draw("L")
leg = TLegend(.28,.59,.55,.82)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.025)
leg.AddEntry(band95size_singleBin,"Single Bin","L")
leg.AddEntry(band95size_multiBin,"Multi Bin","L")
leg.Draw()
c.SaveAs("bandsize_2sigma.pdf")
c.Clear()

infile.Close()