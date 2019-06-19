import pandas as pd


def Testscripts(Startline, Endline, ScriptRef):
    Scriptdetails = {}
    count = 1
    Scriptdetails["ScriptKey"] = ScriptRef
    for Scripts in range(Startline + 1, Endline):
        for ScriptDets in range(0, len(y[Scripts])):

            if y[Scripts][ScriptDets] == "Status":
                #Scriptdetails["Status"] = y[Scripts][ScriptDets + 1]
                #Scriptdetails["Number"] = count
                print("Status",y[Scripts][ScriptDets + 1])
                print("Script no.",count)

            if y[Scripts][ScriptDets] == "Details":
                while y[Scripts + 1][ScriptDets] != "Test Data":
                    #Scriptdetails["Details"] = y[Scripts + 1][ScriptDets]
                    print("Details",y[Scripts + 1][ScriptDets], end='')
                    Scripts += 1

            if y[Scripts][ScriptDets] == "Test Data":
                #Scriptdetails["Status"] = y[Scripts][ScriptDets + 1]
                print("Test Data",y[Scripts][ScriptDets + 1])

            if y[Scripts][ScriptDets] == "Expected Result":
                while y[Scripts][ScriptDets + 1] != "Actual Result":
                    #Scriptdetails["Expected Result"] = Scriptdetails["Expected Result"] + y[Scripts + 1][ScriptDets]
                    print(y[Scripts + 1][ScriptDets])

            if y[Scripts][ScriptDets] == "Actual Result":
                Scriptdetails["Actual Result"] = y[Scripts][ScriptDets + 1]

            if y[Scripts][ScriptDets] == "Attachments":
                Scriptdetails["Attachments"] = y[Scripts][ScriptDets + 1]

            if y[Scripts][ScriptDets] == "Issues":
                Scriptdetails["Issues"] = y[Scripts][ScriptDets + 1]
                count += 1

    return Scriptdetails


file = open(r'''/Users/hari/Desktop/CompTestResults.txt''', 'r')
a = []
Key = []

TestRunRange = []
TestResultsRange = []
TestScriptsRange = []



dict = {}

x = [i.strip().split('\t') for i in file.readlines()]
y = list(filter(None, x))

print(y)

for i in range(0, len(y)):
    if len(y[i]) > 1:
        for j in range(0, len(y[i])):
            if y[i][j] == "Key" and y[i][j + 1][0:8] == "SFHTCM-R":
                #Key.append((y[i][j + 1], i))
                TestRunRange.append()

# for i in range(0,len(Key)):
for j in range(int(Key[0][1]), int(Key[1][1])):
    for k in range(0, len(y[j])):
        if y[j][k] == "Key" and y[j][k + 1][0:8] == "SFHTCM-T":
            dict[y[j][k]] = y[j][k + 1]
            print(y[j][k + 1])
        if y[j][k] == "Status":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Name":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Objective":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Precondition":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Coverage":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Execution date":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Estimated Time":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Actual Time":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Assignee":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Environment":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Type":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Issues":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Attachments":
            dict[y[j][k]] = y[j][k + 1]
        if y[j][k] == "Test Script":
            dict[y[j][k]] = Testscripts(j, Key[1][1], 12345)
            dict[y[j][k]] = "Tests"
    print(y[j])

df = pd.DataFrame.from_dict(dict, orient='index')


print(dict)

