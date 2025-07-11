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
    def kthDistinct(self, arr: List[str], k: int) -> str:
        disc = {}
        banW = []
        for w in arr:
            if w not in disc and w not in banW:
                disc[w] = 1
            else:
                if w not in banW:
                    banW.append(w)
                    del disc[w]

        arr = list(disc.keys())
        if k > len(arr): 
            return ""
        return arr[k - 1]


# @leet end

