from apiclient import discovery
from oauth2client import client
from PeerReview.Logger import getLogger
import httplib2

log = getLogger("Service")


# reference: 
# https://stackoverflow.com/a/44518587/8741626  make cache_discovery=False for all

def getClassRoomService(credentials):
    http = client.OAuth2Credentials.from_json(credentials).authorize(httplib2.Http())
    return discovery.build('classroom', 'v1', http=http, cache_discovery=False)


def getDriveService(credentials):
    http = client.OAuth2Credentials.from_json(credentials).authorize(httplib2.Http())
    return discovery.build('drive', 'v3', http=http, cache_discovery=False)


def getSheetService(credentials):
    http = client.OAuth2Credentials.from_json(credentials).authorize(httplib2.Http())
    return discovery.build('sheets', 'v4', http=http, cache_discovery=False)


def getMailService(credentials):
    http = client.OAuth2Credentials.from_json(credentials).authorize(httplib2.Http())
    return discovery.build('gmail', 'v1', http=http, cache_discovery=False)
