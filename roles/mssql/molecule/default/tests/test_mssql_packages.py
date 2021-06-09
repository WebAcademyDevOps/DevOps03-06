import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_mssql_packagee_has_desired_release_installed(host):
    assert host.package("mssql-server").version == "15.0.4123.1-5"
