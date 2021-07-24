#!/usr/bin/env python
#
# github.com/roobert animated README.md!
#

import curses
from time import sleep
import random


def main(stdscr):
    curses.use_default_colors()

    starfield(stdscr)

    title(stdscr)

    twinkle(stdscr, 2, 5)
    twinkle(stdscr, 20, 60)

    prompt_message(stdscr, "Hi, my name is Rob!")
    sleep(1)
    backspace(stdscr, 20, 18, "Hi, my name is Rob!")

    prompt_message(stdscr, "I love coding")
    sleep(2)
    backspace(stdscr, 20, 24, "coding")

    typewriter(stdscr, 20, 26, "collaboration")
    sleep(2)
    backspace(stdscr, 20, 24, "collaboration")

    typewriter(stdscr, 20, 26, "infrastructure")
    sleep(2)
    backspace(stdscr, 20, 24, "infrastructure")

    typewriter(stdscr, 20, 26, "automation!")
    sleep(2)
    clear_line(stdscr, 20)

    reset_cursor(stdscr)
    sleep(2)

    outro(stdscr)
    sleep(1)


def outro(stdscr):
    lines = frame3.split("\n")
    top_line = 12
    count = 0
    indent = 16

    for line_number in range(top_line, top_line + len(lines), 1):
        for move_to in range(line_number - 1, 0, -1):
            # iterate across the line
            for x in range(indent, indent + len(lines[count]), 1):
                c = lines[count].split()[x - indent]

                stdscr.addch(0, 0, c)
                reset_cursor(stdscr)
                stdscr.refresh()

                stdscr.addch(move_to - 1, x, c)
                clear_char(stdscr, move_to, x)
                reset_cursor(stdscr)
                stdscr.refresh()
                sleep(0.02)
        clear_line(stdscr, 0)
        count += 1


def starfield(stdscr):
    for _ in range(0, 100):
        height, width = stdscr.getmaxyx()
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        stdscr.addch(int(y), int(x), ".")
        reset_cursor(stdscr)
        stdscr.refresh()
        sleep(0.1)


def title(stdscr):
    x = 17
    y = 10
    frame(stdscr, y, x, frame1, 3)
    # outro(stdscr)
    # exit()
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
