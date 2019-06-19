import pandas as pd

file = open(r'''/Users/hari/Desktop/CompTestResults.txt''', 'r')

x = [i.strip().split('\t') for i in file.readlines()]
y = list(filter(None, x))
TestPlanRange = {}
TestPlans = {}
TestRunRange = {}
TestRuns = {}
TestScriptRange = {}
TestScripts = {}

print(y[30][0])

for i in range(0, len(y)):
    for j in range(0, len(y[i])):
        if y[i][j][0:8] == "SFHTCM-P":
            TPstarti = i
            TPstartj = j
            TestPlan = y[i][j]
        if y[i][j][0:8] == "SFHTCM-R":
            TPendi = i
            TPendj = j
            TestPlanRange[TestPlan] = [TPstarti,TPstartj,TPendi,TPendj]
            TestRun = y[i][j]
            TRstarti = i
            TRstartj= j
        if y[i][j][0:8] == "SFHTCM-T":
            TRendi = i
            TRendj = j
            TestRunRange[TestRun] = [TRstarti, TRstartj, TRendi, TRendj]
            TSstarti = i
            TSstartj = j
            TestScript = y[i][j]
            #count = 1
        if y[i][j] == "Test Script":
            TSendi = i
            TSendj = j
            TestScriptRange[TestScript] = [TSstarti,TSstartj,TSendi,TSendj]

#print(TestPlanRange)
#print(TestRunRange)
#print(TestScriptRange)

#df = pd.DataFrame.from_dict(TestRunRange, orient='index')
dict = {}

for k,v in TestRunRange.items():
    kind = k
    breakloop = False
    for j in range(v[0],v[2]):
        if breakloop == True: break
        for k in range(0,len(y[j])):
            #print(y[j][k])
            if y[j][k] == "Name": Name = y[j+1][k]
            if y[j][k] == "Description": Desc = y[j+1][k]
            if y[j][k] == "Planned start date": Pstart = y[j+1][k]
            if y[j][k] == "Planned end date": Pend = y[j+1][k]
            if y[j][k] == "Iteration": iter1 = y[j+1][k]
            if y[j][k] == "Status": stat = y[j+1][k]
            if y[j][k] == "Version":
                ver = y[j+1][k]
                breakloop = True

    TestRuns[kind] = [Name,Desc,Pstart,Pend,iter1,stat,ver]

df = pd.DataFrame.from_dict(TestRuns, orient='index')
#print(df)

for k,v in TestPlanRange.items():
    kind = k
    breakloop = False
    for j in range(v[0],v[2]):
        if breakloop == True: break
        for k in range(0,len(y[j])):
            #print(y[j][k])
            if y[j][k] == "Key": Key = y[j][k+1]
            if y[j][k] == "Name": Name = y[j][k+1]
            #if y[j][k] == "Objective": Obj = y[j][k]
            if y[j][k] == "Status":
                stat = y[j][k+1]
                breakloop = True

    TestPlans[kind] = [Key,Name,"None",stat]

#print(TestPlans)

for k,v in TestScriptRange.items():
    kind = k
    breakloop = False
    for j in range(v[0], v[2]):
        if breakloop == True: break
        for k in range(0,len(y[j])):
            if y[j][k] == "Status": Status = y[j][k + 1]
            if y[j][k] == "Name": Name1 = y[j][k + 1]
            if y[j][k] == "Objective": Obj1 = y[j][k]
            if y[j][k] == "Precondition": precon = y[j][k + 1]
            if y[j][k] == "Coverage": cov = y[j][k + 1]
            if y[j][k] == "Execution date": exdate = y[j][k + 1]
            if y[j][k] == "Estimated Time": estime = y[j][k + 1]
            if y[j][k] == "Actual Time": actime1 = y[j][k + 1]
            if y[j][k] == "Assignee": assignee = y[j][k + 1]
            if y[j][k] == "Environment": env = y[j][k + 1]
            if y[j][k] == "Type": type1 = y[j][k + 1]
            if y[j][k] == "Issues": issues = y[j][k + 1]
            if y[j][k] == "Attachments": attach = y[j][k + 1]
            if y[j][k] == "Test Script": breakloop = True

    TestScripts[kind] = [Status,Name1,Obj1,precon,cov,exdate,estime,assignee,env,type1,issues,attach]


Tscriptsdf = pd.DataFrame.from_dict(TestScripts, orient='index')

print(Tscriptsdf)