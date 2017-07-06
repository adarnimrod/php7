from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_php7(Command):
    assert Command('php7.0 --version').stdout.startswith('PHP 7')


def test_composer(Command):
    assert Command('composer --version').stdout.startswith('Composer version')


def test_pear(Command):
    assert Command('pear version').stdout.startswith('PEAR Version')


def test_php_ini(Command):
    command = Command('php7.0 --info')
    assert command.rc == 0
    assert 'PHP Version => 7' in command.stdout
    assert 'syntax error' not in command.stdout
    assert 'syntax error' not in command.stderr
