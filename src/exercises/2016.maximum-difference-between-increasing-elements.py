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
    def maximumDifference(self, nums: List[int]) -> int:
        max_val = -1
        for i in range(len(nums)):
            j = len(nums) - 1
            while j > i:
                if nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    max_val = max(diff, max_val)
                j -= 1

        return max_val


# @leet end

