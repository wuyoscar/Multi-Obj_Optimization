import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f','--foo', help='foo help')
parser.add_argument('-s','--ss', type = str,nargs= '+',help='foo help')

args = parser.parse_args()
if args.ss is None:
    print('this is no input')


print(args.foo + "a")