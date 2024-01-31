import os
import sys
import argparse
from tqdm import tqdm

def batch_unpack(apk_path, res_path):
    if os.path.exists(res_path) == False:
        os.makedirs(res_path)
    files = os.listdir(apk_path)
    t_files = tqdm(files)
    for file in t_files:
        fileName = file[0: -4]
        cmd = os.path.join(os.path.abspath(r".."), "apktool.jar") + " d " + os.path.join(apk_path, file) + " -o " +  os.path.join(res_path, fileName)
        os.system(cmd)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--apk_path", type=str, default=None)
    parser.add_argument("--res_path", type=str, default=None)
    args = parser.parse_args()
    if (args.apk_path == None or args.res_path == None or args.apk_path == "" or args.res_path == ""):
        print("Path cannot be empty!!!")
        sys.exit()
    batch_unpack(args.apk_path, args.res_path)