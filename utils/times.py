#!/usr/bin/env python

import json
import fileinput
import dateutil.parser

for line in fileinput.input():
    tweet = json.loads(line)
    created_at = dateutil.parser.parse(tweet["created_at"])
    print created_at.strftime("%Y-%m-%d %H:%M:%S")


