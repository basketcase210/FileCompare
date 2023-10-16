#open directory


#for each file in directory, compare to all other files 
#Print output to console  #in 
#future feature to print to DB table for faster comparison when collection gets big
import filecmp


f1= "Z:/Noodle/Noodle/test/test1.jpg"
f2= "Z:/Noodle/Noodle/test/test2.jpg"


result = filecmp.cmp(f1,f2)
print (result)