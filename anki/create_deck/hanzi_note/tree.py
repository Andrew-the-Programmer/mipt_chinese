import random
from pprint import pprint
from typing import Any, Callable

from get_fields.components import get_components
from get_fields.dictionary import chin_dict
from treelib import Tree


def Id():
    if not hasattr(Id, "count"):
        Id.count = 0
    Id.count += 1
    return Id.count


def create_tree(root: Any, func: Callable[[Any], list[Any]]):
    tree = Tree()
    root_id = Id()
    tree.create_node(tag=root, identifier=root_id)

    def recursive(node: Any, parent_id: Any):
        for child in func(node):
            child_id = Id()
            tree.create_node(child, identifier=child_id, parent=parent_id)
            recursive(child, child_id)

    recursive(root, root_id)
    return tree


def main() -> None:

    def chin_dict_func(hanzi):
        try:
            comps = chin_dict.lookup_char(hanzi).components
            return [c.character for c in comps]
        except:
            return []

    def my_func(hanzi):
        return get_components(hanzi)

    hanzi = "焦(点)"

    create_tree(hanzi, chin_dict_func).show()
    create_tree(hanzi, my_func).show()


if __name__ == "__main__":
    main()
