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
    def specialTriplets(self, nums: List[int]) -> int:
        j = 0
        count_left = {}
        count_right = {}
        total = 0
        for i in nums:
            if i not in count_right:
                count_right[i] = 1
            else:
                count_right[i] += 1

        while j < len(nums) - 1:
            count_right[nums[j]] -= 1
            target = nums[j] * 2

            left_count = count_left.get(target, 0)
            right_count = count_right.get(target, 0)

            total += left_count * right_count

            # Update count_left with current value
            if nums[j] not in count_left:
                count_left[nums[j]] = 1
            else:
                count_left[nums[j]] += 1

            j += 1

        return total % (10**9 + 7)


# @leet end

