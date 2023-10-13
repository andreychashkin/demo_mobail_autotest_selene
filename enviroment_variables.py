import os 


device_name = '901c3d02' if os.environ.get('DEVICE_NAME') is None\
    else os.environ.get('DEVICE_NAME')
permissions = True if os.environ.get('PERMISSIONS') is None\
    else False 
