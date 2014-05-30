# -*- coding:utf-8 -*-
import pytest
# node-semver/test/index.js

#  [version1, version2]
#  version1 should be greater than version2
cands = [
    ['0.0.0', '0.0.0-foo', False],
    ['0.0.1', '0.0.0', False],
    ['1.0.0', '0.9.9', False],
    ['0.10.0', '0.9.0', False],
    ['0.99.0', '0.10.0', False],
    ['2.0.0', '1.2.3', False],
    ['v0.0.0', '0.0.0-foo', True],
    ['v0.0.1', '0.0.0', True],
    ['v1.0.0', '0.9.9', True],
    ['v0.10.0', '0.9.0', True],
    ['v0.99.0', '0.10.0', True],
    ['v2.0.0', '1.2.3', True],
    ['0.0.0', 'v0.0.0-foo', False],
    ['0.0.1', 'v0.0.0', False],
    ['1.0.0', 'v0.9.9', False],
    ['0.10.0', 'v0.9.0', False],
    ['0.99.0', 'v0.10.0', False],
    ['2.0.0', 'v1.2.3', False],
    ['1.2.3', '1.2.3-asdf', False],
    ['1.2.3', '1.2.3-4', False],
    ['1.2.3', '1.2.3-4-foo', False],
    ['1.2.3-5-foo', '1.2.3-5', False],
    ['1.2.3-5', '1.2.3-4', False],
    ['1.2.3-5-foo', '1.2.3-5-Foo', False],
    ['3.0.0', '2.7.2+asdf', False],
    ['1.2.3-a.10', '1.2.3-a.5', False],
    ['1.2.3-a.b', '1.2.3-a.5', False],
    ['1.2.3-a.b', '1.2.3-a', False],
    ['1.2.3-a.b.c.10.d.5', '1.2.3-a.b.c.5.d.100', False],
]


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_gt(v0, v1, loose):
    from semver import gt
    assert gt(v0, v1, loose) is True


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_lt(v0, v1, loose):
    from semver import lt
    lt(v1, v0, loose) is True


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_ngt(v0, v1, loose):
    from semver import gt
    (not gt(v1, v0, loose)) is True


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_nlt(v0, v1, loose):
    from semver import lt
    (not lt(v0, v1, loose)) is True


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_eq(v0, v1, loose):
    from semver import eq
    eq(v0, v1, loose) is True


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_eq2(v0, v1, loose):
    from semver import eq
    eq(v1, v0, loose) is True


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_cmp(v0, v1, loose):
    from semver import cmp
    cmp(v1, "==", v1, loose) is True


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_cmp2(v0, v1, loose):
    from semver import cmp
    cmp(v0, ">=", v1, loose) is True


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_cmp3(v0, v1, loose):
    from semver import cmp
    cmp(v1, "<=", v0, loose) is True


@pytest.mark.parametrize("v0, v1, loose", cands)
def test_cmp4(v0, v1, loose):
    from semver import cmp
    cmp(v0, "!=", v1, loose) is True