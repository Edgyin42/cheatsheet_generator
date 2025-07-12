#### Delete: 
        d   motion
  Where:
    d      - is the delete operator.
    motion - is what the operator will operate on (listed below).

#### Motions:
    w - until the start of the next word, EXCLUDING its first character.
    e - to the end of the current word, INCLUDING the last character.
    $ - to the end of the line, INCLUDING the last character.

#### Undo: 
* u: undo
* U: return the lines to the original
* Undo the Undo: CTRL + R

#### PUT: 
* D and then p

#### Replace: 
* r and then the chareacter we want to replace

#### Change: 
* c is like d but after that it puts you in insert mode
* ce: delete to the end of the word and put you in insert mode
* Cc does the same but for the whole line.

#### Location: 
* gg to move to the start of the file*
* G to move to the end of the file
* 500G to move to line 500

#### Search: 
* / + word: To search for the phrase from that line
* ? + word: To search for the same phrase in the opposite direction. 
* n to search the same phrase again
* N to serach  the same phrase in the opposite direction 

#### Matching parenthesis search: 
* Place the cursor any of the parenthesis
* % to move to the match parenthesis. 

#### To substitute new for the first old in a line type    :s/old/new

* To substitute new for all 'old's on a line type       :s/old/new/g
* To substitute phrases between two line #'s type       :#,#s/old/new/g
* To substitute all occurrences in the file type        :%s/old/new/g
* To ask for confirmation each time add 'c'             :%s/old/new/gc

![[Screenshot 2025-07-10 at 8.51.40 PM.png]]
