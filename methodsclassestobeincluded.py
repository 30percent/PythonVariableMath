#!/usr/local/bin/python2.7
    
print "Hello World!\n";

t = [0,10,22,48]
# A, A#, B, C, C#, D, D#, E, F, F#, G, G#

majorKey = [0,2,4,5,7,9,11]

class Key:
  #KeyMajor = [0,2,4,5,7,9,11]
  NoteList = []
  
  def __init__(self, baseNote, keylist):
    if len(Key.NoteList) == 0:
      Key.createNoteList()
    self.key = keylist
    self.base = baseNote
  
  @staticmethod
  def createNoteList():
    retList = Key.NoteList
    val = 0
    it = 0
    while(val < 12):
      key = chr(ord('A') + ((it+2)%7))
      it += 1
      retList.append(key)
      val += 1
      if(key != 'E' and key != 'B'):
        retList.append(key+'#')
        val += 1
    return retList
    
  def getNoteFromKey(self, index):
    i = Key.NoteList.index(self.base)
    num = (i + self.key[index])%11
    return Key.NoteList[num]
  

majorC = Key('C', [0,2,4,5,7,9,11])
print majorC.getNoteFromKey(2)
  
def generateValuePair(mylist):
  retList = []
  for val in mylist:
    m = val % 8
    n = val / 8
    tup = (m,n)
    retList.append(tup)
  return retList
  
print generateValuePair(t)
