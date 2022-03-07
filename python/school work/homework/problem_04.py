class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return f"({self.data})"


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.length = 0

    def empty(self):
        return self.head is None

    def append(self, node: Node):
        if self.head is None:
            # We don't have leading element yet
            self.head = node
        else:
            self.get(self.length - 1).next = node

        self.length += 1

    def insert(self, node: Node, p: int):
        if p == 0:
            node.next = self.head
            self.head = node
            return

        prev = self.get(p - 1)
        node.next = prev.next
        prev.next = node
        self.length += 1

    def delete(self, p: int):
        if p == 0:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head

        prev = self.get(p - 1)
        to_remove = prev.next
        prev.next = to_remove.next
        to_remove.next = None

    def get(self, p: int) -> Node:
        current = self.head

        for _ in range(p):
            current = current.next

        return current

    def is_incremental(self):
        if self.empty():
            return True
        current = self.head
        while current.next is not None:
            if current.__gt__(current.next) :
                return False
            current = current.next
            
        
        return True
    
    def is_gradually_incremental(self):
        if self.empty():
            return True
        current = self.head
        while current.next is not None:
            if current.data >= current.next.data:
                return False
            current = current.next
            
        
        return True

    def remove_dups(self):
        if self.empty() or not self.is_gradually_incremental():
            return

        cur = self.head

        while cur.next != None:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next

    def mirror(self, temp):
      
        if temp:
            self.mirror(temp.next)
            print( f"({temp.data})", end = ' -> ')
        else:
            return



    def __str__(self):
        res = ""
        current = self.head
        while current is not None:
            res += f"{current} -> "
            current = current.next

        return res

if __name__ == '__main__':
    s = LinkedList()
    s.append(Node(10))
    s.append(Node(20))
    s.append(Node(30))
    s.append(Node(40))
    s.is_incremental()