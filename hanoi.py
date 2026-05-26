def hanoi(n, source, target, auxiliary):
    global times
    if n == 1:
        print(f"将盘子 1 从 {source} 移到 {target}")
        times += 1
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"将盘子 {n} 从 {source} 移到 {target}")
    times += 1
    hanoi(n - 1, auxiliary, target, source)
times=0
hanoi(5, 'A', 'C', 'B')
print(f"总共移动了 {times} 次")