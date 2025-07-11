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
    def partitionArray(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set(nums))
        nums = sorted(list(set(nums)))
        subs = 1
        miv = float(inf)
        for i in range(len(nums)):
            miv = nums[i] if miv > nums[i] else miv
            substraction = nums[i] - miv
            if substraction > k:
                subs += 1
                miv = nums[i]

        return subs


# @leet end

