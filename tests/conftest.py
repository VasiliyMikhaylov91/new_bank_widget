import pytest

@pytest.fixture
def card_numbers():
    return [(7000792289606361, '7000 79XX XXXX 6361'),
            ('92289', 'XXX89'),
            ('7000792289606361653', '7000 79XX XXXX XXX1 653'),
            (None, None)]


@pytest.fixture
def account_numbers():
    return [(73654108430135874305, '**4305'),
            ('73654108430135874305654221', '**4221'),
            ('736541084301358', '**1358'),
            (7365, None)]