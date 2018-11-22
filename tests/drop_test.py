from common import *

def test_drop(ds_local):
    ds = ds_local
    dsd = ds.drop(ds.x)
    assert 'x' not in dsd.get_column_names()
    dsd = ds.drop([ds.x, 'y'])
    assert 'x' not in dsd.get_column_names()
    assert 'y' not in dsd.get_column_names()

    ds.drop([ds.x, 'y'], inplace=True)
    assert 'x' not in ds.get_column_names()
    assert 'y' not in ds.get_column_names()

def test_drop_depending(ds_local):
    ds = ds_local
    ds['r'] = ds.x + ds.y
    ds.drop(ds.x, inplace=True)
    assert 'x' not in ds.get_column_names()
    assert '__x' in ds.get_column_names(hidden=True)

    ds.drop(ds.y, inplace=True, check=False)
    assert 'y' not in ds.get_column_names()
    assert '__y' not in ds.get_column_names(hidden=True)

def test_drop_depending_filtered(ds_filtered):
    ds = ds_filtered
    ds.drop(ds.x, inplace=True)
    assert 'x' not in ds.get_column_names()
    assert '__x' in ds.get_column_names(hidden=True)
    ds.y.values  # make sure we can evaluate y
