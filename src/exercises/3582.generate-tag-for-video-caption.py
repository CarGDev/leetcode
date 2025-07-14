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
    def generateTag(self, caption: str) -> str:
        words = caption.strip().split(" ")
        result = []

        for i in range(len(words)):
            clean = re.sub(r"[^a-zA-Z]", "", words[i])
            if not clean:
                continue
            if i == 0:
                result.append(clean.lower())
            else:
                result.append(clean[0].upper() + clean[1:].lower())

        return ("#" + "".join(result))[:100]


# @leet end

