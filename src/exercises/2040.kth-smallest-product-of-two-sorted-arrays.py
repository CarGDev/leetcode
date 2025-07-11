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
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        low = -(10**10)
        high = 10**10

        def countLessEqual(p):
            count = 0
            for i in range(len(nums1)):
                l, h = 0, len(nums2)
                if nums1[i] == 0 and p >= 0:
                    count += len(nums2)
                elif nums1[i] > 0:
                    while l < h:
                        mid = (l + h) // 2
                        x = nums1[i] * nums2[mid]
                        if x <= p:
                            l = mid + 1
                        else:
                            h = mid
                    count += l
                else:
                    while l < h:
                        mid = (l + h) // 2
                        x = nums1[i] * nums2[mid]
                        if x <= p:
                            h = mid
                        else:
                            l = mid + 1
                    count += len(nums2) - l

                    

            return count

        while low < high:
            mid = (low + high) // 2
            count = countLessEqual(mid)
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low


# @leet end
