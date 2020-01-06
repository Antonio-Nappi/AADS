from b_tree.multiway_search_tree import MultiWaySearchTree


def main():
    tree = MultiWaySearchTree(10, 0)
    print()
    if (tree.is_empty()):
        print('vuoto')
    else:
        print('non vuoto')
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()
    tree.new_element(5, 0)
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    """print(tree.node.print_node())
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()"""
    tree.new_element(3, 0)
    tree.print_tree()
    """print(tree.node.print_node())
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()"""
    tree.new_element(8, 0)
    tree.print_tree()
    """print(tree.node.print_node())
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()"""
    tree.new_element(4, 0)
    tree.print_tree()
    """print(tree.node.print_node())
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()"""
    tree.new_element(13, 0)
    tree.print_tree()
    """print(tree.node.print_node())
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()"""
    tree.new_element(1, 0)
    """print(tree.node.print_node())
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()"""
    tree.new_element(7, 0)
    """print(tree.node.print_node())
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()"""
    tree.new_element(12, 0)
    """print(tree.node.print_node())
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()"""
    tree.new_element(9, 0)
    print("Elemento mediano prima dello split: ", tree.node.get_middle_element(), "Numero elementi: ",
          tree.node.stm.__len__())
    print()
    tree.new_element(11, 0)
    print(tree.node.print_node())
    print("Elemento mediano: ", tree.node.get_middle_element(), "Numero elementi: ", tree.node.stm.__len__())
    print()
    tree.print_tree()

    print()
    print("Prima cancellazione")
    tree.delete_tree_element(3)
    tree.print_tree()

    print()
    print("Seconda cancellazione")
    tree.delete_tree_element(8)
    tree.print_tree()

    print()
    tree.new_element(12, 0)
    tree.new_element(15, 0)
    tree.new_element(18, 0)
    tree.new_element(80, 0)
    tree.new_element(65, 0)
    tree.new_element(22, 0)
    tree.new_element(31, 0)
    tree.new_element(19, 0)
    tree.print_tree()

    print()
    tree.delete_tree_element(19)
    tree.delete_tree_element(80)
    tree.delete_tree_element(65)
    tree.delete_tree_element(22)
    tree.delete_tree_element(31)
    print()
    tree.print_tree()


if __name__ == '__main__':
    main()
