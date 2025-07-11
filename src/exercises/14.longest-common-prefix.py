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
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]
        m = float(inf)
        for w in strs:
            m = len(w) if len(w) < m else m
        for i in range(len(strs)):
            strs[i] = strs[i][:m]

        h = m
        for i in range(m - 1, -1, -1):
            current = strs[0][i]
            for j in range(1, len(strs), +1):
                if strs[j][i] != current:
                    h = i

        return strs[0][:h]


# @leet end
