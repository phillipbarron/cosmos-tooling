#!/usr/bin/env python3

import sys
import src.cosmos_service as cosmos_service

valid_environments = ['int', 'test', 'stage', 'live']

if len(sys.argv) < 3:
    # todo - finesse this
    print("Usage:\ncosmos [service] [environment] [instance number (defaults to 0)]")
else:
    # todo - extract this to a menu interaction module
    service = sys.argv[1]
    environment = sys.argv[2]
    instance = None;
    if len(sys.argv) > 3:
        instance = sys.argv[3]
    if environment not in valid_environments:
        print(f"{environment} is not a valid environment. Valid options are {valid_environments}")
        exit(1)
    instance = None
    cosmos_service.login(service, environment, instance)