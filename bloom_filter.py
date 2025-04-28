import hashlib

class BloomFilter:

    # Constructor method (dunder method)
    def __init__(self, size=1000, hash_count=3):
        self.size = size                 # Size of the bit array
        self.hash_count = hash_count     # How many hash functions to use
        self.bit_array = [0] * size      # Initialize all bits to 0

    #utility function to generate hash indices
    def _hashes(self, item):
        # Initialize an empty list to store the hash indices
        result = []
        
        # Convert the input item to bytes using UTF-8 encoding 
        item = item.encode('utf-8')
        
        # Generate 'hash_count' number of hash indices
        for i in range(self.hash_count):

            # Create a unique hash by combining the item with the current index (i)
            hash_digest = hashlib.sha256(item + str(i).encode('utf-8')).hexdigest()
            
            # Convert the hexadecimal hash digest to an integer
            hash_int = int(hash_digest, 16)
            
            # Compute the index by taking the modulo of the integer with the size of the bit array
            result.append(hash_int % self.size)
        
        # Return the list of hash indices
        return result


    def add(self, item):
        # Generate the hash indices for the given item
        for index in self._hashes(item):
            # Set the corresponding bits in the bit array to 1
            self.bit_array[index] = 1

    # Check if an item is in the Bloom Filter
    # Allows the use of the 'in' operator (because of the dunder method)
    def __contains__(self, item):

        # Generate the hash indices for the given item
        hash_indices = self._hashes(item)
        
        # Check if all the corresponding bits in the bit array are set to 1
        for index in hash_indices:
            if self.bit_array[index] != 1:
                # If any bit is not set to 1, the item is definitely not in the Bloom Filter
                return False
        
        # If all bits are set to 1, the item might be in the Bloom Filter
        return True
