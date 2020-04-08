class MaxHeap:
    def __init__(self):
        self.heap = []

    def getParent(self, index):
        return int((index-1)/2)
    
    def getLeftChild(self, index):
        return 2*index + 1
    
    def getRightChild(self, index):
        return 2*index + 2
    
    def hasParent(self, index):
        return self.getParent(index) >= 0 
    
    def hasLeftChild(self, index):
        return self.getLeftChild(index) < len(self.heap)

    def hasRightChild(self, index):
        return self.getRightChild(index) < len(self.heap)

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def bubbleUp(self, index):
        size = len(self.heap)
        while self.hasParent(index) and self.heap[index] > self.heap[self.getParent(index)]:
            self.swap(index, self.getParent(index))
            index = self.getParent(index)
    
    def insertKey(self, key):
        self.heap.append(key)
        self.bubbleUp(len(self.heap) - 1)

    def printHeap(self):
        print(self.heap)

    def getMaxValChildIndex(self, index):
        if self.hasLeftChild(index):
            leftChild = self.getLeftChild(index)
            if self.hasRightChild(index):
                rightChild = self.getRightChild(index)
                if self.heap[leftChild] > self.heap[rightChild]:
                    return leftChild
                else :
                    return rightChild
            else:
                return leftChild
        else:
            return -1

    def bubbleDown(self, index):
        while self.hasLeftChild(index):
            maxChildIndex = self.getMaxValChildIndex(index)
            if maxChildIndex == -1:
                break
            if self.heap[index] < self.heap[maxChildIndex]:
                self.swap(index, maxChildIndex)
                index = maxChildIndex
            else:
                break

    def poll(self):
        if len(self.heap) == 0:
            return -1
        lastIndex = len(self.heap) - 1
        self.swap(0, lastIndex)
        former = self.heap.pop()
        self.bubbleDown(0)
        return former

if __name__ == "__main__":

    maxHeap = MaxHeap()

    arr = [45, 99, 63, 27, 29, 57, 42, 35, 12, 24]
    
    for i in arr:
        maxHeap.insertKey(i)
    
    print("Inital Heap")
    maxHeap.printHeap()
    print("Insert key 50")
    maxHeap.printHeap()
    maxHeap.insertKey(50)
    maxHeap.printHeap()
    print("delete root node")
    maxHeap.poll()
    maxHeap.printHeap()    



