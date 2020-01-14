import hashlib

# '''
# Linked List hash table key/value pair
# '''

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # encodes key to bytes, converts to hexidecimal, converts to int base 16, moudulo by capacity
        hash_ = int(hashlib.sha256(key.encode()).hexdigest(), base=16)
        return hash_


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        key_ = self._hash_mod(key)
        
        if self.storage[key_]:
            original = self.storage[key_]
            self.storage[key_]=LinkedPair(key, value)
            self.storage[key_].next = original

        else:
            self.storage[key_] = LinkedPair(key,value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        key_ = self._hash_mod(key)
        #next_key = self.storage[key_].next

        if self.storage[key_]:
            next_key = self.storage[key_].next
            if self.storage[key_].key == key:
                self.storage[key_].value = None
                #break
            
            else:
                while next_key != None:

                    if next_key.key == key:
                        next_key.value = None
                        break
                    
                    else:
                        next_key = next_key.next


        else:
            print('Key does not exist') # raise keyerr


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        key_ = self._hash_mod(key)
        next_key = self.storage[key_].next

        if self.storage[key_]:
            
            if self.storage[key_].key == key:
                return self.storage[key_].value
            
            else:
                while next_key != None:
                    
                    if next_key.key == key:
                        return next_key.value
                    
                    else:
                        next_key = next_key.next
            
        else:
            return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        new_storage = [None] * self.capacity
        idx = 0
        next_key = self.storage[idx].next 
        
        for ele in self.storage:
            next_key = ele.next
            if ele:
                
                k = self._hash_mod(ele.key)
                
                if new_storage[k]:
                    original = new_storage[k]
                    new_storage[k] = LinkedPair(ele.key, ele.value)
                    new_storage[k].next = original
                
                else:
                    new_storage[k] = LinkedPair(ele.key, ele.value)
                
                while next_key != None:
                    k = self._hash_mod(next_key.key)

                    if new_storage[k]:
                        original = new_storage[k]
                        new_storage[k] = LinkedPair(next_key.key, next_key.value)
                        new_storage[k].next = original

                    else:
                        new_storage[k] = Linked_pair(next_key.key, next_key.value)

                    next_key = next_key.next
        self.storage = new_storage



                     








if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
