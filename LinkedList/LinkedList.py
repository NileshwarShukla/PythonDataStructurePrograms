class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
        
    def cycle_check(node):
        marker1=node
        marker2=node

        while marker2 !=None and marker2.next!=None:
            marker1=marker1.next
            marker2=marker1.next.next

            if marker2==marker1:
                return True
        return False

    def n_LastNode(self,n):
        left=self
        right=self

        for i in xrange(n-1):
            if not right.next:
               print '0'
               return
            right=right.next

        while right.next:
            left=left.next
            right=right.next
            
        return left.value


a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
print a.n_LastNode(2)


