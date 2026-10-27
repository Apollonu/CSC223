import unittest

from split_evens_odds import SplitEvensOdds


class TestSplitEvensOdds(unittest.TestCase):
    def collect_nodes(self, linked):
        nodes = []
        current = linked._head
        while current is not None:
            nodes.append(current)
            current = current.next
        return nodes

    def assert_result_list_is_valid(self, linked):
        nodes = self.collect_nodes(linked)
        self.assertEqual(len(nodes), linked._count)
        self.assertEqual(len(nodes), len(linked))
        if not nodes:
            self.assertIsNone(linked._head)
            self.assertIsNone(linked._tail)
        else:
            self.assertIs(linked._head, nodes[0])
            self.assertIs(linked._tail, nodes[-1])
            self.assertIsNone(linked._tail.next)

    def assert_src_emptied(self, src):
        self.assertEqual(len(src), 0)
        self.assertEqual(src._count, 0)
        self.assertIsNone(src._head)
        self.assertIsNone(src._tail)
        self.assertTrue(src.is_empty())

    def test_mixed_values_split(self):
        src = SplitEvensOdds()
        src.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8])

        evens, odds = src.split_even_odd()

        self.assertEqual(list(evens), [2, 4, 6, 8])
        self.assertEqual(list(odds), [1, 3, 5, 7])
        self.assertEqual(len(evens), 4)
        self.assertEqual(len(odds), 4)
        self.assertEqual(evens._tail.data, 8)
        self.assertEqual(odds._tail.data, 7)
        self.assert_result_list_is_valid(evens)
        self.assert_result_list_is_valid(odds)
        self.assertEqual(len(evens) + len(odds), 8)
        self.assert_src_emptied(src)

    def test_relative_order_preserved_for_interleaved_values(self):
        src = SplitEvensOdds()
        src.build_list_forward([10, 7, 4, 3, 8, 1])

        evens, odds = src.split_even_odd()

        self.assertEqual(list(evens), [10, 4, 8])
        self.assertEqual(list(odds), [7, 3, 1])
        self.assert_result_list_is_valid(evens)
        self.assert_result_list_is_valid(odds)
        self.assert_src_emptied(src)

    def test_all_even_input(self):
        src = SplitEvensOdds()
        src.build_list_forward([2, 4, 6])

        evens, odds = src.split_even_odd()

        self.assertEqual(list(evens), [2, 4, 6])
        self.assertEqual(list(odds), [])
        self.assertEqual(len(evens), 3)
        self.assertEqual(len(odds), 0)
        self.assertEqual(evens._tail.data, 6)
        self.assert_result_list_is_valid(evens)
        self.assert_result_list_is_valid(odds)
        self.assert_src_emptied(src)

    def test_all_odd_input(self):
        src = SplitEvensOdds()
        src.build_list_forward([1, 3, 5])

        evens, odds = src.split_even_odd()

        self.assertEqual(list(evens), [])
        self.assertEqual(list(odds), [1, 3, 5])
        self.assertEqual(len(evens), 0)
        self.assertEqual(len(odds), 3)
        self.assertEqual(odds._tail.data, 5)
        self.assert_result_list_is_valid(evens)
        self.assert_result_list_is_valid(odds)
        self.assert_src_emptied(src)

    def test_single_even_value(self):
        src = SplitEvensOdds()
        src.append(8)

        evens, odds = src.split_even_odd()

        self.assertEqual(list(evens), [8])
        self.assertEqual(list(odds), [])
        self.assertIs(evens._head, evens._tail)
        self.assertIsNone(evens._tail.next)
        self.assert_result_list_is_valid(evens)
        self.assert_src_emptied(src)

    def test_single_odd_value(self):
        src = SplitEvensOdds()
        src.append(9)

        evens, odds = src.split_even_odd()

        self.assertEqual(list(evens), [])
        self.assertEqual(list(odds), [9])
        self.assertIs(odds._head, odds._tail)
        self.assertIsNone(odds._tail.next)
        self.assert_result_list_is_valid(odds)
        self.assert_src_emptied(src)

    def test_zero_and_negative_values(self):
        src = SplitEvensOdds()
        src.build_list_forward([0, -3, -4, 7])

        evens, odds = src.split_even_odd()

        self.assertEqual(list(evens), [0, -4])
        self.assertEqual(list(odds), [-3, 7])
        self.assertEqual(len(evens), 2)
        self.assertEqual(len(odds), 2)
        self.assert_result_list_is_valid(evens)
        self.assert_result_list_is_valid(odds)
        self.assertEqual(len(evens) + len(odds), 4)
        self.assert_src_emptied(src)

    def test_split_reuses_the_original_node_objects(self):
        src = SplitEvensOdds()
        src.build_list_forward([1, 2, 3, 4, 5, 6])

        before = self.collect_nodes(src)
        before_ids = [id(node) for node in before]

        evens, odds = src.split_even_odd()

        after = self.collect_nodes(evens) + self.collect_nodes(odds)
        after_ids = [id(node) for node in after]

        self.assertEqual(
            sorted(before_ids), sorted(after_ids),
            "lists must hold the same Node objects"
        )
        self.assertEqual(
            len(after), len(before),
            "no node lost or duplicated"
        )
        self.assertEqual(
            len(set(after_ids)), len(after_ids),
            "a node cannot appear in both result lists"
        )

    def test_total_result_nodes_equals_original_count(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        src = SplitEvensOdds()
        src.build_list_forward(values)

        evens, odds = src.split_even_odd()

        self.assertEqual(len(evens) + len(odds), len(values))
        self.assertEqual(
            list(evens) + list(odds),
            [v for v in values if v % 2 == 0] +
            [v for v in values if v % 2 == 1]
        )

    def test_empty_src_raises_value_error(self):
        src = SplitEvensOdds()
        with self.assertRaises(ValueError):
            src.split_even_odd()
        self.assert_src_emptied(src)

    def test_src_list_is_empty_after_successful_split(self):
        src = SplitEvensOdds()
        src.build_list_forward([2, 4, 1, 3])

        src.split_even_odd()

        self.assert_src_emptied(src)
        self.assertEqual(list(src), [])


if __name__ == "__main__":
    unittest.main()
