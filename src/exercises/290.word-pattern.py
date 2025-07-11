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
    def wordPattern(self, pattern: str, s: str) -> bool:
        w = {}
        ss = s.split(" ")
        if len(pattern) != len(ss):
            return False

        for i in range(len(ss)):
            if pattern[i] not in w and ss[i] not in w.values():
                w[pattern[i]] = ss[i]
        for i in range(len(ss)):
            if pattern[i] not in w:
                return False
            if ss[i] != w[pattern[i]]:
                return False

        return True



# @leet end

