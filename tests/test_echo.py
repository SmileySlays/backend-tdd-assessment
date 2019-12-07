#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        """ Running with text should make it uppercase """
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout[0:-1]
        self.assertEquals(stdout, "HELLO")

    def test_lower(self):
        """ Running with text should make it lowercase """
        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "HELLO"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout[0:-1]
        self.assertEquals(stdout, "hello")

    def test_title(self):
        """ Running with text should make the first letter capitalized """
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout[0:-1]
        self.assertEquals(stdout, "Hello")

    def test_all(self):
        """ Running with text should make it do the last command is """
        process = subprocess.Popen(
            ["python", "./echo.py", "-tlu", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout[0:-1]
        self.assertEquals(stdout, "HELLO")

    def test_none(self):
        """ Running with only text should return that text """
        process = subprocess.Popen(
            ["python", "./echo.py", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout[0:-1]
        self.assertEquals(stdout, "hello")


if __name__ == '__main__':
    unittest.main()
