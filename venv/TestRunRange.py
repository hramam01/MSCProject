import pandas as pd
import time

#file = open(r'''/Users/hari/Desktop/CompTestResults.txt''', 'r')
file = open(r'''/Users/hari/Desktop/UAT Week 1.txt''', 'r')

x = [i.strip().split('\t') for i in file.readlines()]
flat_list = []
for sublist in x:
    for item in sublist:
        flat_list.append(item)

#y = list(filter(None, flat_list))
y = list(filter(None, x))



TestPlanRange = {}
TestPlans = {}
TestRunRange = {}
TestRuns = {}
TestScriptRange = {}
TestScripts = {}
TestScriptList = {}
Scriptdetails = []



dict = {}

def TPRange(a):
    breakloop = False
    for j in range(a,len(y)):
        if breakloop == True: break
        for k in range(0,len(y[j])):
            #print(y[j][k])
            if y[j][k] == "Key": Key = y[j][k+1]
            if y[j][k] == "Name": Name = y[j][k+1]
            #if y[j][k] == "Objective": Obj = y[j][k]
            if y[j][k] == "Status":
                stat = y[j][k+1]
                breakloop = True

    b = [Key, Name, "None", stat]
    return b

def TRRange(a,CurrRun):
    #for k,v in TestRunRange.items():
    #    kind = k
    breakloop = False
    for j in range(a,len(y)):
        if breakloop == True: break
        for k in range(0,len(y[j])):
            if y[j][k] == "Name": Name = y[j+1][k]
            if y[j][k] == "Description": Desc = y[j+1][k]
            if y[j][k] == "Planned start date": Pstart = y[j+1][k]
            if y[j][k] == "Planned end date": Pend = y[j+1][k]
            if y[j][k] == "Iteration": iter1 = y[j+1][k]
            if y[j][k] == "Status": stat = y[j+1][k]
            if y[j][k] == "Version":
                ver = y[j+1][k]
                TestRunRange[CurrRun] = [Name, Desc, Pstart, Pend, iter1, stat, ver]
                TSRange(j,CurrRun)
                breakloop = True
    #return j



def TSRange(a,CurrRun):
    breakloop = False
    kind = ""
    #TestScriptList = {}
    Status=""
    Name1 = ""
    precon=""
    cov=""
    exdate=""
    estime=""
    actime1 =""
    assignee=""
    env=""
    type1 = ""
    issues=""
    attach=""
    for j in range(a, len(y)):
        if breakloop == True: break
        for k in range(0,len(y[j])):
            if y[j][k][0:11] == "Created by": breakloop = True
            if y[j][k][0:8] == "SFHTCM-T": kind = y[j][k]
            if y[j][k] == "Status" and kind != "": Status = y[j][k + 1]
            if y[j][k] == "Name" and kind != "": Name1 = y[j][k + 1]
            if y[j][k] == "Objective" and kind != "": Obj1 = y[j][k]
            if y[j][k] == "Precondition" and kind != "" and len(y[j])>1: precon = y[j][1]
            if y[j][k] == "Coverage" and kind != "": cov = y[j][k + 1]
            if y[j][k] == "Execution date" and kind != "": exdate = y[j][k + 1]
            if y[j][k] == "Estimated Time" and kind != "": estime = y[j][k + 1]
            if y[j][k] == "Actual Time" and kind != "": actime1 = y[j][k + 1]
            if y[j][k] == "Assignee" and kind != "": assignee = y[j][k + 1]
            if y[j][k] == "Environment" and kind != "": env = y[j][k + 1]
            if y[j][k] == "Type" and kind != "": type1 = y[j][k + 1]
            if y[j][k] == "Issues" and kind != "": issues = y[j][k + 1]
            if y[j][k] == "Attachments" and kind != "": attach = y[j][k + 1]
            if y[j][k] == "Test Script" and kind != "":
                TestScriptList[kind] = [Status, Name1, Obj1, precon, exdate, estime, assignee, env, type1, issues,attach]
                breakloop = True
                TScripts(j,kind,CurrRun)
    #return j

def TScripts(a,kind,CurrRun):
    Scriptdetails = []
    count = 1
    breakloop = False
    ActRes = ""
    attch = ""
    stat1 = "NOT EXECUTED"
    TData = ""
    dets = ""
    ExpRes = ""
    for Scripts in range(a+1, len(y)):
        if breakloop == True: break
        for ScriptDets in range(0, len(y[Scripts])):
            if y[Scripts][0:11] == "Created by":
                #print(CurrRun,Scripts)
                breakloop = True
            if y[Scripts][ScriptDets] == "Status" and ScriptDets == 1:
                #if y[Scripts][ScriptDets+1] != "NOT EXECUTED": print(CurrRun,kind,count)
                stat1 = y[Scripts][ScriptDets+1]
            if y[Scripts][ScriptDets] == "Test Data": TData = y[Scripts+1][ScriptDets]
            if y[Scripts][ScriptDets] == "Expected Result":
                while y[Scripts+1][ScriptDets] != "Actual Result":
                    ExpRes = y[Scripts+1][ScriptDets]
                    Scripts+=1
            if y[Scripts][ScriptDets] == "Actual Result":
                while y[Scripts][ScriptDets] != "Attachments":
                    ActRes = y[Scripts+1][ScriptDets] + ActRes
                    Scripts+=1
            if y[Scripts][ScriptDets] == "Attachments":
                while y[Scripts][ScriptDets] != "Issues":
                    attch = y[Scripts][ScriptDets+1]
                    Scripts+=1
            if y[Scripts][ScriptDets] == "Issues":
                issues = y[Scripts][ScriptDets+1]
                Scriptdetails.append([count,stat1, dets, ExpRes, ActRes, attch, issues,TData])
                count+=1
                ActRes = ""
                attch = ""
                stat1 = "NOT EXECUTED"
                TData = ""
                dets = ""
                ExpRes = ""
            if y[Scripts][ScriptDets][0:8] == "SFHTCM-T":
                count=1
                TestScripts[kind] = Scriptdetails
                TestRuns[CurrRun] = TestScripts
                breakloop = True
                TSRange(Scripts,CurrRun)
            if y[Scripts][ScriptDets] == "Details":
                dets = ""
                while y[Scripts][ScriptDets] != "Test Data":
                    dets = y[Scripts + 1][ScriptDets] + dets
                    Scripts += 1

starttime= time.time()
for i in range(0, len(y)):
    for j in range(0, len(y[i])):
        if y[i][j][0:8] == "SFHTCM-P":
            TestPlan = y[i][j]
            TestPlans[TestPlan] = TPRange(i)
        if y[i][j][0:8] == "SFHTCM-R":
            CurrRun = y[i][j]
            TRRange(i,CurrRun)

TestSummary = {}
ScriptSummary = {}


for k,v in TestRuns.items():
    for i,j in TestRuns[k].items():
        necount = 0
        passcount = 0
        failcount = 0
        for l in range(0,len(TestRuns[k][i])):
               if TestRuns[k][i][l][1] == "NOT EXECUTED":
                   necount += 1
                   ScriptSummary["NOT EXECUTED"] = necount
               if TestRuns[k][i][l][1] == "PASS":
                   passcount += 1
                   ScriptSummary["PASS"] = passcount
               if TestRuns[k][i][l][1] == "FAIL":
                   failcount += 1
                   ScriptSummary["FAIL"] = failcount
        TestSummary[i] = ScriptSummary
#df = pd.DataFrame.from_dict(TestRuns["SFHTCM-R553"], orient='index')
df = pd.DataFrame.from_dict(TestSummary, orient='index')
#df.to_html('Table.html')
print(df)
#print(TestRuns["SFHTCM-R556"]["SFHTCM-T771"])
print(TestScripts)
diff = time.time()-starttime
print(diff)
