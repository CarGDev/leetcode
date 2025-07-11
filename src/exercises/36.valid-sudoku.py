from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *


# @leet start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(len(board))]
        square = [{} for _ in range(len(board))]
        for i in range(len(board)):
            cols = {}
            for j in range(len(board[i])):
                val = board[i][j]
                if val != ".":
                    if val in cols:
                        return False
                    cols[val] = j
                    if val in rows[j]:
                        return False
                    rows[j][val] = i
                    if i < 3:
                        if j < 3:
                            if val in square[0]:
                                return False
                            square[0][val] = i
                        elif j > 2 and j < 6:
                            if val in square[1]:
                                return False
                            square[1][val] = i
                        elif j > 5:
                            if val in square[2]:
                                return False
                            square[2][val] = i
                    elif i > 2 and i < 6:
                        if j < 3:
                            if val in square[3]:
                                return False
                            square[3][val] = i
                        elif j > 2 and j < 6:
                            if val in square[4]:
                                return False
                            square[4][val] = i
                        elif j > 5:
                            if val in square[5]:
                                return False
                            square[5][val] = i
                    elif i > 5:
                        if j < 3:
                            if val in square[6]:
                                return False
                            square[6][val] = i
                        elif j > 2 and j < 6:
                            if val in square[7]:
                                return False
                            square[7][val] = i
                        elif j > 5:
                            if val in square[8]:
                                return False
                            square[8][val] = i


        return True


# @leet end

