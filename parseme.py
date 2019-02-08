import xmltodict

output = {}
bugCount = 0
low = 0
med = 0
high = 0

with open('dependency-check-report.xml') as fd:
    owasp_doc = xmltodict.parse(fd.read())

output['jenkins_name'] = str(owasp_doc['analysis']['projectInfo']['name'])
output['dependency_vuln_count'] = "TODO"

with open('target/spotbugsXml.xml') as fd2:
    spotbugs_doc = xmltodict.parse(fd2.read())

output['project_name'] = str(spotbugs_doc['BugCollection']['Project']['@projectName'])

for bug in spotbugs_doc['BugCollection']['BugInstance']:
    priority = str(bug['@priority'])
    if priority == "1":
        low += 1 
    elif priority == "2":
        med += 1 
    elif priority == "3":
        high += 1
    bugCount += 1 

output['spotbugs_total'] = bugCount
output['spotbugs_low'] = low
output['spotbugs_med'] = med
output['spotbugs_high'] = high

print(output)

