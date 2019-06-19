import pandas as pd

file = open(r'''/Users/hari/Desktop/CompTestResults.txt''', 'r')

x = [i.strip().split('\t') for i in file.readlines()]
y = list(filter(None, x))
TestPlanRange = {}
TestRunRange = {}
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
            TSdetstarti = i
            TSdetstartj = j
            count=1
            for TS in range(i,len(y)):
                if y[TS-1][0] == "Test Script":
                    TestScriptRange[TestRun] = [TestScript,count]
                    count = y[TS][0]
            TSdetendi = i
            TSdetendj = j
            TScount = count
            #count = 1

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

    dict[kind] = [Name,Desc,Pstart,Pend,iter1,stat,ver]

df = pd.DataFrame.from_dict(dict, orient='index')
print(df)