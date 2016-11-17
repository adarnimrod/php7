def test_php5(Command):
    assert Command('php5 --version').stdout.startswith('PHP 5')


def test_composer(Command):
    assert Command('composer --version').stdout.startswith('Composer version')


def test_pear(Command):
    assert Command('pear version').stdout.startswith('PEAR Version')