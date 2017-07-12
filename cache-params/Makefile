CC = clang++
FLAGS = -g -c -std=c++11

SOURCEDIR = src
SOURCES = $(wildcard $(SOURCEDIR)/*.cc)
BUILDDIR = build

EXECUTABLE = cache
SOURCES = $(wildcard $(SOURCEDIR)/*.cc)
OBJECTS = $(patsubst $(SOURCEDIR)/%.cc,$(BUILDDIR)/%.o,$(SOURCES))

all: dir $(BUILDDIR)/$(EXECUTABLE)

dir:
	mkdir -p $(BUILDDIR)

$(BUILDDIR)/$(EXECUTABLE): $(OBJECTS)
	$(CC) $^ -o $@

$(OBJECTS): $(BUILDDIR)/%.o : $(SOURCEDIR)/%.cc
	$(CC) $(FLAGS) $< -o $@

clean:
	rm -f $(BUILDDIR)/*o $(BUILDDIR)/$(EXECUTABLE)
