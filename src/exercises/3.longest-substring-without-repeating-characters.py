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
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        window = {}
        max_char = 0
        while j < len(s):
            if s[j] not in window:
                window[s[j]] = 1
                max_char = len(window.keys()) if max_char < len(window.keys()) else max_char
                j += 1
            elif s[j] in window:
                del window[s[i]]
                i += 1
                        
        return max_char
# @leet end

