import unittest

from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def assert_invariants(self, linked):
        if linked._count == 0:
            self.assertIsNone(linked._head, "_head must be None when empty")
            self.assertIsNone(linked._tail, "_tail must be None when empty")
        else:
            self.assertIsNotNone(linked._head)
            self.assertIsNotNone(linked._tail)
            self.assertIsNone(linked._tail.next, "_tail.next must be None")

        reached = 0
        current = linked._head
        visited = set()
        while current is not None:
            self.assertNotIn(id(current), visited, "cycle detected in list")
            visited.add(id(current))
            reached += 1
            current = current.next

        self.assertEqual(reached, linked._count, "_count must match reachable nodes")
        self.assertEqual(reached, len(linked))

    def test_append_to_empty_list(self):
        linked = SinglyLinkedList()
        linked.append(10)
        self.assertEqual(list(linked), [10])
        self.assertEqual(len(linked), 1)
        self.assertEqual(linked._head.data, 10)
        self.assertIs(linked._head, linked._tail)
        self.assert_invariants(linked)

    def test_append_to_existing_list_updates_tail(self):
        linked = SinglyLinkedList()
        for value in (10, 20, 30):
            linked.append(value)
        self.assertEqual(list(linked), [10, 20, 30])
        self.assertEqual(len(linked), 3)
        self.assertEqual(linked._head.data, 10)
        self.assertEqual(linked._tail.data, 30)
        self.assertIsNone(linked._tail.next)
        self.assert_invariants(linked)

    def test_prepend_to_empty_list(self):
        linked = SinglyLinkedList()
        linked.prepend(10)
        self.assertEqual(list(linked), [10])
        self.assertEqual(len(linked), 1)
        self.assertIs(linked._head, linked._tail)
        self.assert_invariants(linked)

    def test_prepend_to_existing_list_updates_head(self):
        linked = SinglyLinkedList()
        for value in (10, 20, 30):
            linked.prepend(value)
        self.assertEqual(list(linked), [30, 20, 10])
        self.assertEqual(len(linked), 3)
        self.assertEqual(linked._head.data, 30)
        self.assertEqual(linked._tail.data, 10)
        self.assert_invariants(linked)

    def test_build_list_forward_preserves_order(self):
        values = [10, 20, 30, 40, 50]
        original = list(values)
        linked = SinglyLinkedList()
        linked.build_list_forward(values)
        self.assertEqual(list(linked), [10, 20, 30, 40, 50])
        self.assertEqual(len(linked), 5)
        self.assertEqual(linked._head.data, 10)
        self.assertEqual(linked._tail.data, 50)
        self.assertEqual(values, original, "input Python list cannot change")
        self.assert_invariants(linked)

    def test_build_list_backward_reverses_order(self):
        values = [10, 20, 30, 40, 50]
        original = list(values)
        linked = SinglyLinkedList()
        linked.build_list_backward(values)
        self.assertEqual(list(linked), [50, 40, 30, 20, 10])
        self.assertEqual(len(linked), 5)
        self.assertEqual(linked._head.data, 50)
        self.assertEqual(linked._tail.data, 10)
        self.assertEqual(values, original, "input Python list cannot change")
        self.assert_invariants(linked)

    def test_build_methods_with_empty_input(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([])
        self.assertTrue(linked.is_empty())
        linked.build_list_backward([])
        self.assertTrue(linked.is_empty())
        self.assert_invariants(linked)

    def test_contains_finds_present_and_reports_absent(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        self.assertTrue(linked.contains(10))
        self.assertTrue(linked.contains(20))
        self.assertTrue(linked.contains(30))
        self.assertFalse(linked.contains(99))
        self.assertFalse(linked.contains(15))

    def test_contains_on_empty_list_is_false(self):
        self.assertFalse(SinglyLinkedList().contains(10))

    def test_is_empty_transitions(self):
        linked = SinglyLinkedList()
        self.assertTrue(linked.is_empty())
        linked.append(1)
        self.assertFalse(linked.is_empty())
        linked.remove(1)
        self.assertTrue(linked.is_empty())

    def test_len_reflects_count(self):
        linked = SinglyLinkedList()
        self.assertEqual(len(linked), 0)
        linked.build_list_forward([1, 2, 3, 4])
        self.assertEqual(len(linked), 4)
        linked.remove(3)
        self.assertEqual(len(linked), 3)

    def test_forward_iteration_yields_values_in_order(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([1, 2, 3])
        collected = [value for value in linked]
        self.assertEqual(collected, [1, 2, 3])

    def test_str_shows_readable_chain(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        self.assertEqual(str(linked), "Head -> 10 -> 20 -> 30 -> None")
        self.assertEqual(str(SinglyLinkedList()), "Head -> None")

    def test_insert_after_interior_node(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        linked.insert_after(20, 25)
        self.assertEqual(list(linked), [10, 20, 25, 30])
        self.assertEqual(len(linked), 4)
        self.assertEqual(linked._tail.data, 30)
        self.assert_invariants(linked)

    def test_insert_after_tail_updates_tail(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        linked.insert_after(30, 40)
        self.assertEqual(list(linked), [10, 20, 30, 40])
        self.assertEqual(len(linked), 4)
        self.assertEqual(linked._tail.data, 40)
        self.assertIsNone(linked._tail.next)
        self.assert_invariants(linked)

    def test_insert_after_missing_value_raises(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        with self.assertRaises(ValueError):
            linked.insert_after(99, 100)
        self.assertEqual(list(linked), [10, 20, 30])
        self.assertEqual(len(linked), 3)
        self.assert_invariants(linked)

    def test_remove_head(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        linked.remove(10)
        self.assertEqual(list(linked), [20, 30])
        self.assertEqual(linked._head.data, 20)
        self.assertEqual(len(linked), 2)
        self.assert_invariants(linked)

    def test_remove_interior_node(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        linked.remove(20)
        self.assertEqual(list(linked), [10, 30])
        self.assertEqual(linked._head.data, 10)
        self.assertEqual(linked._tail.data, 30)
        self.assertEqual(len(linked), 2)
        self.assert_invariants(linked)

    def test_remove_tail_updates_tail(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        linked.remove(30)
        self.assertEqual(list(linked), [10, 20])
        self.assertEqual(linked._tail.data, 20)
        self.assertIsNone(linked._tail.next)
        self.assertEqual(len(linked), 2)
        self.assert_invariants(linked)

    def test_remove_only_node_empties_list(self):
        linked = SinglyLinkedList()
        linked.append(10)
        linked.remove(10)
        self.assertTrue(linked.is_empty())
        self.assertEqual(len(linked), 0)
        self.assertIsNone(linked._head)
        self.assertIsNone(linked._tail)
        self.assert_invariants(linked)

    def test_remove_missing_value_raises(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        with self.assertRaises(ValueError):
            linked.remove(99)
        self.assertEqual(list(linked), [10, 20, 30])
        self.assertEqual(len(linked), 3)
        self.assert_invariants(linked)

    def test_remove_removes_only_first_duplicate(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([5, 5, 5])
        linked.remove(5)
        self.assertEqual(list(linked), [5, 5])
        self.assertEqual(len(linked), 2)
        self.assert_invariants(linked)

    def test_remove_all_scattered_and_consecutive_matches(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([5, 1, 5, 5, 2, 5])
        removed = linked.remove_all(5)
        self.assertEqual(removed, 4)
        self.assertEqual(list(linked), [1, 2])
        self.assertEqual(len(linked), 2)
        self.assertEqual(linked._tail.data, 2)
        self.assert_invariants(linked)

    def test_remove_all_match_at_head_and_tail(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([7, 1, 2, 7])
        removed = linked.remove_all(7)
        self.assertEqual(removed, 2)
        self.assertEqual(list(linked), [1, 2])
        self.assertEqual(linked._head.data, 1)
        self.assertEqual(linked._tail.data, 2)
        self.assert_invariants(linked)

    def test_remove_all_consecutive_run_at_tail(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([1, 2, 3, 3, 3])
        removed = linked.remove_all(3)
        self.assertEqual(removed, 3)
        self.assertEqual(list(linked), [1, 2])
        self.assertEqual(linked._tail.data, 2)
        self.assertIsNone(linked._tail.next)
        self.assert_invariants(linked)

    def test_remove_all_no_matches_returns_zero(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([1, 2, 3])
        removed = linked.remove_all(99)
        self.assertEqual(removed, 0)
        self.assertEqual(list(linked), [1, 2, 3])
        self.assertEqual(len(linked), 3)
        self.assert_invariants(linked)

    def test_remove_all_every_node(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([4, 4, 4])
        removed = linked.remove_all(4)
        self.assertEqual(removed, 3)
        self.assertTrue(linked.is_empty())
        self.assertIsNone(linked._head)
        self.assertIsNone(linked._tail)
        self.assert_invariants(linked)

    def test_remove_all_on_empty_list_returns_zero(self):
        linked = SinglyLinkedList()
        self.assertEqual(linked.remove_all(1), 0)
        self.assert_invariants(linked)


if __name__ == "__main__":
    unittest.main()
