# Case Study 4: Dictionary Using a Hash Table

## Unit IV: Hashing

**Subject:** Data Structures and Algorithms  
**Language:** Python 3

## Aim
To implement a dictionary using a hash table for efficient key-value storage and retrieval.

## Objectives
- Understand hash functions.
- Insert and search key-value pairs.
- Delete entries from the hash table.
- Handle collisions using separate chaining.

## Theory
A hash table stores data using keys and values. A hash function converts a key into an array index.

A collision occurs when multiple keys map to the same index. This implementation handles collisions using separate chaining, where each index stores a list of entries.

## Operations
- Insert or update a key-value pair.
- Search for a key.
- Delete a key.
- Display the hash table.

## Sample Output

```text
Name: Mayank
Course: Computer Engineering
Delete city: True
City: None
```

The program also displays the hash table buckets.

## Complexity
- Average insertion, search, and deletion: `O(1)`
- Worst-case insertion, search, and deletion: `O(n)`
- Space complexity: `O(n + m)`, where `n` is the number of entries and `m` is the table size.

## Applications
- Dictionaries and symbol tables.
- Caching.
- Database indexing concepts.
- Fast key-value lookup.

## How to Run
```bash
python main.py
```

## Conclusion
A hash table provides efficient key-value operations. Separate chaining handles collisions by storing multiple entries in the same bucket.
