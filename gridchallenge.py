# -*- coding: utf-8 -*-

#
# python extrahopchallenge.py
# usage: extrahopchallenge.py [-h] textfile gridfile
#
# textfile -> File with html body text
# gridfile -> File with 8x8 grid of letters
#



import re
import sys
import argparse

GRID_SIZE = 8
MOVES = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
prog = re.compile('[^a-zA-Z0-9]')

def createWordList(document):
  """Return list of words from the file, ignoring punctuactions and cases.
  """
  wordList = set()
  try:
    with open(document, 'r') as fp:
      for line in fp:
        for word in line.strip().split():
          word = prog.sub('', word).lower()
          if word:
            wordList.add(word)
  except IOError as e:
    print "Error creating word list: {}".format(str(e))

  return wordList


def createGrid(gridFile):
  """Create 8x8 grid of letters from file.
  """
  grid = [[0 for x in xrange(GRID_SIZE)] for x in xrange(GRID_SIZE)]
  row = 0
  try:
    with open(gridFile, 'r') as fp:
      for line in fp:
        if row >= GRID_SIZE:
          raise SystemExit("Error: Grid size exceeds 8 rows.")
        col = 0
        for ltr in line.split():
          if col >= GRID_SIZE:
            raise SystemExit("Error: Grid size exceeds 8 columns.")
          grid[row][col] = ltr.strip().lower()
          col += 1
        row += 1

    if row != GRID_SIZE and col != GRID_SIZE:
      raise SystemExit("Error: Grid size must be 8.")

  except IOError as e:
    print "Error creating grid of letters: {}".format(str(e))

  return grid


def getNextPosition(x, y):
  """Return next possible move from the current position.
  """
  for move in MOVES:
    pos = (x + move[0], y + move[1])
    if 0 <= pos[0] < GRID_SIZE and 0 <= pos[1] < GRID_SIZE:
      yield pos

def filterWords(wordSet, pos, char):
  """Return candidate word list which matches the character in position.
  """
  temp = []
  for word in wordSet:
    if len(word) > pos:
      if word[pos] == char:
        temp.append(word)
  return set(temp)

def getCandidateWords(wordSet, grid, curX, curY, charPos=0, prefixStr='', longest_word=''):
  """Recursively traverse the grid and return the longest word from the starting position.
  """

  # reduce the wordList size to set of words that matches the startLetter in charPos
  startLetter = grid[curX][curY]
  wordSet = filterWords(wordSet, charPos, startLetter)

  # base condition
  if len(wordSet)  == 0:
    return longest_word

  # validate if prefixStr is a full word in the word set
  prefixStr += startLetter
  if prefixStr in wordSet:
    if len(prefixStr) > len(longest_word):
      longest_word = prefixStr
    #print "longest_word is %s" % longest_word

  # do this for 8 next possible moves
  for x, y in getNextPosition(curX, curY):
    longest_word = getCandidateWords(wordSet, grid, x, y, charPos+1, prefixStr, longest_word)

  return longest_word

def findLongestWord(wordList, grid):
  """Return the longest word from the grid.
  """
  longest_word = ''
  x, y = -1, -1
  # get the candidate words
  for i in xrange(GRID_SIZE):
    for j in xrange(GRID_SIZE):
      word = getCandidateWords(wordList, grid, i, j)
      if len(word) > len(longest_word):
        longest_word = word
        x, y = i, j
      #print "longest word at (%s, %s): %s" % (i, j, longest)

  return (longest_word, x, y)

def main():
  parser = argparse.ArgumentParser(description='Programming Problem - '
    'Return the longest word from the list that can be produced from a 8x8 grid of letters')
  parser.add_argument('textfile',
                    help='path to the text file to test candidate words')
  parser.add_argument('gridfile',
                    help='file containing 8x8 grid of letters')
  args = parser.parse_args()

  wordList = createWordList(args.textfile)
  grid = createGrid(args.gridfile)
  longestWord, i, j = findLongestWord(wordList, grid)
  if len(longestWord) > 0:
    sys.stdout.write("Longest word is {0} starting at position {1}\n".format(longestWord, (i+1,j+1)))
  else:
    sys.stdout.write("No words found in the grid.")
  return


if __name__ == '__main__':
  sys.exit(main())
