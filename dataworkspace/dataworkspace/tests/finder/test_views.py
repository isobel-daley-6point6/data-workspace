import pytest

from django.conf import settings
from django.urls import reverse
from waffle.testutils import override_flag

from dataworkspace.tests import factories


@override_flag(settings.DATASET_FINDER_ADMIN_ONLY_FLAG, active=True)
def test_find_datasets_default(client, mocker):
    response = client.get(reverse('finder:find_datasets'))

    assert response.status_code == 200
    assert b"Search for master datasets in Data Workspace" in response.content


@override_flag(settings.DATASET_FINDER_ADMIN_ONLY_FLAG, active=True)
def test_find_datasets_with_no_results(client, mocker):
    dataset_search = mocker.patch('elasticsearch.Elasticsearch.search')
    dataset_search.return_value = {
        'took': 11,
        'timed_out': False,
        '_shards': {'total': 45, 'successful': 45, 'skipped': 0, 'failed': 0},
        'hits': {
            'total': {'value': 0, 'relation': 'eq'},
            'max_score': None,
            'hits': [],
        },
    }
    response = client.get(reverse('finder:find_datasets'), {"q": "search"})

    assert response.status_code == 200
    assert response.context["results"] is None

    assert b"There are no matches for the phrase" in response.content


@pytest.mark.django_db(transaction=True)
@override_flag(settings.DATASET_FINDER_ADMIN_ONLY_FLAG, active=True)
def test_find_datasets_with_results(client, mocker, dataset_finder_db):
    master_dataset = factories.MasterDataSetFactory()
    factories.SourceTableFactory(dataset=master_dataset, schema='public', table='data')

    dataset_search = mocker.patch('elasticsearch.Elasticsearch.search')
    dataset_search.return_value = {
        'took': 11,
        'timed_out': False,
        '_shards': {'total': 45, 'successful': 45, 'skipped': 0, 'failed': 0},
        'hits': {
            'total': {'value': 1260, 'relation': 'eq'},
            'max_score': None,
            'hits': [],
        },
        'aggregations': {
            'indexes': {
                'doc_count_error_upper_bound': 0,
                'sum_other_doc_count': 0,
                'buckets': [
                    {'key': '20210316t070000--public--data--1', 'doc_count': 1260},
                ],
            }
        },
    }
    response = client.get(reverse('finder:find_datasets'), {"q": "search"})

    assert response.status_code == 200
    assert len(response.context["results"]) == 1
    result = response.context["results"][0]
    assert result.name == 'public.data'
    assert result.table_matches[0].schema == 'public'
    assert result.table_matches[0].table == 'data'
    assert result.table_matches[0].count == 1260


@pytest.mark.django_db(transaction=True)
@override_flag(settings.DATASET_FINDER_ADMIN_ONLY_FLAG, active=True)
def test_search_in_data_explorer(client, mocker, dataset_finder_db):
    master_dataset = factories.MasterDataSetFactory()
    factories.SourceTableFactory(dataset=master_dataset, schema='public', table='data')

    response = client.get(
        reverse(
            'finder:search_in_data_explorer',
            kwargs={'schema': 'public', 'table': 'data'},
        ),
        {"q": "search"},
    )

    assert response.status_code == 302
    assert reverse('explorer:index') in response['Location']
