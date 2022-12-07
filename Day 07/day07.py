def main(lines):
    tree = parse_commands(lines)
    dirs = tree.list_dirs()

    # Part 1
    small_dirs = list(filter(lambda s: (s[1] <= 100000), dirs))
    print(f"Part 1 files <100k: {small_dirs}")
    small_dirs_value = sum([x for (_, x) in small_dirs])
    print(f"Part 1 files <100k sum: {small_dirs_value}")

    # Part 2
    tree_size = tree.size
    free_size = 70000000 - tree_size
    freeup_size = 30000000 - free_size

    size_dirs = sorted(filter(lambda s: (s[1] >= freeup_size), dirs), key=lambda s: s[1])
    print(f"Part 2 to delete: {size_dirs[0]}")


def parse_commands(lines):

    root = Tree(None, "/", is_dir=True)
    current = root

    for line in lines:
        match line.split():
            case ["$", "cd", ".."]:
                current = current.parent
            case ["$", "cd", "/"]:
                current = current.get_root()
            case ["$", "cd", to]:
                current = current.get_dir(to)
            case ["$", "ls"]:
                pass
            case ["dir", name]:
                current.add_child(Tree(parent=current, name=name, is_dir=True))
            # file
            case [size, name]:
                current.add_child(Tree(parent=current, name=name, size=int(size), is_dir=False))

    root = current.get_root()
    root.calc_sizes()
    return root


class Tree(object):
    def __init__(self, parent, name, is_dir, size=0):
        self.parent = parent
        self.name = name
        self.size = size
        self.is_dir = is_dir
        self.children = []

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def get_dir(self, d):
        if self.name == d:
            return self

        for child in self.children:
            if child.name == d:
                return child

    def get_root(self):
        return self if self.parent is None else self.parent.get_root()

    def calc_sizes(self):
        if self.is_dir:
            res = 0
            for c in self.children:
                res += c.calc_sizes()
            self.size = res
            return res
        else:
            return self.size

    def list_dirs(self):
        dirs = []
        if not self.is_dir:
            return None
        elif self.name == "/":
            dirs += [(self.name, self.size)]

        for c in self.children:
            if not c:
                continue

            elif c.is_dir:
                dirs += [(c.name, c.size)]
                res = c.list_dirs()
                if res:
                    dirs += res

        return dirs


file = open("input")
#file = open("test_input")
main(file.read().splitlines())
