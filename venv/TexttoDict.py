import pandas as pd
import time

file = open(r'''/Users/hari/Desktop/CompTestResults.txt''', 'r')
#file = open(r'''/Users/hari/Desktop/UAT Week 1.txt''', 'r')

x = [i.strip().split('\t') for i in file.readlines()]
flat_list = []
for sublist in x:
    for item in sublist:
        flat_list.append(item)

y = list(filter(None, flat_list))
#y = list(filter(None, x))



TestPlanRange = {}
TestPlans = {}
TestRunRange = {}
TestRuns = {}
TestScriptRange = {}
TestScripts = {}
TestScriptList = {}
Scriptdetails = []



dict = {}

def TPRange(a,plan):
    breakloop = False
    for j in range(a,len(y)):
        if breakloop == True: break
        #for k in range(0,len(y[j])):
            #print(y[j][k])
        if y[j] == "Name": Name = y[j+1]
        if y[j] == "Objective": Obj = y[j+1]
        if y[j] == "Status":
            stat = y[j+1]
            breakloop = True
    b = [plan, Name, Obj, stat]
    return b

def TRRange(a,CurrRun):
    breakloop = False
    for j in range(a,len(y)):
        if breakloop == True: break
        if y[j] == "Name": Name = y[j+1]
        if y[j] == "Description": Desc = y[j+1]
        if y[j] == "Planned start date": Pstart = y[j+1]
        if y[j] == "Planned end date": Pend = y[j+1]
        if y[j] == "Iteration": iter1 = y[j+1]
        if y[j] == "Status": stat = y[j+1]
        if y[j] == "Version":
            ver = y[j+1]
            TestRunRange[CurrRun] = [Name, Desc, Pstart, Pend, iter1, stat, ver]
            TSRange(j,CurrRun)
            breakloop = True




def TSRange(a,CurrRun):
    breakloop = False
    kind = ""
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
        if y[j][0:11] == "Created by": breakloop = True
        if y[j][0:8] == "SFHTCM-T": kind = y[j]
        if y[j] == "Status" and kind != "": Status = y[j+1]
        if y[j] == "Name" and kind != "": Name1 = y[j+1]
        if y[j] == "Objective" and kind != "": Obj1 = y[j+1]
        if y[j] == "Precondition" and kind != "": precon = y[j+1]
        if y[j] == "Coverage" and kind != "": cov = y[j+1]
        if y[j] == "Execution date" and kind != "": exdate = y[j+1]
        if y[j] == "Estimated Time" and kind != "": estime = y[j+1]
        if y[j] == "Actual Time" and kind != "": actime1 = y[j+1]
        if y[j] == "Assignee" and kind != "": assignee = y[j+1]
        if y[j] == "Environment" and kind != "": env = y[j+1]
        if y[j] == "Type" and kind != "": type1 = y[j+1]
        if y[j] == "Issues" and kind != "": issues = y[j+1]
        if y[j] == "Attachments" and kind != "": attach = y[j+1]
        if y[j] == "Test Script" and kind != "":
            TestScriptList[kind] = [Status, Name1, Obj1, precon, exdate, estime, assignee, env, type1, issues,attach,cov,actime1]
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
        elif y[Scripts][0:11] == "Created by":
            breakloop = True
        elif y[Scripts] == "Status": stat1 = y[Scripts+1]
        elif y[Scripts] == "Test Data": TData = y[Scripts+1]
        elif y[Scripts] == "Expected Result":
            while y[Scripts+1]!= "Actual Result":
                Scripts += 1
                ExpRes = y[Scripts]
        elif y[Scripts] == "Actual Result":
            while y[Scripts] != "Attachments":
                Scripts+=1
                ActRes = y[Scripts] + ActRes
        elif y[Scripts] == "Attachments":
            while y[Scripts] != "Issues":
                Scripts += 1
                attch = y[Scripts+1]
        elif y[Scripts] == "Details":
            dets = ""
            while y[Scripts+1]!= "Test Data":
                Scripts += 1
                dets = dets + y[Scripts]
        elif y[Scripts] == "Issues":
            issues = y[Scripts+1]
            Scriptdetails.append([count,stat1, dets, ExpRes, ActRes, attch, issues,TData])
            #print(Scriptdetails[count-1])
            Scripts+=1
        elif Scripts < len(y)-3 and y[Scripts+1] == str(count+1):
            count+=1
            ActRes = ""
            attch = ""
            stat1 = "NOT EXECUTED"
            TData = ""
            dets = ""
            ExpRes = ""
        if y[Scripts][0:8] == "SFHTCM-T":
            count=1
            TestScripts[kind] = Scriptdetails
            TestRuns[CurrRun] = TestScripts
            breakloop = True
            TSRange(Scripts,CurrRun)



starttime= time.time()
for i in range(0, len(y)):
    if y[i][0:8] == "SFHTCM-P":
        TestPlan = y[i]
        TestPlans[TestPlan] = TPRange(i,TestPlan)
    if y[i][0:8] == "SFHTCM-R":
        CurrRun = y[i]
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
               #ScriptSummary["NOT EXECUTED"] = necount
           if TestRuns[k][i][l][1] == "PASS":
               passcount += 1
               #ScriptSummary["PASS"] = passcount
           if TestRuns[k][i][l][1] == "FAIL":
               failcount += 1
               #ScriptSummary["FAIL"] = failcount
        TestSummary[i] = [necount,passcount,failcount]
#df = pd.DataFrame.from_dict(TestRuns["SFHTCM-R553"], orient='index')
df = pd.DataFrame.from_dict(TestSummary, orient='index')
#df.to_html('Table.html')
#print(df)
df.plot.bar(rot=0)
#print(TestRuns["SFHTCM-R556"]["SFHTCM-T771"])
#print(TestSummary)
diff = time.time()-starttime
print(diff)
