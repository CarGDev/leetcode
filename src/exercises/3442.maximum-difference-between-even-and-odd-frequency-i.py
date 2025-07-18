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
    def maxDifference(self, s: str) -> int:
        record = Counter(s)
        max_odd = 0
        min_even = float(inf)

        for i in record.values():
            if i % 2 == 0:
                min_even = min(min_even, i)
            elif i % 2 != 0:
                max_odd = max(max_odd, i)

        return max_odd - min_even


# @leet end

