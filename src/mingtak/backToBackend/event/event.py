# -*- coding: utf-8 -*-
from plone import api
from mingtak.backToBackend import _
from zope.globalrequest import getRequest

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import transaction_note


def toFolderContents(obj, event):
    """
    Return to Folder Contents
    """
    request = getRequest()
    try:
        folder = obj.getParentNode()
    except:
        return
    if folder == None:
        try:
            folder = api.portal.get()
        except:
            return
    elif getattr(obj, 'portal_type', None) == 'Plone Site':
        folder = obj

    if request:
        request.response.redirect('%s/folder_contents' % folder.absolute_url())


def back_to_cover(event):
    request = getRequest()
    portal = api.portal.get()
    request.response.redirect(portal.absolute_url())

def move_to_top(item, event):
    request = getRequest()
    folder = item.getParentNode()
    if not hasattr(folder, 'moveObjectsToTop'):
        return
    folder.moveObjectsToTop(item.id)
    abs_url = folder.absolute_url()
    request.response.redirect('%s/folder_contents' %abs_url)
