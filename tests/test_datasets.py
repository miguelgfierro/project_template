from miguellib.datasets.dummy import dummy_dataset


def test_dummy_dataset():
    assert len(dummy_dataset()) == 4
    assert dummy_dataset() == [1, 2, 3, 4]
