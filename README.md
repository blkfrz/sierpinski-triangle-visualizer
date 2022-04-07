# Sierpinski Triangle Visualizer
### Python based Sierpinski triangle visualizer made with Pygame.

This visualizer follows a series of specific steps that allow for the gradual plotting of a Sierpinski triangle.
- Plot 3 vertices of an equilateral triangle.
- Plot a point anywhere inside the area defined by the equilateral triangle.
- Choose any of the triangle vertices and plot the midpoint between the starting point and the selected vertex.
- Repeat the last step (any amount of times).

Following this rules will result in an image such as this:


![Alt Text](https://i.imgur.com/rTNzFul.gif)


## Commands

- A - Toggles the automatic mode. This way there's no need to hold space to progress.
- R - Resets the visualizer to the initial state.
- SPACE - Hold it down to progress. Won't do anything on automatic mode.
- UP ARROW - Increse the tick speed, 5 by 5 to a maximum of 5000. 
- DOWN ARROW - Decrease the tick speed, 5 by 5 to a minimum of 10.
- TAB - Toggles the menu.


## Requirements

- [Python] (tested under Python 3.8.0)
- [Pygame] (tested under Pygame 2.1.2)

   [Python]: <https://www.python.org>
   [Pygame]: <https://www.pygame.org/wiki/GettingStarted>

