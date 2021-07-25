from multiprocessing.shared_memory import ShareableList


class SharedCache:
    """Psuedo "hash table" in memory cache that is shareable across processes"""

    # TODO:
    #  - Handle conflicts
    #  - Improve sizing constraints

    SIZE = 256
    MAX_ITEM_SIZE = 1024*64

    def __init__(self, name):
        self.name = name
        self.memory = self._memory(name)

    def get(self, key):
        """Gets item from cache"""
        index = self._hash(key)
        value = self.memory[index]
        return value.rstrip(b'x\00') or None

    def set(self, key, value):
        """Sets item in cache"""
        index = self._hash(key)
        value_bytes = bytes(value, 'utf-8')
        self.memory[index] = self._padded_bytes(value_bytes)

    def close(self):
        self.memory.shm.close()

    def unlink(self):
        self.memory.shm.unlink()

    def _hash(self, key):
        return hash(key) % self.SIZE

    def _padded_bytes(self, value):
        return value + b'\x00'*(self.MAX_ITEM_SIZE - len(value))

    def _memory(self, name):
        """Link to existing shared memory cache or create a new one"""
        try:
            return ShareableList(name=name)
        except FileNotFoundError:
            # hacky setting of cache size... 256 slots of 64KB each
            sequence = [self._padded_bytes(b'')] * self.SIZE
            return ShareableList(name=name, sequence=sequence)
