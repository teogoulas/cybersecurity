import argparse
import pandas as pd
from utils.utilities import get_data
import csv


def main():
    # parser = argparse.ArgumentParser(description='dcop')
    # parser.set_defaults(func=classification)
    # parser.add_argument("generate_raw_data", type=str, help="Generate Datasets")

    # args = parser.parse_args()
    # if hasattr(args, 'func'):
    #     args.func(args)
    # raw_data_set = pd.read_csv(r'data/data.csv')
    # print(raw_data_set.shape)
    with open(r'data/file.binetflow') as f:
        reader = csv.DictReader(f)
        for flow in reader:
            if flow['Dir'] == '':
                continue
            elif flow['Label'] != '':
                print(flow['Label'])


if __name__ == '__main__':
    main()
