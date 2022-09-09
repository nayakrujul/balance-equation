import argparse
from balance.balance import force_solve, process
from balance.balance import interface as _interface

def interface():
    parser = argparse.ArgumentParser(prog ='balance',
                                     description ='Balance a chemical reaction equation!')
    parser.add_argument('left', metavar ='left', type=str, nargs=1, help= 'The left side of the equation')
    parser.add_argument('right', metavar ='right', type=str, nargs=1, help= 'The right side of the equation')
    args = parser.parse_args()
    ls, rs = args.left[0].replace(' ', '').split('+'), args.right[0].replace(' ', '').split('+')
    sol = force_solve([process(x) for x in ls], [process(y) for y in rs])
    if not sol:
        print("Couldn't brute-force this.")
        return 1
    print("Multipliers:", *sol)
    print("Equation:", _interface(args.left[0], args.right[0]))
