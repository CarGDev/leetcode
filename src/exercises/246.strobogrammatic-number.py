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
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        left, right = 0, len(num) - 1

        while left <= right:
            if num[left] not in mapping or num[right] not in mapping:
                return False
            if mapping[num[left]] != num[right]:
                return False
            left += 1
            right -= 1

        return True


# @leet end
