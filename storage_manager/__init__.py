import os
import inspect
import json

from storage_manager.exceptions import StorageManagerEngineException, StorageManagerDataException


class StorageManagerBase(object):
    STORAGE_MANAGER_ENGINE_DATA_ID = "id"
    STORAGE_MANAGER_ENGINE_MODE_FILESYSTEM = "FILESYSTEM"

    STORAGE_MANAGER_ENGINE_EXCLUDED_KEYS = ['']

    def _read_database(self):
        if not os.path.isfile(self.storage_manager_path):
            return {}

        data = open(self.storage_manager_path, "r")
        result = json.loads(data.read())
        data.close()
        if not result:
            result = {}

        return result

    def _write_data(self, data):
        f = open(self.storage_manager_path, 'w')
        f.write(json.dumps(data))
        f.close()

    def _save_dict(self, data):
        stored = self._read_database()
        stored[data[StorageManagerBase.STORAGE_MANAGER_ENGINE_DATA_ID]] = data

        self._write_data(stored)

    def _save_obj(self, data):
        self._save_dict(self.dict_from_class(data))

    def dict_from_class(self, klass):
        return dict((key, value) for (key, value) in klass.__dict__.items() if key not in
                    self.STORAGE_MANAGER_ENGINE_EXCLUDED_KEYS)


class StorageManager(StorageManagerBase):

    def __init__(self, storage_manager_engine=None, storage_manager_file_path=None):
        self.storage_manager_engine = storage_manager_engine or os.environ.get("STORAGE_MANAGER_ENGINE")
        self.storage_manager_path = storage_manager_file_path or os.environ.get("STORAGE_MANAGER_FILE_PATH")

        if not self.storage_manager_engine:
            raise StorageManagerEngineException("You must define STORAGE_MANAGER_ENGINE")

        if self.storage_manager_engine == self.STORAGE_MANAGER_ENGINE_MODE_FILESYSTEM and not self.storage_manager_path:
            raise StorageManagerEngineException("You must define STORAGE_MANAGER_FILE_PATH")

    def save(self, data=None, klass_type=None):
        if not data:
            raise StorageManagerDataException("Cannot save. You must provide data.")

        if isinstance(data, dict):
            return self._save_dict(data)
        elif inspect.isclass(data):
            return self._save_obj(data)

        raise StorageManagerDataException("Data type is not supported. Only dict and object is supported.")

    def list(self, klass_reference=None):
        pass

    def get(self, id, klass_reference=None):
        pass
