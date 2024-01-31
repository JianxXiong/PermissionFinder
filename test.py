import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str, default=None)
args = parser.parse_args()

for file in os.listdir(args.path):

    print(os.path.join(args.path, file))