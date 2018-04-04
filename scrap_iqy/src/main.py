import sys
import argparse
import scrap

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Enter a search text")


if __name__ == '__main__':
	args = parser.parse_args()
	scrap.start_scrap(args.name)
