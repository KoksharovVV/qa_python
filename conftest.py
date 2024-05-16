import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def book(collector):
    collector.add_new_book('Наименование')
    return collector
