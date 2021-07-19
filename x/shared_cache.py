import json
from multiprocessing.shared_memory import SharedMemory


class SharedCache:
    """In memory cache that is shareable across processes"""

    def __init__(self, name, size):
        self.size = size
        self.name = name
        self.data = {}
        self.memory = self._memory(name, size)
        self._write_memory()

    def get(self, key):
        """Gets item from cache"""
        self._read_memory()
        return self.data.get(key)

    def set(self, key, value):
        """Sets item in cache"""
        self.data[key] = value
        self._write_memory()

    def shutdown(self):
        """Clean up shared memory and shutdown cache"""
        self.memory.close()
        self.memory.unlink()

    def _write_memory(self):
        """Writes data into shared memory buffer"""
        try:
            data = self._data_size().to_bytes(4, "big") + self._data_to_bytes()
            self.memory.buf[:self._data_size()+4] = data
        except ValueError:
            print("data size: ", len(data))
            print("buffer slot size:", self._data_size()+4)

    def _read_memory(self):
        """Reads data from shared memory buffer"""
        data = self.memory.buf.tobytes()
        size = int.from_bytes(data[:4], "big")
        self.data = json.loads(data[4:size+4])

    def _memory(self, name, size):
        """Link to existing shared memory cache or create a new one"""
        try:
            return SharedMemory(name=name)
        except FileNotFoundError:
            return SharedMemory(name=name, size=size, create=True)

    def _data_to_bytes(self):
        """Serialize data"""
        return json.dumps(self.data).encode()

    def _data_size(self):
        return len(self._data_to_bytes())
