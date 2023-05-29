from pathlib import Path


tree_str = ''

def generate_tree(pathname, n=0):
    global tree_str
    if pathname.is_file():
        tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'
    elif pathname.is_dir():
        tree_str += '    |' * n + '-' * 4 + \
            str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)


if __name__ == '__main__':
    # 命令参数个数为2并且目录存在存在
    if len(sys.argv) == 2 and Path(sys.argv[1]).exists():
        generate_tree(Path(sys.argv[1]), 0)
    else: # 当前路径
        generate_tree(Path.cwd(), 0)
    print(tree_str)