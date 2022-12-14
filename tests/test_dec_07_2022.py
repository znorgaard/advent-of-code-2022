import unittest
from advent_of_code_2022 import dec_07_2022

example_data = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k"
]


class TestDirectory(unittest.TestCase):

    def test_children(self):
        test_directory = dec_07_2022.Directory("/")
        children_to_add = [dec_07_2022.Directory("sub-directory"), dec_07_2022.File("j", 123)]

        for child in children_to_add:
            test_directory.add_child(child)

        self.assertEqual(test_directory.children, children_to_add)
        self.assertEqual([child.parent for child in children_to_add], [test_directory] * 2)

        self.assertEqual(test_directory.child_directories(), ["sub-directory"])
        self.assertEqual(test_directory.child_files(), ["j"])

    def test_navigation(self):
        test_directory = dec_07_2022.Directory("/")
        child_directory_1 = dec_07_2022.Directory("sub-directory")
        child_directory_2 = dec_07_2022.Directory("bottom-directory")
        child_directory_1.add_child(child_directory_2)
        test_directory.add_child(child_directory_1)

        self.assertEqual(test_directory.find_root(), test_directory)
        self.assertEqual(test_directory.children[0].find_root(), test_directory)
        self.assertEqual(test_directory.children[0].children[0].find_root(), test_directory)
        self.assertEqual(child_directory_1.find_root(), test_directory)
        self.assertEqual(child_directory_2.find_root(), test_directory)

        self.assertEqual(test_directory.full_path(), "/")
        self.assertEqual(child_directory_1.full_path(), "//sub-directory")
        self.assertEqual(child_directory_2.full_path(), "//sub-directory/bottom-directory")

    def test_size(self):
        test_directory = dec_07_2022.Directory("/")
        sub_directory = dec_07_2022.Directory("sub-directory")
        files = [dec_07_2022.File("j", 1), dec_07_2022.File("k", 2)]
        children_to_add = [sub_directory] + files

        for child in files:
            sub_directory.add_child(child)

        for child in children_to_add:
            test_directory.add_child(child)

        self.assertEqual([file.get_size() for file in files], [1, 2])
        self.assertEqual(sub_directory.get_size(), 3)
        self.assertEqual(test_directory.get_size(), 6)


class TestBuildTree(unittest.TestCase):
    def test_example(self):
        dir_tree = dec_07_2022.build_tree(example_data)
        self.assertEqual(dir_tree.name, "/")

        # root contents
        self.assertEqual(dir_tree.child_directories(), ["a", "d"])
        self.assertEqual(dir_tree.child_files(), ["b.txt", "c.dat"])
        self.assertEqual(dir_tree.get_size(), 48381165)

        # a contents
        self.assertEqual(dir_tree.cd_child("a").child_directories(), ["e"])
        self.assertEqual(dir_tree.cd_child("a").child_files(), ["f", "g", "h.lst"])
        self.assertEqual(dir_tree.cd_child("a").get_size(), 94853)

        # d contents
        self.assertEqual(dir_tree.cd_child("d").child_directories(), [])
        self.assertEqual(dir_tree.cd_child("d").child_files(), ["j", "d.log", "d.ext", "k"])
        self.assertEqual(dir_tree.cd_child("d").get_size(), 24933642)

        # e contents
        self.assertEqual(dir_tree.cd_child("a").cd_child("e").child_directories(), [])
        self.assertEqual(dir_tree.cd_child("a").cd_child("e").child_files(), ["i"])
        self.assertEqual(dir_tree.cd_child("a").cd_child("e").get_size(), 584)

        expected_sizes = {"/": 48381165, "//a": 94853, "//d": 24933642, "//a/e": 584}
        self.assertEqual(dir_tree.dir_sizes(), expected_sizes)

        self.assertEqual(sum([size for dir_name, size in dir_tree.dir_sizes().items() if size <= 100000]), 95437)

        full_space = 70000000
        needed_space = 30000000
        used_space = dir_tree.get_size()
        self.assertEqual(used_space, 48381165)

        min_delete = needed_space - (full_space - used_space)
        self.assertEqual(min_delete, 8381165)

        to_delete = min([val for val in dir_tree.dir_sizes().values() if val >= min_delete])
        self.assertEqual(to_delete, 24933642)


