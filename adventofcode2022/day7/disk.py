from __future__ import annotations
from dataclasses import dataclass, field
import re


@dataclass
class Directory:
    children: dict[str, Directory | File] = field(default_factory=dict)


@dataclass
class File:
    size: int


class DirectorySize:
    def __init__(self):
        self.dir_sizes = []

    @classmethod
    def visit(cls, root: Directory) -> int:
        visitor = cls()
        visitor.visit_child(root)

        return sum(size for size in visitor.dir_sizes)

    def visit_child(self, node: File | Directory):
        if isinstance(node, File):
            return node.size
        else:
            this_size = sum(self.visit_child(child) for child in node.children.values())
            if this_size <= 100000:
                self.dir_sizes.append(this_size)

            return this_size


class DeleteDirectory:
    def __init__(self):
        self.dir_sizes = []

    @classmethod
    def visit(cls, root: Directory, total_size = 70_000_000, need_free = 30_000_000) -> int:
        visitor = cls()
        used_size = visitor.visit_child(root)
        free = total_size - used_size
        need_to_free = need_free - free
        for size in sorted(visitor.dir_sizes):
            if size >= need_to_free:
                return size

    def visit_child(self, node: File | Directory):
        if isinstance(node, File):
            return node.size
        else:
            this_size = sum(self.visit_child(child) for child in node.children.values())
            self.dir_sizes.append(this_size)

            return this_size


def build_disk(lines: list[str]) -> Directory:
    root = Directory()
    curdir = [root]

    for line in lines:
        if cd_pattern := re.search(r"\$ cd (?P<arg>\S+)", line):
            arg = cd_pattern["arg"]
            if arg == "/":
                curdir = [root]
            elif arg == "..":
                curdir.pop()
            else:
                curdir.append(curdir[-1].children[arg])
        elif re.search(r"\$ ls", line):
            continue
            
        if dir_pattern := re.search(r"dir (?P<arg>\S+)", line):
            curdir[-1].children[dir_pattern["arg"]] = Directory()
        elif file_pattern := re.search(r"(?P<size>\d+) (?P<name>[\w\.]+)", line):
            curdir[-1].children[file_pattern["name"]] = File(int(file_pattern["size"]))

    return root


def parse1(lines: list[str]) -> int:
    root = build_disk(lines)

    return DirectorySize.visit(root)


def parse2(lines: list[str]) -> int:
    root = build_disk(lines)

    return DeleteDirectory.visit(root)