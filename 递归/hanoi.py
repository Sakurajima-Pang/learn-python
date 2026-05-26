""" 汉诺塔问题 
汉诺塔问题是一个经典的递归问题，涉及将一组盘子从一个柱子移动到另一个柱子，遵循特定的规则。规则如下：
1. 只能移动一个盘子。
2. 每次移动一个盘子时，必须将其放在另一个柱子上，或者放在一个更大的盘子上。
3. 不能将一个较大的盘子放在一个较小的盘子上。
在这个问题中，我们有三个柱子：源柱子（source）、目标柱子（target）和辅助柱子（auxiliary）。我们需要将所有盘子从源柱子移动到目标柱子，使用辅助柱子作为临时存储。
                            A               C                  B
例如盘子数为3时，
我们来分析这个递归函数的执行过程：
1. 首先，函数调用 hanoi(3, 'A', 'C', 'B')。
2. 由于 n 不等于 1，函数会递归调用 hanoi(2, 'A', 'B', 'C')，将前两个盘子从 A 移到 B。
3. 在 hanoi(2, 'A', 'B', 'C') 中，函数再次递归调用 hanoi(1, 'A', 'C', 'B')，将第一个盘子从 A 移到 C。
4. 接着，函数会打印 "将盘子 1 从 A 移到 C"，并递归调用 hanoi(1, 'B', 'C', 'A')，将第二个盘子从 B 移到 C。
5. 最后，函数会打印 "将盘子 2 从 B 移到 C"，并递归调用 hanoi(1, 'A', 'B', 'C')，将第三个盘子从 A 移到 C。
6. 最后，函数会打印 "将盘子 3 从 A 移到 C"。
通过递归调用，函数能够正确地将所有盘子从源柱子移动到目标柱子，同时遵守规则。每次递归调用都会处理一个更小的子问题，直到达到基本情况（n == 1），此时直接移动盘子并返回。

这个问题的逻辑是，将 n-1 个盘子从源柱子移动到辅助柱子，然后将第 n 个盘子从源柱子移动到目标柱子，最后再将 n-1 个盘子从辅助柱子移动到目标柱子。
这样就能够确保所有盘子按照规则正确地移动到目标柱子上。

不过实际上这样看来很难构造递归函数，比较抽象
"""

# ai生成的代码如下：
def hanoi(n, source, target, auxiliary):
    """汉诺塔问题的递归解法。

    Args:
        n: 盘子的数量。
        source: 源柱名称。
        target: 目标柱名称。
        auxiliary: 辅助柱名称。
    """
    global times
    if n == 1:
        print(f"将盘子 1 从 {source} 移到 {target}")
        times += 1
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"将盘子 {n} 从 {source} 移到 {target}")
    times += 1
    hanoi(n - 1, auxiliary, target, source)


# 下面是我们一步一步的思考，看看到底是怎么写出这个函数的：
def my_hanoi(n, source, target, auxiliary): 
    """汉诺塔问题的递归解法（带注释推导过程）。

    Args:
        n: 盘子的数量。
        source: 源柱名称。
        target: 目标柱名称。
        auxiliary: 辅助柱名称。
    """
    global times

    """
    先假设这个函数就是能够正确地将 n 个盘子从 source 移动到 target 的函数
    那么我们在任何时候调用 my_hanoi(n, source, target, auxiliary) 都会print出正确的移动步骤
    我们实际上并不知道这个函数内部是如何实现的
    但是我们知道n=1时，my_hanoi(1, source, target, auxiliary)显然是可以用print(f"将盘子 1 从 {source} 移到 {target}")来给出正确结果的
    所以我们至少能写出n=1时的实现，即：
    """
    if n == 1:
        print(f"将盘子 1 从 {source} 移到 {target}")
        times += 1
        return


    """
    那么对于n>1的情况，
    如果我们可以将n-1个盘子从source移动到auxiliary，那么我们就可以将第n个盘子从source移动到target
    所以我们写出以下代码：
    """
    my_hanoi(n - 1, source, auxiliary, target) 
    print(f"将盘子 {n} 从 {source} 移到 {target}")
    times += 1


# 最后我们还需要将n-1个盘子从auxiliary移动到target，所以我们写出以下代码：
    my_hanoi(n - 1, auxiliary, target, source) 
# 大功告成！

# 调用测试代码：
times=0
# hanoi(3, 'A', 'C', 'B')
# my_hanoi(3, 'A', 'C', 'B')
# print(f"总共移动了 {times} 次")