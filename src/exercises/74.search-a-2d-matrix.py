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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def row_search(low, high):
            if low > high:
                return -1
            if matrix[low][0] <= target and target <= matrix[0][len(matrix[low]) - 1]:
                return low
            if matrix[high][0] <= target and target <= matrix[0][len(matrix[high]) - 1]:
                return high

            mid = (low + high) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid]) - 1]:
                return mid
            if matrix[mid][0] < target:
                return row_search(mid + 1, high)
            if matrix[mid][0] > target:
                return row_search(low, mid - 1)

        row = row_search(0, len(matrix) - 1)
        nums = matrix[row]

        def bin_search(low, high):
            if low > high:
                return -1
            mid = (high + low) // 2
            if nums[low] == target:
                return low
            if nums[high] == target:
                return high
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return bin_search(mid + 1, high)
            if nums[mid] > target:
                return bin_search(low, mid - 1)

        isValid = bin_search(0, len(nums) - 1)
        return isValid != -1


# @leet end

