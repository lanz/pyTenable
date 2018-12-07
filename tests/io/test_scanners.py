from tenable.errors import *
from ..checker import check, single
import uuid, pytest

@pytest.mark.vcr()
def test_scanner_control_scans_scanner_id_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.control_scan('nope', str(uuid.uuid4()), 'stop')

@pytest.mark.vcr()
def test_scanner_control_scans_scan_uuid_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.control_scan(1,1,'stop')

@pytest.mark.vcr()
def test_scanner_control_scans_action_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.control_scan(1,str(uuid.uuid4()), 1)

@pytest.mark.vcr()
def test_scanner_control_scans_action_unexpectedvalue(api):
    with pytest.raises(UnexpectedValueError):
        api.scanners.control_scan(1, str(uuid.uuid4()), 'nope')

@pytest.mark.vcr()
def test_scanner_control_scans_notfounderror(api):
    with pytest.raises(NotFoundError):
        api.scanners.control_scan(1, 
            'c5e3e4c9-ee47-4fbc-9e1d-d6f39801f56c', 'stop')

@pytest.mark.vcr()
def test_scanner_control_scans_permissionerror(stdapi):
    with pytest.raises(PermissionError):
        stdapi.scanners.control_scan(1, 
            'c5e3e4c9-ee47-4fbc-9e1d-d6f39801f56c', 'stop')

@pytest.mark.vcr()
def test_scanner_delete_id_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.delete('nope')

@pytest.mark.vcr()
def test_scanner_delete_notfound(api):
    with pytest.raises(NotFoundError):
        api.scanners.delete(1)

@pytest.mark.vcr()
def test_scanner_delete_permissionerror(stdapi, scanner):
    with pytest.raises(PermissionError):
        stdapi.scanners.delete(scanner['id'])

@pytest.mark.skip(reason="We don't want to actually delete scanners.")
def test_scanner_delete(api, scanner):
    api.scanners.delete(scanner['id'])

@pytest.mark.vcr()
def test_scanner_details_id_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.details('nope')

@pytest.mark.vcr()
def test_scanner_details_notfounderror(api):
    with pytest.raises(NotFoundError):
        api.scanners.details(1)

@pytest.mark.vcr()
def test_scanner_details_permissionerror(stdapi, scanner):
    with pytest.raises(PermissionError):
        stdapi.scanners.details(scanner['id'])

@pytest.mark.vcr()
def test_scanner_details(api, scanner):
    check = api.scanners.details(scanner['id'])
    assert check['id'] == scanner['id']

@pytest.mark.vcr()
def test_scanner_edit_id_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.edit('nope')

@pytest.mark.vcr()
def test_sanner_edit_plugin_update_typeerror(api, scanner):
    with pytest.raises(TypeError):
        api.scanners.edit(scanner['id'], force_plugin_update='yes')

@pytest.mark.vcr()
def test_scanner_edit_ui_update_typeerror(api, scanner):
    with pytest.raises(TypeError):
        api.scanners.edit(scanner['id'], force_ui_update='yes')

@pytest.mark.vcr()
def test_scanner_edit_finish_update_typeerror(api, scanner):
    with pytest.raises(TypeError):
        api.scanners.edit(scanner['id'], finish_update='yes')

@pytest.mark.vcr()
def test_scanner_edit_registration_code_typeerror(api, scanner):
    with pytest.raises(TypeError):
        api.scanners.edit(scanner['id'], registration_code=False)

@pytest.mark.vcr()
def test_scanner_edit_aws_update_typeerror(api, scanner):
    with pytest.raises(TypeError):
        api.scanners.edit(scanner['id'], aws_update_interval='no')

@pytest.mark.vcr()
@pytest.mark.xfail(raises=PermissionError)
def test_scanner_edit_notfounderror(api):
    with pytest.raises(NotFoundError):
        api.scanners.edit(1, force_ui_update=True)

@pytest.mark.vcr()
def test_scanner_edit_permissionserror(stdapi, scanner):
    with pytest.raises(PermissionError):
        stdapi.scanners.edit(scanner['id'], force_ui_update=True)

@pytest.mark.vcr()
@pytest.mark.xfail(raises=PermissionError)
def test_scanner_edit(api, scanner):
    api.scanners.edit(scanner['id'], force_plugin_update=True)

@pytest.mark.vcr()
def test_scanner_get_aws_targets_id_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.get_aws_targets('nope')

@pytest.mark.vcr()
def test_scanner_get_aws_targets_notfounderror(api):
    with pytest.raises(NotFoundError):
        api.scanners.get_aws_targets(1)

@pytest.mark.vcr()
@pytest.mark.xfail(raises=NotFoundError)
def test_scanner_get_aws_targets_permissionerror(stdapi):
    with pytest.raises(PermissionError):
        stdapi.scanners.get_aws_targets(1)

@pytest.mark.skip(reason="No AWS Environment to test against.")
@pytest.mark.vcr()
def test_scanner_get_aws_targets(api, scanner):
    pass

@pytest.mark.vcr()
def test_scanner_key_id_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.get_scanner_key('nope')

@pytest.mark.vcr()
def test_scanner_key(api, scanner):
    assert isinstance(api.scanners.get_scanner_key(scanner['id']), str)

@pytest.mark.vcr()
def test_get_scans_id_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.get_scans('nope')

@pytest.mark.vcr()
def test_get_scans_notfounderror(api):
    with pytest.raises(NotFoundError):
        api.scanners.get_scans(1)

@pytest.mark.vcr()
def test_get_scans_permissionerror(stdapi, scanner):
    with pytest.raises(PermissionError):
        stdapi.scanners.get_scans(scanner['id'])

@pytest.mark.vcr()
def test_get_scans(api, scanner):
    assert isinstance(api.scanners.get_scans(scanner['id']), list)

@pytest.mark.vcr()
def test_list_scanners_permissionerror(stdapi):
    with pytest.raises(PermissionError):
        stdapi.scanners.list()

@pytest.mark.vcr()
def test_list_scanners(api):
    assert isinstance(api.scanners.list(), list)

@pytest.mark.vcr()
def test_link_state_id_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.toggle_link_state('nope', True)

@pytest.mark.vcr()
def test_link_state_linked_typeerror(api):
    with pytest.raises(TypeError):
        api.scanners.toggle_link_state(1, 'False')

@pytest.mark.vcr()
def test_link_state_permissionerror(stdapi, scanner):
    with pytest.raises(PermissionError):
        stdapi.scanners.toggle_link_state(scanner['id'], True)

@pytest.mark.vcr()
def test_link_state(api, scanner):
    api.scanners.toggle_link_state(scanner['id'], True)