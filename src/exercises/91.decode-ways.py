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
    @lru_cache(maxsize=None)
    def getWordsCount(self, i, s) -> int:
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        if i == len(s) - 1:
            return 1
        answer = self.getWordsCount(i + 1, s)
        if int(s[i : i + 2]) < 27:
            answer += self.getWordsCount(i + 2, s)
        return answer

    def numDecodings(self, s: str) -> int:
        return self.getWordsCount(0, s)


# @leet end

