class node:
    def __init__(self,info):
        self.__data = info
        self.__next = None
    def get_data(self):              #getter method
        return self.__data 
    def set_data(self,info):         #setter math
        self.__data = info
    def get_next(self):              #getter method
        return self.__next
    def set_next(self,next_node):    #setter method 
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
    def get_head(self):
        return self.__head
    def set_head(self,node):
        self.__head = None
    def get_tail(self):
        self.__tail = node 
    def ll_append(self,info):
        #if the linked list does not pre exist then create a new 
         # otherwise append a new node at the end of the linked list
        new_node = node(info)
        if (self.get_head() is None):
            new_node.set_next(None)
            self.set_head(new_node)
            self.set_tail(new_node)
            print ("Creating a linked list with a new node...")
        else :
            self.get_tail().set_next(new_node)
            self.set_tail()(new_node)
            print("Appending the new node at the end of the linked list...")
        def ll_desplay(self):
            ptr = self.get_jead()
            if(ptr == None):
                print("Linked list is not pre - existing")
                while (ptr is not None):
                    print (f"Info = {ptr.get_data()} and link = {ptr.get_next()}...")
                    ptr = ptr.get_next()
                print  ("End of the display operation...")
        def __str__(self):
            ptr = self.get_head()
        all_info = []
        while (ptr is not None):
            all_info.append(str(ptr.get_data()))
            ptr = ptr.get_next()
        message = ", ".join(all_info)
        return "Linked list from Head to Tail: " + message
    def ll_insert(self, data_new, data_before):
        ptr = self.get_head()
        while (ptr is not None):
            if (ptr.get_data() == data_before):
                break
            ptr = ptr.get_next()
        if (ptr is None):
            print (f"Unsuccessful searching for info {data_before}...")
        else:
            new_node = Node(data_new)
            new_node.set_next(ptr.get_next())  # new_node->next = ptr->next
            ptr.set_next(new_node)   # ptr->next = new_node
            if (ptr == self.get_tail()):   # if (ptr == tail):
                self.set_tail(new_node)   # tail = new_node
    def ll_delete(self, data_old):
        ptr = self.get_head()
        if (ptr == None):
            print ("U N D E R F L O W !!!")
            return
        if (ptr.get_data() == data_old):
            self.set_head(ptr.get_next())
            del(ptr)
            print ("Deleting the Header Node...")
            return
        ptr_next = ptr.get_next()
        while (ptr_next != None and ptr_next.get_data() != data_old):
            ptr = ptr.get_next()  # ptr = ptr_next
            ptr_next = ptr_next.get_next() # ptr_next->next
        if (ptr_next != None and ptr_next.get_data() == data_old):
            ptr.set_next(ptr_next.get_next())
            del ptr_next
            print ("Successful Deletion...")
        else:
            print ("Unsuccessful Deletion...")
    def ll_search(self, data_search):
        ptr = self.get_head()
        while (ptr != None):
            if (ptr.get_data() == data_search):
                break
            ptr = ptr.get_next()
        if (ptr == None):
            print ("Unsuccessful searching...")
        else:
            print ("Successful searching")
data_list = [33, 22, 11, 77, 55, 44, 66]
link_list = LinkedList()
for info in data_list:
    link_list.ll_append(info)
link_list.ll_display()
print (link_list)
link_list.ll_insert(88, 77)
print (link_list)
link_list.ll_insert(99, 1000)
print (link_list)
link_list.ll_delete(77)
print (link_list)
link_list.ll_delete(7000)
print (link_list)
link_list.ll_search(1000)
link_list.ll_search(88)           
        