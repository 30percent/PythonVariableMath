#!/usr/local/bin/python2.7
from collections import deque

class Key:
  #KeyMajor = [0,2,4,5,7,9,11]
  NoteList = createNoteList()
  MajorKey = [0,2,4,5,7,9,11]
  NatMinor = [0,2,3,5,7,8,10]
  HarmMinor = [0,2,3,5,7,8,11]
  
  def __init__(self, baseNote, key=MajorKey):
    if len(Key.NoteList) == 0:
      Key.createNoteList()
    self.key = key
    self.base = baseNote

  '''
    @return: list of "Notes" in order that fall within instance key
  '''
  def getScale(self):
    retL = []
    for i in range(0, len(self.key)):
      retL.append(self.getNoteFromKey(i))
    return retL
  
  '''
    @return: list of ordered "Notes" that correspond to western structure
  '''
  @staticmethod
  def createNoteList():
    retList = []
    val = 0
    it = 0
    while(val < 12):
      note = chr(ord('A') + ((it+2)%7))
      it += 1
      retList.append(note)
      val += 1
      if(note != 'E' and note != 'B'):
        retList.append(note+'#')
        val += 1
    return retList
  
  '''
    @param: "index" - index of desired note within instance key list
    @return: (String) "Note" based on key and base note
  '''
  def getNoteFromKey(self, index):
    i = Key.NoteList.index(self.base)
    num = (i + self.key[index])%12
    return Key.NoteList[num]

  def sigFromAccidentals(count, scale="major"):
    signatureList = ['Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'F#',
         'B', 'E', 'A', 'D', 'G']
    
  def matchingScale(self):
    pass #solve eventually

#1,2,3,4,6,8 (eigth note increments)
#mod6 decides duration,
def matchToSum(mylist, mCount):
  initDeq = deque(mylist)
  finalDeq = deque()
  sum1 = 0
  while len(initDeq) > 0:
    temp = sum1+initDeq[0]
    if(temp > mCount):
      if((mCount-sum1) < (temp)):
        t = finalDeq.pop()
        t += mCount-sum1
        finalDeq.append(t)
        sum1 = 0
      else:
        t = initDeq.popleft()
        t -= temp-mCount
        finalDeq.append(t)
        sum1 = 0
    else:
      t = initDeq.popleft()
      sum1 += t
      finalDeq.append(t)
  return finalDeq
  
def listToNoteDuration(mylist):
  diction = {0:.125,1:.25,2:.325,3:.5,4:.75,5:1}
  #diction = {0:1,1:2,2:3,3:4,4:6,5:8}
  decList = []
  for val in mylist:
    decList.append(diction[(val*7)%6])
  return matchToSum(decList, 8)
  
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
