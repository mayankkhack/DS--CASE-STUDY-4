
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in str(key)) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for item in bucket:
            if item[0] == key:
                item[1] = value
                return

        bucket.append([key, value])

    def search(self, key):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                return item[1]

        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for item in bucket:
            if item[0] == key:
                bucket.remove(item)
                return True

        return False

    def display(self):
        for index, bucket in enumerate(self.table):
            print(index, ":", bucket)


def main():
    dictionary = HashTable()

    dictionary.insert("name", "Mayank")
    dictionary.insert("course", "Computer Engineering")
    dictionary.insert("city", "Pune")

    print("Name:", dictionary.search("name"))
    print("Course:", dictionary.search("course"))

    print("Delete city:", dictionary.delete("city"))
    print("City:", dictionary.search("city"))

    print("\nHash Table:")
    dictionary.display()


if __name__ == "__main__":
    main()
