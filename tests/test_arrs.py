import pytest

from utils import arrs, dicts


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


@pytest.mark.parametrize('coll, start, end, expected', [
    ([1, 2, 3], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([1, 2, 3], -2, None, [2, 3]),
    ([1, 2, 3], -5, None, [1, 2, 3]),
    ([], 0, None, [])
])
def test_slice(coll, start, end, expected):
    assert arrs.my_slice(coll, start, end) == expected


def test_get_val():
    data = {"vcs": "mercurial"}
    assert dicts.get_val(data, "vcs") == 'mercurial'
    assert dicts.get_val(data, "vcs", "git") == 'mercurial'
    assert dicts.get_val(data, "python", "git") == 'git'
    data = {}
    assert dicts.get_val(data, "python", "bazaar") == 'bazaar'


# import unittest
# from utils import arrs
#
#
# class TestArrs(unittest.TestCase):
#
#     def test_get(self):
#         self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
#         self.assertEqual(arrs.get([], 0, "test"), "test")
#
#     def test_slice(self):
#         self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
#         self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
#         self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
#         self.assertEqual(arrs.my_slice([1, 2, 3], -5), [1, 2, 3])
#         self.assertEqual(arrs.my_slice([], 0), [])
