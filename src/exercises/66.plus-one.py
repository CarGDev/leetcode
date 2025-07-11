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
    def plusOne(self, digits: List[int]) -> List[int]:
        def sumDigits(arr, con, i):
            if i < 0:
                arr.insert(0, con)
                return arr
            if con != None:
                n = arr[i] + con
            else:
                n = arr[i] + 1
            if n < 10:
                arr[i] = n
            else:
                ci = n % 10
                con = n // 10
                arr[i] = ci
                return sumDigits(arr, con, i - 1)
            return arr

        return sumDigits(digits, None, len(digits) - 1)


# @leet end

