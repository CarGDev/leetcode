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
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return x
        lw = 1
        lm = x
        while lw < lm:
            mid = (lw + lm) // 2
            s = mid**2
            if s <= x:
                lw = mid + 1
            else:
                lm = mid
        return lw - 1


# @leet end

