import os
import unittest2

from storage_manager import StorageManager, StorageManagerEngineException, StorageManagerDataException


class TestStorageManager(unittest2.TestCase):

    def setUp(self):
        self.storage_manager_engine = "FILESYSTEM"
        self.storage_manager_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "db.json")

    def test_basic_variables(self):
        self.assertIn(self.storage_manager_engine, ["FILESYSTEM"], msg="You must define STORAGE_MANAGER_ENGINE "
                                                                       "environment variable")

    def test_init_storage_manager(self):
        with self.assertRaises(StorageManagerEngineException):
            StorageManager()

        with self.assertRaises(StorageManagerEngineException):
            StorageManager(storage_manager_engine=StorageManager.STORAGE_MANAGER_ENGINE_MODE_FILESYSTEM)

    def test_storage_manager_get(self):
        instance = StorageManager(storage_manager_engine=self.storage_manager_engine,
                                  storage_manager_file_path=self.storage_manager_file_path)

        self.assertTrue("get" in dir(instance), msg="Storage manager must have read method")
        data = instance.get(9999)
        self.assertEqual(data, None, msg="If data does not exists it must return None")

    def test_storage_manager_save(self):
        instance = StorageManager(storage_manager_engine=self.storage_manager_engine,
                                  storage_manager_file_path=self.storage_manager_file_path)

        self.assertTrue("save" in dir(instance), msg="Storage manager must have save method")

        with self.assertRaises(StorageManagerDataException):
            instance.save()

        with self.assertRaises(StorageManagerDataException):
            instance.save({})

        with self.assertRaises(StorageManagerDataException):
            instance.save("sfsdfsdfsdff")

        instance.save({"id": 1, "title": "Go python go!"})

        class Test(object):
            pass

        t = Test()
        t.title = "Go python go!"
        t.id = 2

        # instance.save(t, Test)
