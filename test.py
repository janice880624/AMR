import sys
import tty, termios

if __name__ == '__main__':

  print ('press Q to quit')

  while True:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
      tty.setraw(fd)
      ch = sys.stdin.read(1)

    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

      if ch == 'w':
        print("w")
      elif ch == 'a':
        print("a")
      elif ch == 's':
        print("s")
      elif ch == 'd':
        print("d")
      elif ch == 'q':
        print("shutdown")
        break