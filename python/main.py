from CLI import CLI
from GUI import GUI
import sys

# Checks if any command line arguments have been passed, if they have then CLI is used,
# if not then the GUI is used
if not len(sys.argv) > 1:
    ui = GUI()
else:
    cli = CLI()
