# Storage Engine Documentation [![Build Status](https://travis-ci.org/geraldoandradee/storage-manager.svg?branch=master)](https://travis-ci.org/geraldoandradee/storage-manager)

This project is a POC. Not production ready.


# Tests
    
To run the tests:
    
    $ pip install -r requirements/dev.txt
    $ unit2 discover


# Installing 

It's simple:
    
    $ pip install ga-storage-manager



# How it works

In order make `ga_storage_manager` works you must define at least some env vars:

* STORAGE_MANAGER_ENGINE (required): Defines storage manager's engine. `FILESYSTEM` is the only mode supported.