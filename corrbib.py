import os
import sys

#the goal of this is to append an extra set of curly brackets in front of title to preserve capitalization in bibtex
#want this to apply only to first and last {,} in the line (others may be there due to special characters)

#function to find all indices of a character in a string (probably could be done better with regex)
def getcharindices(string,match_character):
  indices=[]
  for i,character in enumerate(string):
    if character==match_character:
      indices.append(i)
  return indices

args=sys.argv
if len(args)!=3:
  print 'You either have too many or too few arguments. The function takes 2 arguments: infile and outfile.'
  sys.exit()

infile=str(args[1])
outfile=str(args[2])
f_in=open(infile).readlines()
f_out=open(outfile,'w')

#see if line has title in it, and make sure it doesn't have two brackets already
for line in f_in:
  if 'title=' in line:
    if 'title={{' not in line:
      #split string into 3 parts, one before first apperanace of {, one after last appearance of } and one in middle.
      #put middle part in brackets to get {{titletext}}
      first_char=getcharindices(line,'{')[0]
      last_char=getcharindices(line,'}')[-1]
      part1=line[:first_char]
      part2=line[first_char:last_char]
      part3=line[last_char:]
      newline=part1+'{'+part2+'}'+part3
      f_out.write(newline)
  else:
    f_out.write(line)
      
