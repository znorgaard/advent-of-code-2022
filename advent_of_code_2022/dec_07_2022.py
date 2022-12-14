# -*- coding: utf-8 -*-

"""
--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds.
Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system.
You try to run a system update:

```
$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
```

Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input).
For example:

```
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
```

The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files).
The outermost directory is called /.
You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory.
This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.
Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a).
These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion.
To do this, you need to determine the total size of each directory.
The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly.
(Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
Directory d has total size 24933642.
As the outermost directory, / contains every file.
Its total size is 48381165, the sum of the size of every file.
To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes.
In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584).
(As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

--- Part Two ---
Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000.
To run the update, you need unused space of at least 30000000.
You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update.
Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space.
However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
What is the total size of that directory?
"""
import logging

logging.getLogger().setLevel(logging.DEBUG)


class Directory:
    # For a real package, would add typing
    def __init__(self, name, parent=None, children=None):
        """ Object Initialization

        Args:
            name: name of directory
            parent: parent directory object
            children: list of children objects (File / Directory)
        """
        if children is None:
            children = []  # looking back, a dictionary probably would've been more helpful
        self.name = name
        self.parent = parent
        self.children = children

    def get_size(self):
        """ Get size of directory including all sub-directories and files

        Returns:
            integer for directory size
        """
        return sum([child.get_size() for child in self.children])

    def find_root(self):
        """ Find root directory of this directory

        Returns:
            The root directory object
        """
        if self.parent is None:
            return self
        else:
            return self.parent.find_root()

    def one_up(self):
        """ Find directory one up from this one

        Returns:
            parent directory object of this directory or self if parent is None
        """
        if self.parent is None:
            return self
        else:
            return self.parent

    def cd_child(self, child_name):
        """ Change directory to child directory

        Args:
            child_name: name of child directory
        Returns:
            child directory object with name == child_name or self if child does not exist
        """
        if child_name not in self.child_directories():
            return self
        else:
            cd_dirs = [child for child in self.children if child.name == child_name and isinstance(child, Directory)]
            return cd_dirs[0]

    def child_directories(self):
        """ Get list of child directory names

        Returns:
             list of child directory names
        """
        return [child.name for child in self.children if isinstance(child, Directory)]

    def child_files(self):
        """ Get list of child directory files

        Returns:
            list of child file names
        """
        return [child.name for child in self.children if isinstance(child, File)]

    def add_child(self, child):
        """ Adds child to directory

        Args:
            child: child object to be added, parent will be updated
        """
        child.parent = self
        self.children.append(child)

    def full_path(self):
        """ Get full path to self

        Returns:
            full path to self with "/" used as path separator (should use os.path.join instead)
        """
        if self.parent is not None:
            return self.parent.full_path() + "/" + self.name
        else:
            return self.name

    def dir_sizes(self):
        """ Get sizes of all directories

        Returns:
            directory with keys as full paths and values as sizes
        """
        sizes = {self.full_path(): self.get_size()}
        for child_dir in self.child_directories():
            sizes.update(self.cd_child(child_dir).dir_sizes())
        return sizes


class File:
    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.parent = parent

    def get_size(self):
        # Should make a super class of File/Directory that requires certain things for reliable use
        """ Get size of self

        Returns:
            int size of self
        """
        return self.size


def build_tree(terminal_text_list):
    """ Parse terminal text and build a directory tree

    Args:
        terminal_text_list: list of terminal commands
    Returns:
        root directory of tree
    """
    current_directory = Directory("/")
    for terminal_text in terminal_text_list:
        # Handle tree navigation
        if terminal_text.startswith("$ cd"):
            if terminal_text.endswith("/"):
                current_directory = current_directory.find_root()
            elif terminal_text.endswith(".."):
                current_directory = current_directory.one_up()
            else:
                cd_dir = terminal_text.split(" ")[-1]
                current_directory = current_directory.cd_child(cd_dir)

        elif not terminal_text.startswith("$"):
            part_one, part_two = terminal_text.split(" ")

            # Add new directories only
            if part_one == "dir" and part_two not in current_directory.child_directories():
                current_directory.add_child(Directory(name=part_two))
            elif part_one != "dir" and part_two not in current_directory.child_files():
                current_directory.add_child(File(name=part_two, size=int(part_one)))
            else:
                logging.warning(f'Unrecognized terminal text: {terminal_text}')

        elif terminal_text == "$ ls":
            pass
        else:
            logging.warning(f'Uncaptured terminal text: {terminal_text}')

    return current_directory.find_root()
