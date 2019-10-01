#!/usr/bin/env python3

import sys
import src.cosmos_service as cosmos_service

valid_environments = ['int', 'test', 'stage', 'live'] # add training support here?

# todo - extract this to a menu interaction module - commander link python?
if len(sys.argv) < 3:
    print("Usage:\ncosmos [service] [environment] [instance number (defaults to 0)]")
else:
    service = sys.argv[1]
    environment = sys.argv[2]
    instance = 0
    if len(sys.argv) > 3:
        instance = int(sys.argv[3])
        print(f"instance {instance}")

    if environment not in valid_environments:
        print(f"{environment} is not a valid environment. Valid options are {valid_environments}")
        exit(1)
    cosmos_service.login(service, environment, instance)