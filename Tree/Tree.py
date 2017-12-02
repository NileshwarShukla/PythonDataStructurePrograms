class Tree(object):

     def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

     def insertLeft(self,val):
        if self.left==None:
            self.left=Tree(val)

        else:
            t=Tree(val)
            t.left=self.left
            self.left=t

     def insertRight(self,val):
        if self.right==None:
            self.right=Tree(val)

        else:
            t=Tree(val)
            t.right=self.right
            self.right=t

     def getRoot(self):
        return self.value

     def getRight(self):
         return self.right
     def getLeft(self):
         return self.left

     def setRoot(self,val):
          self.value=val
t=Tree(4)
t.insertLeft(2)
t.insertRight(6)
t.getRight().insertLeft(5)
t.getLeft().insertRight(3)
t.insertLeft(1)
