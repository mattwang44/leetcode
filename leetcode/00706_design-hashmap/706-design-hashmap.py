class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memo = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for i, (k, v) in enumerate(self.memo):
            if key == k:
                self.memo[i] = (k, value)
                return
        self.memo.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for (k, v) in self.memo:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i, (k, v) in enumerate(self.memo):
            if key == k:
                del self.memo[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
