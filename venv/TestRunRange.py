import pandas as pd
import time

#file = open(r'''/Users/hari/Desktop/CompTestResults.txt''', 'r')
file = open(r'''/Users/hari/Desktop/UAT Week 1.txt''', 'r')

x = [i.strip().split('\t') for i in file.readlines()]
#y = list(filter(None, x))
y=x


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
    return j



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
            #if y[j][k] == "Precondition" and kind != "" and len(y[j]): precon = y[j][k + 1]
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
    for Scripts in range(a+1, len(y)):
        ActRes = ""
        attch = ""
        if breakloop == True: break
        for ScriptDets in range(0, len(y[Scripts])):
            if y[Scripts][0:11] == "Created by":
                #print(CurrRun,Scripts)
                breakloop = True
            if y[Scripts][ScriptDets] == "Status": stat1 = y[Scripts][ScriptDets]
            if y[Scripts][ScriptDets] == "Details":
                dets = ""
                while y[Scripts + 1][ScriptDets] != "Test Data":
                    dets = y[Scripts + 1][ScriptDets] + dets
                    Scripts += 1
            if y[Scripts][ScriptDets] == "Test Data": TData = y[Scripts][ScriptDets]
            if y[Scripts][ScriptDets] == "Expected Result":
                while y[Scripts][ScriptDets] != "Actual Result":
                    ExpRes = y[Scripts][ScriptDets]
                    Scripts+=1
            if y[Scripts][ScriptDets] == "Actual Result":
                while y[Scripts][ScriptDets] != "Attachments":
                    ActRes = y[Scripts][ScriptDets]
                    Scripts+=1
            if y[Scripts][ScriptDets] == "Attachments":
                while y[Scripts][ScriptDets] != "Issues":
                    attch = y[Scripts][ScriptDets]
                    Scripts+=1
            if y[Scripts][ScriptDets] == "Issues":
                issues = y[Scripts][ScriptDets]
                Scriptdetails.append([count,stat1, dets, ExpRes, ActRes, attch, issues])
                count+=1
            elif y[Scripts][ScriptDets][0:8] == "SFHTCM-T":
                count=1
                TestScripts[kind] = Scriptdetails
                TestRuns[CurrRun] = TestScripts
                breakloop = True
                TSRange(Scripts,CurrRun)

starttime= time.time()
for i in range(0, len(y)):
    for j in range(0, len(y[i])):
        if y[i][j][0:8] == "SFHTCM-P":
            TestPlan = y[i][j]
            TestPlans[TestPlan] = TPRange(i)
        if y[i][j][0:8] == "SFHTCM-R":
            CurrRun = y[i][j]
            TRRange(i,CurrRun)
            #print(i)


df = pd.DataFrame.from_dict(TestRuns, orient='index')


print(df)
diff = time.time()-starttime
print(diff)