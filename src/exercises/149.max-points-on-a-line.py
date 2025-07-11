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
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        i = 0
        mx = float(-inf)
        j = len(points) - 1

        def getM(i, j):
            y1 = points[i][1]
            y2 = points[j][1]
            x1 = points[i][0]
            x2 = points[j][0]
            if x2 - x1 == 0:
                mm = float(inf)
            else:
                mm = (y2 - y1) / (x2 - x1)
            return mm

        for i in range(len(points) - 1):
            m = {}
            for j in range(i + 1, len(points), +1):
                mm = getM(i, j)
                if mm not in m:
                    m[mm] = 1
                else:
                    m[mm] += 1
            lmx = max(m.values() if m else 0)
            mx = max(mx, lmx + 1)

        return mx


# @leet end

