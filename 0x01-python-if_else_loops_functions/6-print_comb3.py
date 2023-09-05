#!/usr/bin/python3
for outer_loop in range(10):
    for inner_loop in range(10):
        if (outer_loop != inner_loop and outer_loop < inner_loop) \
                and outer_loop < 9:
            if (outer_loop == 8 and inner_loop == 9):
                print('{0}{1}'.format(outer_loop, inner_loop))
            else:
                print('{0}{1}, '.format(outer_loop, inner_loop), end='')
