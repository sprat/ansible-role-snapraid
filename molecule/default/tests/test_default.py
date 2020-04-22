import os

import testinfra.utils.ansible_runner

here = os.path.dirname(__file__)
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def read_reference_file():
    with open(os.path.join(here, 'snapraid.reference.conf')) as reference_file:
        return reference_file.read()


def test_configuration_file(host):
    reference = read_reference_file()
    configuration = host.file("/etc/snapraid.conf").content_string
    assert configuration == reference
