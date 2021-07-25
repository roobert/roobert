#!/usr/bin/env python
#
# github.com/roobert animated README.md!
#

# TODO
# * auto positioning
# * star mask
# * switch from window to pad
# * improve horizon

import curses
from curses import error
from time import sleep
import random


def main(stdscr):
    curses.use_default_colors()

    camera_pan(stdscr)
    starfield(stdscr)
    type_title(stdscr)
    title(stdscr)
    typewriter(stdscr, 20, 30, "CORPORATION")
    sleep(2)
    shoot(stdscr, 20, 30, "CORPORATION")
    twinkle(stdscr, 2, 5)
    twinkle(stdscr, 20, 60)
    prompt_messages(stdscr)
    atomise(stdscr)


def camera_pan(stdscr):
    horizon = 15
    height, width = stdscr.getmaxyx()
    for y in range(0, height):
        line = "#" * (width - 2)
        stdscr.addstr(y, 0, line)
        stdscr.refresh()

    height, width = stdscr.getmaxyx()
    for y in range(0, height - horizon):
        line = " " * (width - 2)
        stdscr.addstr(y, 0, line)
        reset_cursor(stdscr)
        stdscr.refresh()
        sleep(0.05)


def starfield(stdscr, interval=0.1):
    horizon = 15
    for _ in range(0, 100):
        height, width = stdscr.getmaxyx()
        height = height - horizon
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        stdscr.addch(int(y), int(x), ".")
        reset_cursor(stdscr)
        stdscr.refresh()
        sleep(interval)


def type_title(stdscr):
    x = 17
    y = 10
    frame(stdscr, y, x, letter0, 0.75)
    frame(stdscr, y, x + 10, letter1, 0.75)
    frame(stdscr, y, x + 20, letter2, 0.75)
    frame(stdscr, y, x + 30, letter3, 0.75)


def title(stdscr):
    x = 17
    y = 10
    frame(stdscr, y, x, frame1, 3)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame2, 0.1)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame1, 0.25)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame0, 0.1)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame1, 0.25)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame0, 0.25)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame1, 0.1)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame0, 0.1)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame1, 0.1)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame0, 0.1)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame3, 0.1)
    frame(stdscr, y, x, blank, 0)
    frame(stdscr, y, x, frame1, 0.1)


def shoot(stdscr, y, x, s):
    for i in _shuffle(list(range(x, x + len(s)))):
        stdscr.addch(y, i, " ")
        reset_cursor(stdscr)
        interval = random.uniform(0.0, 0.3)
        sleep(interval)
    reset_cursor(stdscr)


def prompt_messages(stdscr):
    y = 20

    prompt_message(stdscr, "Hi, my name is Rob!")
    sleep(1)
    backspace(stdscr, y, 18, "Hi, my name is Rob!")

    prompt_message(stdscr, "I love coding")
    sleep(2)
    backspace(stdscr, y, 24, "coding")

    typewriter(stdscr, y, 26, "collaboration")
    sleep(2)
    backspace(stdscr, y, 24, "collaboration")

    typewriter(stdscr, y, 26, "infrastructure")
    sleep(2)
    backspace(stdscr, y, 24, "infrastructure")

    typewriter(stdscr, y, 26, "automation!")
    sleep(2)
    clear_line(stdscr, y)

    reset_cursor(stdscr)
    sleep(2)


def twinkle(stdscr, y, x):
    frame(stdscr, y, x, star0, 0.1)
    frame(stdscr, y, x, blank_star, 0)
    frame(stdscr, y, x, star1, 0.2)
    frame(stdscr, y, x, blank_star, 0)
    frame(stdscr, y, x, star2, 0.2)
    frame(stdscr, y, x, blank_star, 0)
    frame(stdscr, y, x, star3, 0.2)
    frame(stdscr, y, x, blank_star, 0)
    frame(stdscr, y, x, star4, 0.2)
    frame(stdscr, y, x, blank_star, 0)
    frame(stdscr, y, x, star5, 0.1)
    frame(stdscr, y, x, blank_star, 0)
    frame(stdscr, y, x, star6, 0.1)
    frame(stdscr, y, x, blank_star, 0)
    frame(stdscr, y, x, star7, 0.1)
    frame(stdscr, y, x, blank_star, 0)


def atomise(stdscr):
    lines = frame3.split("\n")
    top_line = 12
    count = 0
    indent = 16

    # iterate through the line numbers on the screen which contain the title
    for line_number in range(top_line, top_line + len(lines), 1):

        # iterate through each line number above the title, to 0
        for move_to in range(line_number - 1, -1, -1):

            # iterate across the line randomly
            for x in _shuffle(list(range(indent, indent + len(lines[count]), 1))):
                try:
                    c = stdscr.inch(move_to + 1, x)
                    clear_char(stdscr, move_to + 1, x)
                    y_new = move_to + int(random.uniform(-1, -10))
                    stdscr.addch(y_new, x, c)

                    reset_cursor(stdscr)
                    stdscr.refresh()
                    sleep(0.001)

                # ignore errors when writing to off-screen co-ords
                except error:
                    pass
        clear_line(stdscr, 0)
        count += 1


def _shuffle(array):
    random.shuffle(array)
    return array


def frame(stdscr, y, x, frame, interval):
    row = y
    for line in frame.split("\n"):
        stdscr.addstr(row, x, line)
        reset_cursor(stdscr)
        stdscr.refresh()
        row += 1
    sleep(interval)


def clear_line(stdscr, line_number):
    _, width = stdscr.getmaxyx()
    line = " " * (width - 1)
    stdscr.addstr(line_number, 0, line)
    reset_cursor(stdscr)
    stdscr.refresh()


def clear_char(stdscr, y, x):
    stdscr.addch(y, x, " ")
    stdscr.refresh()


def typewriter(stdscr, y, x, s):
    for c in s:
        stdscr.addch(y, x, c)
        stdscr.refresh()
        interval = random.uniform(0.0, 0.3)
        sleep(interval)
        x += 1


def backspace(stdscr, y, x, word):
    x = x + 1 + len(word)
    i = 0
    while i < len(word):
        stdscr.addch(y, (x - i), " ")
        stdscr.move(y, (x - i))
        stdscr.refresh()
        interval = 0.02
        sleep(interval)
        i += 1


def prompt_message(stdscr, s):
    indent = 17
    y, x = 20, indent + 2

    stdscr.addstr(y, indent, "> ")
    stdscr.refresh()
    sleep(1.5)

    typewriter(stdscr, y, x, s)


def blursed_heart(stdscr, y, x):
    stdscr.addch(y, x, '❤️"')
    stdscr.move(y, x)
    stdscr.refresh()


def reset_cursor(stdscr):
    height, width = stdscr.getmaxyx()
    stdscr.move(height - 1, width - 1)
    stdscr.refresh()


letter0 = """

:::::::::
:+:    :+:
+:+    +:+
+#+    +:+
+#+    +#+
#+#    #+#
######### 

"""

letter1 = """

:::    :::
:+:    :+:
+:+    +:+
+#+    +:+
+#+    +#+
#+#    #+#
 ######## 

"""

letter2 = """

 :::::::::
:+:    :+:
+:+       
+#++:++#++
       +#+
#+#    #+#
 ######## 

"""

letter3 = """

::::::::::
   :+:
   +:+
   +#+
   +#+
   #+#
   ###

"""

# FIXME - replace blank frames with character masks
blank = """
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
                                               
"""

frame0 = """
*******   **     **  ******** **********
/**////** /**    /** **////// /////**///
/**    /**/**    /**/**           /**
/**    /**/**    /**/*********    /**
/**    /**/**    /**////////**    /**
/**    ** /**    /**       /**    /**
/*******  //*******  ********     /**
///////    ///////  ////////      //

"""

frame1 = """

::::::::: :::    ::: :::::::::::::::::::
:+:    :+::+:    :+::+:    :+:   :+:
+:+    +:++:+    +:++:+          +:+
+#+    +:++#+    +:++#++:++#++   +#+
+#+    +#++#+    +#+       +#+   +#+
#+#    #+##+#    #+##+#    #+#   #+#
#########  ########  ########    ###

"""

frame2 = """

      ::::::::: :::    ::: ::::::::::::::::::: 
     :+:    :+::+:    :+::+:    :+:   :+:      
    +:+    +:++:+    +:++:+          +:+       
   +#+    +:++#+    +:++#++:++#++   +#+        
  +#+    +#++#+    +#+       +#+   +#+         
 #+#    #+##+#    #+##+#    #+#   #+#          
#########  ########  ########    ###

"""

frame3 = """
 ::::::::: :::    ::: :::::::::::::::::::
 :+:    :+::+:    :+::+:    :+:   :+:
 +:+    +:++:+    +:++:+          +:+
 +#+    +:++#+    +:++#++:++#++   +#+
 +#+    +#++#+    +#+       +#+   +#+
 #+#    #+##+#    #+##+#    #+#   #+#
 #########  ########  ########    ###

"""

star0 = """
     
     
    + 
     
     
"""

star1 = """
     
   \ /
    x 
   / \\
     
"""

star2 = """
     
    . 
   -+-
    '  
     
"""

star3 = """
     
    |
  - x - 
    |
     
"""

star4 = """
    .
    |
 --   --
    |
    '
"""

star5 = """
    .
     
 -     -
     
    '
"""

star6 = """
    .
     
         
     
    '
"""

star7 = """
     
     
        
     
     
"""

blank_star = """
     
      
        
      
     
"""

if __name__ == "__main__":
    curses.wrapper(main)
