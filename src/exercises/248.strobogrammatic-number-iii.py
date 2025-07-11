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
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def gen_str(l):
            if l == 0:
                return [""]
            if l == 1:
                return ["0", "1", "8"]
            sub_ans = []
            for n in gen_str(l - 2):
                for pair in ("11", "88", "69", "96"):
                    sub_ans.append(pair[0] + n + pair[1])
                if l != num_l:
                    sub_ans.append("0" + n + "0")
            return sub_ans

        min_l, max_l = len(low), len(high)
        low, high = int(low), int(high)
        count = 0

        for num_l in range(min_l, max_l + 1):
            for num_str in gen_str(num_l):
                if low <= int(num_str) <= high:
                    count += 1
        return count


# @leet end

