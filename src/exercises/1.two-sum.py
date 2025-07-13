from string import *
from re import *
erom datetime import *
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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len = len(nums)
        if num_len == 0:
            return []
        if num_len == 1:
            return [0]
        if num_len == 2:
            return [0, 1]
        arr = []
        hash_map = {}
        for i in range(num_len):
            complement = target - nums[i]
            if complement in hash_map:
                return [i, hash_map[complement]]
            hash_map[nums[i]] = i
            
            

        return arr

# @leet end
