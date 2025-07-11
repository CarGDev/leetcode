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
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        consecutive = set(nums)
        consecutive = sorted(consecutive)
        counter = [0] * len(consecutive)
        count = 1
        k = 0
        for i in range(len(consecutive)):
            if i == 0:
                counter[k] = count
                continue
            if consecutive[i] == consecutive[i - 1] + 1:
                count += 1
            else:
                count = 1
                k += 1
            counter[k] = count
        max_num = 0
        counter = [i for i in counter if i > 0]
        for num in counter:
            max_num = max(max_num, num)
        return max_num
        
# @leet end
