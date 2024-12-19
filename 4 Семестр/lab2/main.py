from collections import deque


def gen_bin_tree(height=5,
                 root=10,
                 left=lambda r: r * 3 + 1,
                 right=lambda r: r * 3 - 1):
  queue = deque()
  tree = {'value': root, 'left': None, 'right': None}
  queue.append(tree)

  for _ in range(1, 2**height):
    node = queue.popleft()

    if node['left'] is None:
      node['left'] = {
        'value': left(node['value']),
        'left': None,
        'right': None
      }
      queue.append(node['left'])

    if node['right'] is None:
      node['right'] = {
        'value': right(node['value']),
        'left': None,
        'right': None
      }
      queue.append(node['right'])

  return tree


def print_bin_tree(tree, level=0):
  if tree is not None:
    print_bin_tree(tree['left'], level + 1)
    print(' ' * 4 * level + str(tree['value']))
    print_bin_tree(tree['right'], level + 1)


if __name__ == '__main__':
  # 10
  tree = gen_bin_tree()
  print_bin_tree(tree)
