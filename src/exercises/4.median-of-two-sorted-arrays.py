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
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1, N2 = nums1, nums2
        lt = len(N1) + len(N2)
        half = lt // 2

        if len(N1) > len(N2):
            N1, N2 = N2, N1

        l = 0
        h = len(N1) - 1
        while True:
            midA = (l + h) // 2
            midB = half - midA - 2

            aLeft = N1[midA] if midA >= 0 else float(-inf)
            aRight = N1[midA + 1] if (midA + 1) < len(N1) else float(inf)

            bLeft = N2[midB] if midB >= 0 else float(-inf)
            bRight = N2[midB + 1] if (midB + 1) < len(N2) else float(inf)

            if aLeft <= bRight and bLeft <= aRight:
                if lt % 2 == 0:
                    return (min(bRight, aRight) + max(bLeft, aLeft)) / 2
                else:
                    return min(bRight, aRight)
            if aLeft > bRight:
                h = midA - 1
            else:
                l = midA + 1

# @leet end
