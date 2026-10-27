from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

def show(label, value):
    print(f"  {label:<30}{value}")

def node_ids(linked):
    pairs = []
    current = linked._head
    while current is not None:
        pairs.append((current.data, id(current)))
        current = current.next
    return pairs

def demo_part_one():
    values = [10, 20, 30, 40, 50]

    print("\nbuild_list_forward([10, 20, 30, 40, 50])")
    forward = SinglyLinkedList()
    forward.build_list_forward(values)
    show("linked list:", forward)
    show("length:", len(forward))
    show("input Python list:", values)

    print("\nbuild_list_backward([10, 20, 30, 40, 50])")
    backward = SinglyLinkedList()
    backward.build_list_backward(values)
    show("linked list:", backward)
    show("length:", len(backward))
    show("input Python list:", values)

    print("\nappend(60) and prepend(5) on the reversed list")
    backward.append(60)
    show("after append(60):", backward)
    backward.prepend(5)
    show("after prepend(5):", backward)

    print("\ninsert_after()")
    backward.insert_after(30, 35)
    show("insert_after(30, 35):", backward)
    backward.insert_after(60, 65)
    show("insert_after(60, 65):", backward)

    print("\nqueries and iteration")
    show("contains(35):", backward.contains(35))
    show("contains(999):", backward.contains(999))
    show("is_empty():", backward.is_empty())
    show("len(list):", len(backward))
    show("for value in list:", [value for value in backward])

    print("\nremove() - head, interior node, and tail")
    demo = SinglyLinkedList()
    demo.build_list_forward([1, 2, 3, 4, 5])
    show("start:", demo)
    demo.remove(1)
    show("after remove(1) [head]:", demo)
    demo.remove(3)
    show("after remove(3) [interior]:", demo)
    demo.remove(5)
    show("after remove(5) [tail]:", demo)
    show("length:", len(demo))

    print("\nremove() - the only node in the list")
    solo = SinglyLinkedList()
    solo.append(42)
    show("start:", solo)
    solo.remove(42)
    show("after remove(42):", solo)
    show("is_empty():", solo.is_empty())

    print("\nremove_all() with scattered and consecutive matches")
    duplicates = SinglyLinkedList()
    duplicates.build_list_forward([5, 1, 5, 5, 2, 5])
    show("before:", duplicates)
    removed = duplicates.remove_all(5)
    show("after remove_all(5):", duplicates)
    show("nodes removed:", removed)
    show("remove_all(99) again:", duplicates.remove_all(99))

def demo_error_cases():
    linked = SinglyLinkedList()
    linked.build_list_forward([10, 20, 30])
    show("working list:", linked)

    print("\ninsert_after(12345, 0) - the existing value is not present")
    try:
        linked.insert_after(12345, 0)
    except ValueError as error:
        print(f"  ValueError caught -> {error}")

    print("\nremove(12345) - the value is not present")
    try:
        linked.remove(12345)
    except ValueError as error:
        print(f"  ValueError caught -> {error}")

    print("\ncontains(12345) - a query, so it simply returns False")
    show("contains(12345):", linked.contains(12345))

    print("\nremove_all(12345) - no matches, so it returns 0")
    show("remove_all(12345):", linked.remove_all(12345))

    show("list is still intact:", linked)

def demo_part_two():
    source = SplitEvensOdds()
    source.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8])
    show("source before the split:", source)

    evens, odds = source.split_even_odd()

    print("\nafter split_even_odd()")
    show("even list:", evens)
    show("odd list:", odds)
    show("source list:", source)
    show("even count:", len(evens))
    show("odd count:", len(odds))
    show("source count:", len(source))
    show("even tail.next is None:", evens._tail.next is None)
    show("odd tail.next is None:", odds._tail.next is None)
    show("total nodes in results:", len(evens) + len(odds))

    print("\nsplit edge cases")
    for label, values in (
        ("all even", [2, 4, 6]),
        ("all odd", [1, 3, 5]),
        ("single even value", [8]),
        ("single odd value", [9]),
    ):
        edge = SplitEvensOdds()
        edge.build_list_forward(values)
        edge_evens, edge_odds = edge.split_even_odd()
        print(f"\n  {label}: {values}")
        show("    even list:", edge_evens)
        show("    odd list:", edge_odds)
        show("    source list:", edge)

    print("\nempty source list")
    empty = SplitEvensOdds()
    show("source:", empty)
    try:
        empty.split_even_odd()
    except ValueError as error:
        print(f"  ValueError caught -> {error}")

def demo_node_reuse():
    check = SplitEvensOdds()
    check.build_list_forward([1, 2, 3, 4])
    before = node_ids(check)
    print("\nnode objects before the split (data -> id)")
    for data, identifier in before:
        print(f"  {data} -> {identifier}")

    evens, odds = check.split_even_odd()
    after = node_ids(evens) + node_ids(odds)
    print("\nthe same node objects after the split (data -> id)")
    for data, identifier in after:
        print(f"  {data} -> {identifier}")

    show("ids match exactly:", sorted(i for _, i in before) == sorted(i for _, i in after))
    show("nodes created or lost:", len(after) - len(before))

def demo_inheritance():
    linked = SplitEvensOdds()
    linked.build_list_forward([10, 20, 30])
    show("build_list_forward([10, 20, 30]):", linked)
    linked.append(40)
    show("after append(40):", linked)
    linked.prepend(5)
    show("after prepend(5):", linked)
    linked.insert_after(20, 25)
    show("after insert_after(20, 25):", linked)
    linked.remove(5)
    show("after remove(5):", linked)
    removed = linked.remove_all(25)
    show("after remove_all(25):", linked)
    show("nodes removed:", removed)
    show("contains(30):", linked.contains(30))
    show("len(linked):", len(linked))

    evens, odds = linked.split_even_odd()
    print("\nthe same object can still be split")
    show("even list:", evens)
    show("odd list:", odds)
    show("source after split:", linked)

def main():
    demo_part_one()
    demo_error_cases()
    demo_part_two()
    demo_node_reuse()
    demo_inheritance()

if __name__ == "__main__":
    main()
