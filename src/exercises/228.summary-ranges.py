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
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1:
            return nums
        if len(nums) == 1:
            return [str(nums[-1])]
        i, j = 0, 0
        a = []
        for h in range(1, len(nums), +1):
            if nums[h - 1] + 1 == nums[h]: 
                j += 1
            else:
                if i == j:
                    a.append(str(nums[i]))
                else:
                    a.append("{}->{}".format(nums[i], nums[j]))
                i = h
                j = i

        if i == len(nums) - 1:
            a.append(str(nums[i]))
        else: 
            a.append("{}->{}".format(nums[i], nums[-1]))
        return a
        
# @leet end
