import sys
import argparse
import xml.sax
import utils

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--apk_path", type=str, default=None)
    parser.add_argument("--res_path", type=str, default=None)
    args = parser.parse_args()
    if (args.apk_path == None or args.res_path == None or args.apk_path == "" or args.res_path == ""):
        print("Path cannot be empty!!!")
        sys.exit()
    
    utils.batch_unpack(args.apk_path, args.res_path)

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = utils.UsePermissionHandler()
    parser.setContentHandler(Handler)
    
    permissions = utils.get_permissions(parser, Handler, args.res_path)
    utils.write_permissions(permissions, args.res_path)