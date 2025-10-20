#!/usr/bin/env python3

from unittest import mock

import pytest

from cloudinit.sources.DataSourceEc2Kubernetes import (
    DataSourceEc2Kubernetes,
    DataSourceEc2KubernetesLocal,
)


def test_no_recursion_in_get_data():
    ds = DataSourceEc2KubernetesLocal(sys_cfg={}, distro=None, paths=None)

    with mock.patch.object(
        DataSourceEc2Kubernetes, "_get_data", return_value=True
    ) as mock_parent_get_data:
        try:
            result = ds._get_data()
        except RecursionError as e:
            pytest.fail(f"RecursionError occurred: {e}")
