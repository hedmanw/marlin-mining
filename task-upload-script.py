#!/usr/bin/env python

import sys
import requests
import os

url = "http://web.student.chalmers.se/~hedmanw/bananas.php"


class Uploader:
    def __init__(self, identifier):
        self.identifier = identifier
        self.files = [
            ".MPS34/system/log/idea.log",
            "results/incline.c",
            "rcpttWorkspace/experiment/recording.test",
            "results/eclipse.c"
        ]
        self.statuses = {}

    def go(self):
        def home_path(file_path):
            home = os.path.expanduser('~')
            return os.path.join(home, file_path)

        for file_path in self.files:
            self.post_payload(home_path(file_path))

        print "----------------------------"
        print "Summary of {} files:".format(len(self.files))
        for key, value in self.statuses.iteritems():
            print "{}: {}".format(os.path.basename(key), value)
        print "----------------------------"


    def post_payload(self, file_path):
        errors = None
        if os.path.exists(file_path):
            with open(file_path, 'rb') as payload:
                r = requests.post(url, files={'payload': payload}, data={'id': self.identifier})
                if "Failed with errors" in r.text:
                    errors = r.text
                else:
                    print "Successfully uploaded {}".format(file_path)
                    self.statuses[file_path] = "Succeeded."
        else:
            errors = "File not found at {}".format(file_path)

        if errors:
            self.statuses[file_path] = "Failed: {}".format(errors)
            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            print "@@ UPLOAD FAILED FOR {}".format(file_path)
            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            print "Reason: {}".format(errors)

if __name__ == '__main__':
    name = sys.argv[1]
    uploader = Uploader(name)
    uploader.go()