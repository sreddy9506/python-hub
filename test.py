# Gets the version report for all version of a project.
#Downloads and scp to /nfs/blackduck/user...
from bda_hubapi import HubAPI
import time
### Local Parameters == You must update these for this script to run
ENDPOINT ='https://bdhub-01.bdhub.crate.farm:443'
USERNAME = 'sysadmin'
PASSWORD = 'blackduck'
##### +++++++++++++++++++++++++++++++
#Create an instance of HubAPI with your endpoint
hub = HubAPI(ENDPOINT)

#Authenticate with your username and password
hub.authenticate(USERNAME, PASSWORD)

#Prompt for the project name
projectName = raw_input('Please enter the name of a valid project in the Black Duck Hub at '
    + ENDPOINT + '""')

#Get the project JSON from Hub
projectData = hub.getProjects(q='name:'+projectName)


# Get meta section for parseing
#Python dictionarys make it easy to traverse JSON data
#In this case we want the '_meta' section from the first entry of the 'items' list
project_metaData = projectData['items'][0]['_meta']

#Get link to Cannonical version
#canVersionLink = hub.getLink(project_metaData, 'canonicalVersion')

#Get link to Cannonical version
VersionLink = hub.getLink(project_metaData, 'versions')


#Get the version JSON from Hub
versionData = hub.getVersions(VersionLink)
res = []
v = []
for i in range(len(versionData['items'])):
    res = versionData['items'][i]['_meta']['href']
    v.append(res)
#Get the meta section of the version
versionMetaData = v
reportLink = []
reportsList = []
mostRecentReport = []
rLink = []
VData = []
for i in range(0,len(versionMetaData)-1):
#    VData = versionMetaData[i]
#    print (VData)
#    print ("second")
    rLink = hub.getVersions(versionMetaData[i])
for j in range(0,len(reportLink)-1):
        if reportLink != reportLink.empty:
            versionReport = hub.getLink(reportLink['_meta'], 'versionReport')
            print versionReport
        else:
            print("no url")


