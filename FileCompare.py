#open directory


#for each file in directory, compare to all other files 
#Print output to console  #in 
#future feature to print to DB table for faster comparison when collection gets big
import filecmp
import os
import datetime
import time
import shutil

#f1= "Z:/Noodle/Noodle/test/test1.jpg"
#f2= "Z:/Noodle/Noodle/test/test2.jpg"


#result = filecmp.cmp(f1,f2)
#print (result)




#abosolute path where you would like the folder names transformed to upper case
dir_path = r'Z:/Noodle/Noodle/meatball'
current_date = datetime.date.today()
Start_time = time.ctime(time.time())
Start_time_calc= time.time()
files_processed = 0
duplicate_files = 0
duplicate= []
orig = []

f=open("Z:/Noodle/Noodle/logs/TestLog_"+ str({}).format(current_date)  +".txt","a")
f.write("\nStart time:" +str({}).format(Start_time))

#print(os.listdir(dir_path))

try:
    for path in os.listdir(dir_path):
        file1=os.path.join(dir_path,path)
    # print(r'This is the outer file ' + file1)
        orig.append(file1)
        files_processed = files_processed + 1

        for path in os.listdir(dir_path): 
            file2=os.path.join(dir_path,path)
            #print (orig)
            if file2 not in orig:
        # print(r'This is the internal file '+ file2)
                print(r'I am comparing ' +file1+ r' and ' +file2)
                result = filecmp.cmp(file1,file2)
                if result == True and file1 != file2 :
                    duplicate_files = duplicate_files + 1
                    duplicate.append(file2)
                    f.write("\n"+file2)
                    #f.write("\n Result of "+ file1 + " and " + file2 + ' result= ')
                    #f.write(str({}).format(result))
                    #shutil.move(file2,"z:/Noodle/Noodle/Duplicate")              
except FileNotFoundError:
    pass

try:
    for dup in duplicate:
        f.write("\n "+ dup + " moved")
        shutil.move(dup,"z:/Noodle/Noodle/Duplicate")
except FileExistsError:
    pass

end_time = time.ctime(time.time())
end_time_calc = time.time()
f.write("\nEnd time:" +str({}).format(end_time))
run_time =(end_time_calc -Start_time_calc) *10**3
f.write("\nRun time ="+str({}).format(run_time) +"ms")
f.write("\nFiles Processed ="+str({}).format(files_processed))
f.write("\nDuplicate Files ="+str({}).format(duplicate_files))
        
        
