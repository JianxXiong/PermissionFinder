# PermissionFinder

### Introduction
    This repository contains a tool used to analyse Android APK file and record its permissions claim.
    **This tool is developed by Jian Xiong as part of his undergraduate design.**

### Usage
    Just open run the command: python tool.py --apk_path=__your file which contains your apks__ --res_path=__the file you want to store your result__
    For example:
                                                                     
        your file which contains your Android APKs                      the file you want to store your result
        │                                                               │ 
        └───A.apk                                                       └───A
        │                                                               │   │───....   
        └───B.apk                                                       │   │───AndroidManifest.xml    
        │                                                               │   │───aoktool.yml    
        └───C.apk                                                       │
                                                                        └───B
                                                                        │   │───...
                                                                        │   │───AndroidManifest.xml
                                                                        │   │───apktool.yml
                                                                        │───...
                                                                        │───...
                                                                        │───result.xlsx
                                                                         
### Requirement                                                            
    Your device must contain the following environment:
        Python >= 3.7
        apktool
        JDK(your JDK version must over 8, 8 is also fine)
    Python package requirement will be given in [requirement.txt](./requirement.txt), just use command pip install -r requirement.txt

