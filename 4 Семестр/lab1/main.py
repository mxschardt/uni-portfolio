def gen_bin_tree(height=5,
                 root=10,
                 left=lambda r: r * 3 + 1,
                 right=lambda r: r * 3 - 1):
  """Создание бинарного дерева"""
  # Дерево хранится в памяти как массив значений.
  tree = [0 for _ in range(2**(height + 1) - 1)]
  tree[0] = root
  for (idx, node) in enumerate(tree):
    l, r = child_nodes(idx)
    if l < len(tree):
      tree[l] = left(node)
    if r < len(tree):
      tree[r] = right(node)

  return tree


def insert(tree, value):
  tree.append(value)


def print_bin_tree(tree, idx=0, level=0):
  """Вывод бинарного дерева"""
  if idx < len(tree):
    l, r = child_nodes(idx)
    print_bin_tree(tree, l, level + 1)
    print(' ' * 4 * level + str(tree[idx]))
    print_bin_tree(tree, r, level + 1)


def child_nodes(i):
  return (2 * i) + 1, (2 * i) + 2


if __name__ == '__main__':
  # 10
  tree = gen_bin_tree()
  print_bin_tree(tree)
