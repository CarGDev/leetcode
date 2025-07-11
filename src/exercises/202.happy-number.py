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
    def isHappy(self, n: int) -> bool:
        def getHappyNumber(num, memo):
            if num not in memo:
                memo.append(num)
            else:
                return False
            count = 0
            while num > 0:
                d = num % 10
                count += d**2
                num //= 10

            if count == 1:
                return True
            else:
                return getHappyNumber(count, memo)

        return getHappyNumber(n, [])


# @leet end

