# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import httplib2
from oauth2client import client
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from PeerReview.Logger import getLogger
from django.contrib.auth import logout
from django.conf import settings
from oauth2client.file import Storage

log = getLogger("OAuth")
# HOST = 'http://localhost:8000'
redirect_uri = settings.HOST + '/auth/oauth2callback'

def login(request):
    if 'credentials' not in request.session:
        log.info("No Credentials Found. Getting Credentials")
        return redirect('oauth2callback')
    return redirect('/courses')


def auth_return(request):
    log.info(request)
    flow = client.flow_from_clientsecrets(
        'client_secret.json',
        scope= settings.SCOPES,
        redirect_uri=(redirect_uri))
    flow.params['access_type'] = 'offline'  # offline access
    flow.params['include_granted_scopes'] = 'true'  # incremental auth
    log.info("inside auth_return")
    if request.GET.get('code') is None:
        auth_uri = flow.step1_get_authorize_url()
        return HttpResponseRedirect(auth_uri)
    else:
        auth_code = request.GET.get('code')
        credentials = flow.step2_exchange(auth_code)
        request.session['credentials'] = credentials.to_json()
        return redirect('/courses')

def get_global_account_credentials():
    home_dir = os.getcwd()
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'classroom.googleapis.com-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    http = credentials.authorize(httplib2.Http())
    credentials.refresh(http)
    credentials = credentials.to_json()
    return credentials

def logout_page(request):
    del request.session['credentials']
    request.session.modified = True
    logout(request)
    return HttpResponseRedirect('/')