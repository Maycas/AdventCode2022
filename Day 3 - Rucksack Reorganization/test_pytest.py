import rucksack as ru

FILE_DIR = './test_file.txt'

class Test_format_input:
    rucksacks = ru.format_input('./test_file.txt')

    def test_result_is_a_list(self):
        assert type(self.rucksacks) == list

    def test_result_is_nested_array_with_length_2(self):
        length_is_2 = False
        for rucksack in self.rucksacks:
            if len(rucksack) == 2:
                length_is_2 = True
            else:
                length_is_2 = False
        assert length_is_2    

    def test_all_compartments_are_of_same_length(self):
        all_same_length = False
        for rucksack in self.rucksacks:
            for compartment in rucksack:
                all_same_length = ( len(compartment[0]) == len(compartment[1]) )
        assert all_same_length

    def test_example_1(self):
        compartments = self.rucksacks[0]
        assert (compartments[0] == 'vJrwpWtwJgWr') and (compartments[1] == 'hcsFMMfFFhFp')

    def test_example_2(self):
        compartments = self.rucksacks[1]
        assert (compartments[0] == 'jqHRNqRjqzjGDLGL') and (compartments[1] == 'rsFMfFZSrLrFZsSL')

    def test_example_3(self):
        compartments = self.rucksacks[2]
        assert (compartments[0] == 'PmmdzqPrV') and (compartments[1] == 'vPwwTWBwg')

class Test_find_common_items:
    rucksacks = ru.format_input('./test_file.txt')

    def test_common_items_is_a_list(self):
        assert type(ru.find_common_items(self.rucksacks[0])) == list

    def test_example_1(self):
        assert ru.find_common_items(self.rucksacks[0]) == ['p']
    
    def test_example_2(self):
        assert ru.find_common_items(self.rucksacks[1]) == ['L']
    
    def test_example_3(self):
        assert ru.find_common_items(self.rucksacks[2]) == ['P']
    
class Test_assign_priorities:
    priorities_dict = ru.generate_prio_dict()
    
    def test_returns_an_int(self):
        assert type(ru.assign_priorities(['p'], self.priorities_dict)) == int

    def test_example_1_common_item_1(self):
        assert ru.assign_priorities(['p'], self.priorities_dict) == 16

    def test_example_1_common_item_2(self):
        assert ru.assign_priorities(['L'], self.priorities_dict) == 38

    def test_example_2_common_items_1(self):
        assert ru.assign_priorities(['p', 'L'], self.priorities_dict) == (16 + 38)

    def test_example_2_common_items_2(self):
        assert ru.assign_priorities(['t', 's'], self.priorities_dict) == (20 + 19)

class Test_calculate_priority_sum:

    def test_e2e(self):
        assert ru.calculate_priority_sum(FILE_DIR) == 157