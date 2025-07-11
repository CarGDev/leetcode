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

# * I can be placed before V (5) and X (10) to make 4 and 9.
# * X can be placed before L (50) and C (100) to make 40 and 90.
# * C can be placed before D (500) and M (1000) to make 400 and 900.

# @leet start
class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        i = len(s) - 1
        while i > -1:
            if i == 0:
                count += numbers[s[i]]
            elif (
                (s[i] == "V" and s[i - 1] == "I")
                or (s[i] == "X" and s[i - 1] == "I")
                or (s[i] == "C" and s[i - 1] == "X")
                or (s[i] == "L" and s[i - 1] == "X")
                or (s[i] == "D" and s[i - 1] == "C")
                or (s[i] == "M" and s[i - 1] == "C")
            ):
                val = numbers[s[i]] - numbers[s[i - 1]]
                count += val
                i -= 1
            else:
                count += numbers[s[i]]
            i -= 1

        return count


# @leet end
