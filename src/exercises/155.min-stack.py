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
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or self.min[-1] >= val:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end

