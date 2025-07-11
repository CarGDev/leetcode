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
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_string = float(-inf)
        ans = ""
        i = 0

        def checker(l, r, a, mx):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_string:
                    a = s[l : r + 1]
                    mx = r - l + 1
                l -= 1
                r += 1
            return a, mx

        for i in range(len(s)):
            ans, max_string = checker(i, i, ans, max_string)
            ans, max_string = checker(i, i + 1, ans, max_string)

        return ans


# @leet end

