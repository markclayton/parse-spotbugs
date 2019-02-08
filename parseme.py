import xmltodict
import requests

output = {}
bugCount = 0
low = 0
med = 0
high = 0

endpoint = ""

with open('dependency-check-report.xml') as fd:
    owasp_doc = xmltodict.parse(fd.read())

output['jenkins_name'] = str(owasp_doc['analysis']['projectInfo']['name'])
output['dependency_vuln_count'] = "TODO"

with open('target/spotbugsXml.xml') as fd2:
    spotbugs_doc = xmltodict.parse(fd2.read())

output['project_name'] = str(spotbugs_doc['BugCollection']['Project']['@projectName'])

# https://spotbugs.readthedocs.io/en/stable/filter.html
# <Rank>
# This element matches warnings with a particular bug rank. 
# The value attribute should be an integer value between 1 and 20, 
# where 1 to 4 are scariest, 5 to 9 scary, 10 to 14 troubling, and 15 to 20 of concern bugs.

for bug in spotbugs_doc['BugCollection']['BugInstance']:
    priority = int(bug['@rank'])
    if priority in range(15,20):
        low += 1 
    elif priority in range(10,14):
        med += 1 
    elif priority in range(1,9):
        high += 1
    bugCount += 1 

output['spotbugs_total'] = bugCount
output['spotbugs_low'] = low
output['spotbugs_med'] = med
output['spotbugs_high'] = high

# r = requests.post(endpoint, data = output)
print(output)

