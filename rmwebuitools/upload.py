#!/usr/bin/env python3
'''
Upload - Upload either PDFs or ePubs to your remarkable.
'''

from . import api 
import os

from sys import stderr

def upload_to_rm(target_folder, file_name):
    with open(file_name, 'rb') as file:
        try:
            api.changeDirectory(target_folder)
            file_name, file_extension = os.path.splitext(file.name)
            if file_extension.lower() not in [".pdf", ".epub"]:
                print('Only PDFs and ePubs are supported. Skipping {}'.format(file.name)) 
            print('Uploading {} to {}'.format(file.name, target_folder))
            api.upload(file)
            print('Successfully uploaded {} to {}'.format(file.name, target_folder))
        except KeyboardInterrupt:
            print('Cancelled.')
            exit(0)
        except Exception as ex:
            print('ERROR: %s' % ex, file=stderr)
            print(file=stderr)
            print('Please make sure your reMarkable is connected to this PC and you have enabled the USB Webinterface in "Settings -> Storage".', file=stderr)
            exit(1)
        finally:
            for file in file:
                file.close()