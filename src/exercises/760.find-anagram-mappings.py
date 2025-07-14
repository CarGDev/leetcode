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
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsList = {}
        j = 0
        for i in nums2:
            if i not in numsList:
                numsList[i] = j
            j += 1

        arr = []
        for i in nums1:
            arr.append(numsList[i])
        return arr


# @leet end

