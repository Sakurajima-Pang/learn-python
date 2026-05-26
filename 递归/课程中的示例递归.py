"""
前者先打印再下潜
后者先下潜再打印
本质上只是打印的时机不同
"""

def welcome_print_first(n):
    print(f'你好呀{n}')
    if n>1:
        welcome_print_first(n-1)
welcome_print_first(5)

def welcome_print_later(n):
    print(f'你好呀{n}')
    if n>1:
        welcome_print_later(n-1)
welcome_print_later(5)

