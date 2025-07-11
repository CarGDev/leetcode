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
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()
        new_s = s[::-1]
        return s == new_s


# @leet end

