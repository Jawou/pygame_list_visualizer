from list_visualizer.py import numbers_displayer

display = numbers_displayer(1000, 1000, [1, 2, 3], 1, 5, "example", [1, 2, 3])
display.update_screen()

while True:
  clock.tick(67)
