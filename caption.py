import re

a=open('paper3.tex')
a=a.readlines()
outfile=open('paper3a.tex','w')

for line in a:
  if "\caption{" in line and line[0]!='%': #check for \caption{ tag and that the line is not commented out
    try: #check for incomplete latex syntax, if it occurs, pass, as it's probably commented out anyways
      text=re.findall(r'{.*}', line)[0][1:-1] #the 1:-1 gets rid of the curly braces done by regex
    except:
      print 'error, moving on'
    first_sentence=text.split('. ')[0] + '.' #search by '. ' and get the first instance before it. add period to complete sentnce
    caption_command='['+first_sentence+']'
    print caption_command
    insert_index=8 #this is where \caption{ ends, write the new substring after this
    newline=line[:insert_index]+caption_command+line[insert_index:]
    print newline
    outfile.write(newline)
  else:
    outfile.write(line)
outfile.close()    
    
    
    
