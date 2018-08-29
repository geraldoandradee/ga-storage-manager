# Storage Engine Documentation [![Build Status](https://travis-ci.org/geraldoandradee/ga-storage-manager.svg?branch=master)](https://travis-ci.org/geraldoandradee/ga-storage-manager)

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


# How to use

    # -*- coding: utf-8 -*-
    import os
    
    from ga_storage_manager import StorageManager
    
    db = StorageManager(storage_manager_engine=StorageManager.STORAGE_MANAGER_ENGINE_MODE_FILESYSTEM,
                        storage_manager_file_path=os.getenv('DATABASE_PATH',
                                                            os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                         os.getenv('DATABASE_NAME', "db.json"))))
                                                                         
    db.save({"id": 34, "message": "You shall not pass!"})     
    db.get(34)     # gets the data
    db.list()      # returns all data
    db.delete(34)  # deletes the data                                                             