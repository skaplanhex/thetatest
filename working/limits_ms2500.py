

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
    if "Ms2500mgg" in histName:
        return True
    else:
        return False
def changeName(histName):
    return histName
def transformHist(hist):
    return hist

model = theta_auto.build_model_from_rootfile("thetainput_highstats.root",histogramFilter,changeName,transformHist,False)
# model = theta_auto.build_model_from_rootfile("test.root")
model.set_signal_processes('ADDMs2500')
model_summary(model)
expected,observed = theta_auto.bayesian_limits(model)
expected.write_txt("expected2500.txt")
observed.write_txt("observed2500.txt")