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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        arr = []
        for i in range(0, len(nums) - 1):
            j = i + 1
            k = n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                sum = nums[j] + nums[i] + nums[k]
                if sum == 0:
                    val = [nums[i], nums[j], nums[k]]
                    val.sort()
                    arr.append(val)
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
        return arr


# @leet end

