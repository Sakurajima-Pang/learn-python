def welcome_print_first(n: int) -> None:
    """先打印再递归下潜，展示递归的"递"过程。

    在递归调用之前执行打印操作，因此输出顺序为 n, n-1, ..., 1。

    Args:
        n: 起始数字，函数会从 n 递减打印到 1。
    """
    print(f'你好呀{n}')
    if n > 1:
        welcome_print_first(n - 1)


def welcome_print_later(n: int) -> None:
    """先递归下潜再打印，展示递归的"归"过程。

    在递归调用之后执行打印操作，因此先下潜到底再逐层返回打印，输出顺序为 1, 2, ..., n。

    Args:
        n: 起始数字，函数会先下潜到底再从 1 递增打印到 n。
    """
    print(f'你好呀{n}')
    if n > 1:
        welcome_print_later(n - 1)

