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
    def canBeValid(self, s: str, locked: str) -> bool:
        var = ''
        new_str = []
        for i in s:
            new_str.append(i)

        for i in range(len(s)):
            if i % 2 == 0:
                var = '('
                if var != s[i] and locked[i] == "0":
                    new_str[i] = var
            elif i % 2 != 0:
                var = ')'
                if var != s[i] and locked[i] == "0":
                    new_str[i] = var

        count_v = 0
        count_x = 0
        for i in new_str:
            if i == ')':
                count_x += 1
            if i == '(':
                count_v += 1

        return count_v % 2 == 0 and count_x % 2 == 0


        
# @leet end
