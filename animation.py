#!/usr/bin/env python
#
# github.com/roobert animated README.md!
#

import curses
from time import sleep
import random


def main(stdscr):
    curses.use_default_colors()

    title(stdscr)

    twinkle(stdscr, 2, 5)
    twinkle(stdscr, 20, 60)

    prompt_message(stdscr, "Hi, my name is Rob!")

    sleep(1)

    clear_line(stdscr, 20)

    prompt_message(
        stdscr,
        "I love coding",
    )

    sleep(2)

    backspace(stdscr, 20, 24, "coding")

    typewriter(
        stdscr,
        20,
        26,
        "collaboration",
    )

    sleep(2)

    backspace(stdscr, 20, 24, "collaboration")

    typewriter(
        stdscr,
        20,
        26,
        "infrastructure",
    )

    sleep(2)

    backspace(stdscr, 20, 24, "infrastructure")

    typewriter(
        stdscr,
        20,
        26,
        "automation!",
    )

    sleep(2)

    # blursed_heart(stdscr, 20, 21)
    # sleep(2)

    clear_line(stdscr, 20)

    sleep(2)


def title(stdscr):
    x = 17
    y = 10
    frame(stdscr, y, x, frame1, 3)
    frame(stdscr, y, x, frame2, 0.1)
    frame(stdscr, y, x, frame1, 0.25)
    frame(stdscr, y, x, frame0, 0.1)
    frame(stdscr, y, x, frame1, 0.25)
    frame(stdscr, y, x, frame0, 0.25)
    frame(stdscr, y, x, frame1, 0.1)
    frame(stdscr, y, x, frame0, 0.1)
    frame(stdscr, y, x, frame1, 0.1)
    frame(stdscr, y, x, frame0, 0.1)
    frame(stdscr, y, x, frame3, 0.1)
    frame(stdscr, y, x, frame1, 0.1)


def twinkle(stdscr, y, x):
    frame(stdscr, y, x, star0, 0.1, False)
    frame(stdscr, y, x, star1, 0.2, False)
    frame(stdscr, y, x, star2, 0.2, False)
    frame(stdscr, y, x, star3, 0.2, False)
    frame(stdscr, y, x, star4, 0.2, False)
    frame(stdscr, y, x, star5, 0.1, False)
    frame(stdscr, y, x, star6, 0.1, False)
    frame(stdscr, y, x, star7, 0.1, False)


def frame(stdscr, y, x, frame, interval, clear=True):
    indent = " " * x
    indented_frame = "\n".join([indent + line for line in frame.split("\n")])

    if clear:
        stdscr.clear()
    stdscr.addstr(y, 0, indented_frame)
    reset_cursor(stdscr)
    stdscr.refresh()
    sleep(interval)


def clear_line(stdscr, line_number):
    _, width = stdscr.getmaxyx()
    line = " " * (width - 1)
    stdscr.addstr(line_number, 0, line)


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
        interval = 0.1
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

if __name__ == "__main__":
    curses.wrapper(main)
