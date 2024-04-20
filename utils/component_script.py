import os
import xml.sax
import pandas as pd
from tqdm import tqdm

class ComponentHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.component = {"activity": 0, "service": 0, "receiver": 0, "provider": 0}

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag in ["activity", "service", "receiver", "provider"]:
            self.component[tag] = self.component[tag] + 1
    
    def endElement(self, tag):
        self.CurrentData = ""

    def characters(self, content):
        None

def component_statistics(parser, Handler, res_path):
    
    components = []
    files = os.listdir(res_path)
    t_files = tqdm(files)
    for file in t_files:
        first_path = os.path.join(res_path, file)
        if os.path.isdir(first_path):
            for f in os.listdir(first_path):
                second_path = os.path.join(first_path, f)
                if os.path.isfile(second_path) and f == "AndroidManifest.xml":
                    cur_component = []
                    cur_component.append(file)
                    parser.parse(second_path)
                    cur_component.append(Handler.component)
                    Handler.component = {"activity": 0, "service": 0, "receiver": 0, "provider": 0}
                    components.append(cur_component)
    return components

def write_components(components, res_path):

    excel_path = os.path.join(res_path, "components.xlsx")
    result = pd.DataFrame(components, columns=["APP", "Details"])
    result = result.join(result["Details"].apply(pd.Series))
    result.drop("Details", axis=1, inplace=True)
    result.to_excel(excel_path)
    print("*********解析完成*********")