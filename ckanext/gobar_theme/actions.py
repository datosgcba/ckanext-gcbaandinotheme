# coding=utf-8
import ckan.logic as logic
import ckan.lib.base as base
import ckanext
import re
import sys
from ckan.lib.helpers import literal
import ckan.lib.helpers as h
import ckanext.gobar_theme.helpers as h_gobar
import ckan.model as model

_get_action = logic.get_action


def package_activity_list_html(context, data_dict):
    activity_stream = logic.action.get.package_activity_list(context, data_dict)
    offset = int(data_dict.get('offset', 0))
    extra_vars = {
        'controller': 'package',
        'action': 'activity',
        'id': data_dict['id'],
        'offset': offset,
    }
    return activity_list_to_html(
        context, activity_stream, extra_vars)   

def _resource_purge(context, data_dict):
    model = context['model']
    id = logic.get_or_bust(data_dict, 'id')
    entity = model.Resource.get(id)
    entity.purge()
    model.repo.commit_and_remove()


def _resource_delete_from_datastore(context, data_dict):
    id = logic.get_or_bust(data_dict, 'id')
    resource = model.Resource.get(data_dict['id'])
    if (resource is not None and
        resource.extras.get('datastore_active') is True):
            ckanext.datastore.logic.action.datastore_delete(context, {'resource_id': id, 'force': True})


def resource_delete_and_purge(context, data_dict):
    _resource_delete_from_datastore(context, data_dict)
    logic.action.delete.resource_delete(context, data_dict)
    _resource_purge(context, data_dict)


def group_delete_and_purge(context, data_dict):
    logic.action.delete._group_or_org_delete(context, data_dict)
    return logic.action.delete.group_purge(context, data_dict)


def _delete_and_purge_datasets_resources(context, data_dict):
    resources = logic.action.get.package_show(context, data_dict)['resources']
    for resource in resources:
        resource_delete_and_purge(context, {'id': resource['id']})


def dataset_delete_and_purge(context, data_dict):
    logic.action.delete.package_delete(context, data_dict)
    _delete_and_purge_datasets_resources(context, data_dict)
    return logic.action.delete.dataset_purge(context, data_dict)


def organization_delete_and_purge(context, data_dict):
    for suborganization in h_gobar.get_suborganizations():
        logic.action.delete._group_or_org_delete(context, {'id': suborganization}, is_org=True)
        logic.action.delete.group_purge(context, {'id': suborganization})
    logic.action.delete._group_or_org_delete(context, data_dict, is_org=True)
    return logic.action.delete.group_purge(context, data_dict)
