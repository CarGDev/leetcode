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
        if len(s) % 2 != 0:
            return False
        mo = 0
        mxo = 0
        for i in range(len(s)):
            if locked[i] == "1":
                mo = mo + 1 if s[i] == "(" else mo - 1
                mxo = mxo + 1 if s[i] == "(" else mxo - 1
            else:
                mo -= 1
                mxo += 1
            if mxo < 0:
                return False
            mo = mo if mo > 0 else 0
        return mo == 0


# @leet end
