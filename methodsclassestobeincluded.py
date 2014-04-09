#!/usr/local/bin/python2.7
class Key:
  #KeyMajor = [0,2,4,5,7,9,11]
  NoteList = []
  MajorKey = [0,2,4,5,7,9,11]
  NatMinor = [0,2,3,5,7,8,10]
  HarmMinor = [0,2,3,5,7,8,11]
  
  def __init__(self, baseNote, key=MajorKey):
    if len(Key.NoteList) == 0:
      Key.createNoteList()
    self.key = key
    self.base = baseNote

  def getScale(self):
    retL = []
    for i in range(0, len(self.key)):
      retL.append(self.getNoteFromKey(i))
    return retL
  
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
    num = (i + self.key[index])%12
    return Key.NoteList[num]

  def sigFromAccidentals(count, scale="major"):
    signatureList = ['Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'F#',
         'B', 'E', 'A', 'D', 'G']
    
  def matchingScale(self):
    pass #solve eventually
  
'''
majorC = Key('B')
print Key.NoteList
print majorC.getNoteFromKey(2)
print majorC.getScale()
  '''
def generateModValuePair(mylist):
  retList = []
  for val in mylist:
    m = val % 7
    n = val / 7
    retList.append((m,n))
  return retList

def createNoteList(mylist, key):
  retList = []
  for val in mylist:
    retList.append(key.getNoteFromKey(val))
  return retList
  '''
sto = generateValuePair(t)
print sto[0][0]
'''
