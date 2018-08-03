#Makefile

EXECUTABLE := __init__

SOURCES := *.py

EXT := py
CC := python2

0:
	$(CC) $(SOURCES)
	$(CC) $(EXECUTABLE).$(EXT) 0

1:
	$(CC) $(SOURCES)
	$(CC) $(EXECUTABLE).$(EXT) 1

2:
	$(CC) $(SOURCES)
	$(CC) $(EXECUTABLE).$(EXT) 2
realclean:
	find . -type f -name "*.pyc" -exec rm '{}' \;

# this line required by make - don't delete
