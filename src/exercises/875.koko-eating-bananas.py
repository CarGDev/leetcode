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
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bs(val, low, high, len):
            if low > high:
                return val
            mid = (low + high) // 2
            sum_v = 0
            for i in range(len):
                sum_v += (piles[i]  + mid - 1) // mid
            if sum_v <= h:
                min_val = min(val, mid)
                return bs(min_val, low, mid - 1, len)
            else:
                return bs(val, mid + 1, high, len)

        return bs(float(inf), 1, max(piles), len(piles))


# @leet end

