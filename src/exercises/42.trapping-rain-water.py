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
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        c, m_l, m_r = 0, 0, 0
        while i < j:
            if height[i] < height[j]:
                if m_l < height[i]:
                    m_l = height[i]
                if (m_l - height[i]) > 0:
                    c += m_l - height[i]
                i += 1
            else:
                if m_r < height[j]:
                    m_r = height[j]
                if (m_r - height[j]) > 0:
                    c += m_r - height[j]
                j -= 1

        return c


# @leet end

