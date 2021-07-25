#!/usr/bin/env python
#
# github.com/roobert animated README.md!
#

# TODO
# * auto positioning
# * refactor
# * turn cursor off/on

import curses
from curses import error
from time import sleep
import random


def main(stdscr):
    curses.use_default_colors()

    title_top = 10
    prompt_line = title_top + 10
    indent = int((curses.COLS / 2)) - 20
    horizon = 19

    curses.curs_set(0)
    star_coords, pad = camera_pan_down(stdscr, horizon)
    sleep(2)

    type_title(pad, title_top, indent)
    title(pad, title_top, indent)
    typewriter(pad, prompt_line, indent + 13, "CORPORATION")
    sleep(2)

    twinkle(pad, 2, 5)
    twinkle(pad, prompt_line, 60)
    sleep(1)

    shoot(pad, prompt_line, indent + 13, "CORPORATION")

    curses.curs_set(1)
    prompt_messages(pad, prompt_line, indent)
    curses.curs_set(0)

    atomise(pad, star_coords, title_top, indent)

    reset_cursor(pad)
    sleep(5)


def camera_pan_down(stdscr, horizon):
    horizon = 19
    height, width = stdscr.getmaxyx()
    pad = curses.newpad(height * 2, width)

    star_coords = gen_starfield(pad, height, width, horizon)
    gen_horizon(pad, height, width, horizon)

    for y in range(height, 0, -1):
        try:
            pad.refresh(0, 0, y, 0, height - 1, width - 1)
        except error:
            pass
        sleep(0.1)

    return star_coords, pad


def gen_starfield(pad, height, width, horizon):
    star_coords = {}
    for _ in range(0, 100):
        y = int(random.uniform(0, height - horizon))
        x = int(random.uniform(0, width))

        if not star_coords.get(y):
            star_coords[y] = []
        star_coords[y].append(x)

        pad.addch(y, x, ".")
    return star_coords


def gen_horizon(pad, height, width, horizon):
    # horizon
    line = "_" * width
    pad.addstr(height - horizon, 0, line)
    pad.addstr(height - (horizon - 2), 0, line)
    pad.addstr(height - (horizon - 5), 0, line)
    pad.addstr(height - (horizon - 10), 0, line)


def starfield_refresh(pad, star_coords):
    for y, values in star_coords.items():
        for x in values:
            pad.addch(y, x, ".")
    pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)


def type_title(pad, title_top, indent):
    x = indent
    y = title_top
    frame(pad, y, x, letter0, 0.75)
    frame(pad, y, x + 10, letter1, 0.75)
    frame(pad, y, x + 20, letter2, 0.75)
    frame(pad, y, x + 30, letter3, 0.75)


def title(pad, title_top, indent):
    x = indent
    y = title_top
    frame(pad, y, x, frame1, 3)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame2, 0.1)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame1, 0.25)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame0, 0.1)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame1, 0.25)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame0, 0.25)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame1, 0.1)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame0, 0.1)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame1, 0.1)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame0, 0.1)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame3, 0.1)
    frame(pad, y, x, blank, 0)
    frame(pad, y, x, frame1, 0.1)


def shoot(pad, y, x, s):
    for i in _shuffle(list(range(x, x + len(s)))):
        pad.addch(y, i, " ")
        reset_cursor(pad)
        interval = random.uniform(0.0, 0.3)
        sleep(interval)
    reset_cursor(pad)


def prompt_messages(pad, prompt_line, indent):
    y = prompt_line
    x = indent

    prompt_message(pad, y, x, "Hi, my name is Rob!")
    sleep(1)
    backspace(pad, y, x + 2 + len("Hi, my name is Rob!"), "Hi, my name is Rob!")

    prompt_message(pad, y, x, "I love coding..")
    sleep(2)
    backspace(pad, y, x + 2 + len("I love coding.."), "coding..")

    typewriter(pad, y, x + 2 + len("I love "), "collaboration..")
    sleep(2)
    backspace(pad, y, x + 2 + len("I love collaboration.."), "collaboration..")

    typewriter(pad, y, x + 2 + len("I love "), "infrastructure..")
    sleep(2)
    backspace(pad, y, x + 2 + len("I love infrastructure.."), "infrastructure..")

    typewriter(pad, y, x + 2 + len("I love "), "automation!")
    reset_cursor(pad)
    sleep(2)

    clear_line(pad, y)
    sleep(2)


def twinkle(pad, y, x):
    frame(pad, y, x, star0, 0.1)
    frame(pad, y, x, blank_star, 0)
    frame(pad, y, x, star1, 0.2)
    frame(pad, y, x, blank_star, 0)
    frame(pad, y, x, star2, 0.2)
    frame(pad, y, x, blank_star, 0)
    frame(pad, y, x, star3, 0.2)
    frame(pad, y, x, blank_star, 0)
    frame(pad, y, x, star4, 0.2)
    frame(pad, y, x, blank_star, 0)
    frame(pad, y, x, star5, 0.1)
    frame(pad, y, x, blank_star, 0)
    frame(pad, y, x, star6, 0.1)
    frame(pad, y, x, blank_star, 0)
    frame(pad, y, x, star7, 0.1)
    frame(pad, y, x, blank_star, 0)


def atomise(pad, star_coords, title_top, indent):
    lines = frame3.split("\n")
    count = 0

    # iterate through the line numbers on the screen which contain the title
    for line_number in range(title_top, title_top + len(lines), 1):

        # iterate through each line number above the title, to 0
        for move_to in range(line_number - 1, -1, -1):

            # iterate across the line randomly
            for x in _shuffle(list(range(indent, indent + len(lines[count]), 1))):
                try:
                    c = pad.inch(move_to + 1, x)
                    clear_char(pad, move_to + 1, x)
                    y_new = move_to + int(random.uniform(-1, -10))
                    pad.addch(y_new, x, c)

                    reset_cursor(pad)
                    pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)
                    sleep(0.001)

                # ignore errors when writing to off-screen co-ords
                except error:
                    pass

        clear_line(pad, 0)
        starfield_refresh(pad, star_coords)
        count += 1


def _shuffle(array):
    random.shuffle(array)
    return array


def frame(pad, y, x, frame, interval):
    row = y
    for line in frame.split("\n"):
        pad.addstr(row, x, line)
        reset_cursor(pad)
        pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)
        row += 1
    sleep(interval)


def clear_line(pad, line_number):
    _, width = pad.getmaxyx()
    line = " " * (width - 1)
    pad.addstr(line_number, 0, line)
    reset_cursor(pad)
    pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)


def clear_char(pad, y, x):
    pad.addch(y, x, " ")
    pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)


def typewriter(pad, y, x, s):
    for c in s:
        pad.addch(y, x, c)
        pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)
        interval = random.uniform(0.0, 0.3)
        sleep(interval)
        x += 1


def backspace(pad, y, x, word):
    i = 0
    while i < len(word):
        pad.addch(y, (x - i), " ")
        pad.move(y, (x - i))
        pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)
        interval = 0.03
        sleep(interval)
        i += 1


def prompt_message(pad, prompt_line, indent, s):
    y, x = prompt_line, indent + 2

    pad.addstr(y, indent, "> ")
    pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)
    sleep(1.5)

    typewriter(pad, y, x, s)


def blursed_heart(pad, y, x):
    pad.addch(y, x, '❤️"')
    pad.move(y, x)
    pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)


def reset_cursor(pad):
    height, width = pad.getmaxyx()
    pad.move(height - 1, width - 1)
    pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)


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
