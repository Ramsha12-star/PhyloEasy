import os
class convert_format:
    def change_format(path, name):
        file_name="../../"+path
        print(os.listdir(file_name))

        file = open(file_name+"/"+name)
        lines=file.readlines()
        new_file=open(file_name+"/new.csv","w")
        for l in lines:
            print(l)
            new_file.write(l.replace("\t",","))
        file.close()
        new_file.close()


        
obj=convert_format
obj.change_format("79","Distance Matrix.csv")