import cleanup as cu

FILE_DIR = './data/test.txt'

class Test_generate_zone_sets:
    lines = cu.generate_zones(FILE_DIR)

    def test_is_a_list(self):
        assert type(self.lines) == list

    def test_is_a_nested_list_with_2_lists(self):
       assertions = [True if len(line) == 2 else False for line in self.lines]
       assert False not in assertions

    def test_each_nested_list_is_of_length_2(self):
        assertions = [True if (len(line[0]) == 2 and len(line[1]) == 2) else False for line in self.lines]
        assert False not in assertions

    def test_examples(self):
        assert self.lines == [
            [ [2, 4], [6, 8] ],
            [ [2, 3], [4, 5] ],
            [ [5, 7], [7, 9] ],
            [ [2, 8], [3, 7] ],
            [ [6, 6], [4, 6] ],
            [ [2, 6], [4, 8] ],
        ]

class Test_count_subsets:
    subsets_num = cu.count_subsets(FILE_DIR)

    def test_subsets_is_int(self):
        assert type(self.subsets_num) == int
    
    def test_example(self):
        assert self.subsets_num == 2

class Test_count_overlaps:
    overlaps_num = cu.count_overlaps(FILE_DIR)

    def test_overlaps_is_int(self):
        assert type(self.overlaps_num) == int
    
    def test_example(self):
        assert self.overlaps_num == 4