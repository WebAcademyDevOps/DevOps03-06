import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_mssql_service_state(host):
    assert host.service("mssql-server").is_running == True
    assert host.service("mssql-server").is_enabled == True
    assert host.service("mssql-server").is_masked == False

# def test_mssql_service_property_valid(host):
#     # mssql_service = host.service("mssql-server")
#     # assert mssql_service.systemd_properties["LimitNPROC"] == "infinity"
#     # assert mssql_service.systemd_properties["LimitNOFILE"] == "infinity"


def test_mssql_socket_listen(host):
    assert host.socket("tcp://127.0.0.1:1433").is_listening == True
    assert host.socket("tcp://0.0.0.0:1433").is_listening == True
