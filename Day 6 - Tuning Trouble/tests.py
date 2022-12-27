import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.utils import read_list

import tuning as tng


class Test_find_marker:

    def test_returns_int(self):
        marker = tng.find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4)
        assert type(marker) == int

    def test_mjqjpqmgbljsphdztnvjfqwrcgsmlb_buff_4(self):
        marker = tng.find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4)
        assert marker == 7

    def test_bvwbjplbgvbhsrlpgdmjqwftvncz_buff_4(self):
        marker = tng.find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 4)
        assert marker == 5

    def test_nppdvjthqldpwncqszvftbrmjlhg_buff_4(self):
        marker = tng.find_marker('nppdvjthqldpwncqszvftbrmjlhg', 4)
        assert marker == 6

    def test_nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg_buff_4(self):
        marker = tng.find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4)
        assert marker == 10

    def test_zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw_buff_4(self):
        marker = tng.find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4)
        assert marker == 11

    def test_mjqjpqmgbljsphdztnvjfqwrcgsmlb_buff_14(self):
        marker = tng.find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)
        assert marker == 19

    def test_bvwbjplbgvbhsrlpgdmjqwftvncz_buff_14(self):
        marker = tng.find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 14)
        assert marker == 23

    def test_nppdvjthqldpwncqszvftbrmjlhg_buff_14(self):
        marker = tng.find_marker('nppdvjthqldpwncqszvftbrmjlhg', 14)
        assert marker == 23

    def test_nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg_buff_14(self):
        marker = tng.find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14)
        assert marker == 29

    def test_zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw_buff_14(self):
        marker = tng.find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14)
        assert marker == 26



