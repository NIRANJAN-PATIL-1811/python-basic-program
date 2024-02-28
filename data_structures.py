class Data_struct:
    def data_struct(self, mylist):
        mydict = {}        
        for i in mylist:
            mydict.update({i:len(i)})
        return mydict
list_ = ['neer', 'patil']    

print(Data_struct().data_struct(list_))