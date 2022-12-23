import supply as ss

FILE_DIR = './data/test.txt'

class Test_create_stacks_from_input:
    stacks = ss.create_stacks_from_input(FILE_DIR)

    def test_stacks_is_a_dict(self):
        assert type(self.stacks) == dict
    
    def test_example(self):
        assert self.stacks == {
            '1': ['Z', 'N'],
            '2': ['M', 'C', 'D'],
            '3': ['P']
        }

class Test_create_operations_moves_dict:
    operations = ss.create_operations_moves_dict(FILE_DIR)

    def test_operations_is_list(self):
        assert type(self.operations) == list
    
    def test_each_element_in_list_is_dict(self):
        assertions = [True if type(operation) == dict else None for operation in self.operations]
        assert False not in assertions
    
    def test_example(self):
        assert self.operations == [
            {
                'qty': 1,
                'from': 2,
                'to': 1
            },
            {
                'qty': 3,
                'from': 1,
                'to': 3
            },
            {
                'qty': 2,
                'from': 2,
                'to': 1
            },
            {
                'qty': 1,
                'from': 1,
                'to': 2
            },        
        ]

class Test_operate_crate_mover_9000:
    stacks = ss.create_stacks_from_input(FILE_DIR)
    operations = ss.create_operations_moves_dict(FILE_DIR)
    sorted_stacks = ss.operate_crate_mover_9000(stacks, operations)

    def test_sorted_stacks_is_dict(self):
        assert type(self.sorted_stacks) == dict

    def test_example(self):
        assert self.sorted_stacks == {
            '1': ['C'],
            '2': ['M'],
            '3': ['P', 'D', 'N', 'Z']
        }

class Test_operate_crate_mover_9001:
    stacks = ss.create_stacks_from_input(FILE_DIR)
    operations = ss.create_operations_moves_dict(FILE_DIR)
    sorted_stacks = ss.operate_crate_mover_9001(stacks, operations)

    def test_sorted_stacks_is_dict(self):
        assert type(self.sorted_stacks) == dict

    def test_example(self):
        assert self.sorted_stacks == {
            '1': ['M'],
            '2': ['C'],
            '3': ['P', 'Z', 'N', 'D']
        }


class Test_top_elements_in_crates:
    top_stacks_9000 = ss.top_elements_in_crates(FILE_DIR, 'CrateMover 9000')

    top_stacks_9001 = ss.top_elements_in_crates(FILE_DIR, 'CrateMover 9001')

    def test_stacks_is_str(self):
        assert type(self.top_stacks_9000) == str and type(self.top_stacks_9001) == str

    def test_example_9000(self):
        assert self.top_stacks_9000 == 'CMZ'
    
    def test_example_9001(self):
        assert self.top_stacks_9001 == 'MCD'