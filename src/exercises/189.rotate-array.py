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
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        l = len(nums)
        arr = [0] * l
        k = k % len(nums) if k > len(nums) else k
        j = 1
        for i in range(l - 1, -1, -1):
            x = k - j
            if x < 0:
                x += l
            arr[x] = nums[i]
            j += 1
        for i in range(len(arr)):
            nums[i] = arr[i]
        
# @leet end
