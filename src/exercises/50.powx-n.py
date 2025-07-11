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
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        def getP(xx, nn):
            if nn == 1: return xx
            h = getP(xx, nn // 2)
            if nn % 2 == 0:
                return h * h
            else:
                return xx * h * h
        if n < 0:
            return 1 / getP(x, abs(n))
        return getP(x, n)
# @leet end
