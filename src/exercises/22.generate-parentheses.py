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
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        if n == 1:
            return ["()"]

        stack = []
        res = []
        def retrieveParenthesis(open, close):
            if open == close == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append('(')
                retrieveParenthesis(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(')')
                retrieveParenthesis(open, close + 1)
                stack.pop()

        retrieveParenthesis(0, 0)

        return res


# @leet end

