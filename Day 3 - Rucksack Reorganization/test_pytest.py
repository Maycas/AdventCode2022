import rucksack as ru

FILE_DIR = './data/test_file.txt'

class Test_split_rucksack_compartments:
    rucksacks = ru.split_rucksacks_compartments(FILE_DIR)

    def test_result_is_a_list(self):
        assert type(self.rucksacks) == list

    def test_result_is_nested_array_with_length_2(self):
        length_is_2 = []
        for rucksack in self.rucksacks:
            if len(rucksack) == 2:
                length_is_2.append(True)
            else:
                length_is_2.append(False)
        assert False not in length_is_2    

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

class Test_group_packs_of_3_rucksacks:
    rucksacks = ru.group_packs_of_3_rucksacks(FILE_DIR)

    def test_result_is_a_list(self):
        assert type(self.rucksacks) == list

    def test_result_is_nested_array_with_length_3(self):
        length_is_3 = []
        for rucksack in self.rucksacks:
            if len(rucksack) == 3:
                length_is_3.append(True)
            else:
                length_is_3.append(False)
        assert False not in length_is_3

    def test_example_1(self):
        assert self.rucksacks[0] == [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg'
        ]

    def test_example_2(self):
        assert self.rucksacks[1] == [
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw'
        ]


class Test_find_common_items_per_rucksack:
    rucksacks = ru.split_rucksacks_compartments(FILE_DIR)

    def test_common_items_is_a_list(self):
        assert type(ru.find_common_items_per_rucksack(self.rucksacks[0])) == list

    def test_example_1(self):
        assert ru.find_common_items_per_rucksack(self.rucksacks[0]) == ['p']
    
    def test_example_2(self):
        assert ru.find_common_items_per_rucksack(self.rucksacks[1]) == ['L']
    
    def test_example_3(self):
        assert ru.find_common_items_per_rucksack(self.rucksacks[2]) == ['P']


class Test_find_common_badges_in_grouped_rucksacks:
    rucksacks = ru.group_packs_of_3_rucksacks(FILE_DIR)

    def test_common_items_is_a_list(self):
        assert type(ru.find_common_badges_in_grouped_rucksacks(self.rucksacks[0])) == list

    def test_example_1(self):
        assert ru.find_common_badges_in_grouped_rucksacks(self.rucksacks[0]) == ['r']
    
    def test_example_1(self):
        assert ru.find_common_badges_in_grouped_rucksacks(self.rucksacks[1]) == ['Z']


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


class Test_priorities_aggregation:
    priorities_dict = ru.generate_prio_dict()

    def test_e2e_returns_int(self):
        assert type(ru.priorities_aggregation(FILE_DIR, self.priorities_dict, ru.split_rucksacks_compartments, ru.find_common_items_per_rucksack, ru.assign_priorities)) == int
    
    def test_e2e_part1(self):
        assert ru.priorities_aggregation(FILE_DIR, self.priorities_dict, ru.split_rucksacks_compartments, ru.find_common_items_per_rucksack, ru.assign_priorities) == 157

    def test_e2e_part2(self):
        assert ru.priorities_aggregation(FILE_DIR, self.priorities_dict, ru.group_packs_of_3_rucksacks, ru.find_common_badges_in_grouped_rucksacks, ru.assign_priorities) == 70