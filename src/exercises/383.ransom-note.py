# @leet imports start
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

# @leet imports end


# @leet start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def option1():
            d = {}
            for s in ransomNote:
                if s not in d:
                    d[s] = 1
                else:
                    d[s] += 1
            for m in magazine:
                if m in d:
                    d[m] -= 1
                    if d[m] == 0:
                        del d[m]
            return len(d.keys()) == 0

        def option2():
            r = Counter(ransomNote)
            m = Counter(magazine)
            return not(r - m)

        return option2()


# @leet end

