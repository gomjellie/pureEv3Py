import curses
import time

class KeyBoard(object):
    '''
    on MAC 
        68=>left, 66=>down, 67=>right, 65=>top

    '''
    def __init__(self):
    	self.c = 0
    	self.stdscr = curses.initscr()
    	curses.noecho()
    	curses.cbreak()
    	self.stdscr.nodelay(1)
    	
    def get_ch(self):
        while True:
            self.c = self.stdscr.getch()
            if self.c != -1:
                if self.c == 68:
                    key_in = 'left'
                elif self.c == 65:
                    key_in = 'top'
                elif self.c == 67:
                    key_in = 'right'
                elif self.c == 66:
                    key_in = 'down'
                else:
                    key_in = 'N/A'
                self.stdscr.addstr(' ' + str(self.c) + ' ' + key_in)
                self.stdscr.refresh()
                self.stdscr.move(0, 0)
        else:
            curses.endwin()
    
if __name__ == '__main__':
    keyBoard = KeyBoard()
    while 1:
    	keyBoard.get_ch()

