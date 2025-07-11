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
    def maxArea(self, height: List[int]) -> int:
        i, j, max_vol = 0, len(height) - 1, 0
        while i < j:
            if height[i] > height[j]:
                max_vol = max(max_vol, min(height[i], height[j]) * (j - i))
                j -= 1
            elif height[j] >= height[i]:
                max_vol = max(max_vol, min(height[i], height[j]) * (j - i))
                i += 1

        return max_vol


# @leet end

