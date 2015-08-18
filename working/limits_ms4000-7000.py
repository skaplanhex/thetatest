

#############################################
# Build a model through a CombinedLimit datacard
#############################################

# model = higgs_datacard.build_model("/uscms_data/d3/skaplan/diphotons/theta/CMSSW_7_2_4/src/theta/working/testcard.txt")
# model_summary(model)
# expected,observed = theta_auto.bayesian_limits(model)
# expected.write_txt("expected.txt")
# observed.write_txt("observed.txt")

########################################
# Build a model directly from a root file
########################################

def histogramFilter(histName):
    if histName[:3] == "mgg":
        return True
    else:
        return False
def changeName(histName):
    return histName
def transformHist(hist):
    return hist

model = theta_auto.build_model_from_rootfile("thetainput_highstats.root",histogramFilter,changeName,transformHist,False)
model.set_signal_processes( ("ADDMs4*","ADDMs5*","ADDMs6*","ADDMs7*") )
model_summary(model)
expected,observed = theta_auto.bayesian_limits(model)
expected.write_txt("expected4000-7000.txt")
observed.write_txt("observed4000-7000.txt")