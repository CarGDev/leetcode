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
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_abs = float(inf)
        ans = []
        for i in range(len(arr) - 1):
            abs_sum = abs(arr[i] - arr[i + 1])
            if abs_sum < min_abs:
                ans = []
                min_abs = abs_sum
                ans.append([arr[i], arr[i + 1]])
            elif abs_sum == min_abs:
                ans.append([arr[i], arr[i + 1]])

        return ans


# @leet end
