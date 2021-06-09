import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_mssql_databases_exist(host):
    cmd = host.run('/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Passwor8!" -Q "SELECT Name from sys.Databases"')
    assert "2804" in cmd.stdout
    assert "webacademy" in cmd.stdout
