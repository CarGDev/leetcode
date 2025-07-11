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
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word_indices = {}
        for i, word in enumerate(wordsDict):
            word_indices.setdefault(word, []).append(i)

        pos1 = word_indices[word1]
        pos2 = word_indices[word2]

        # Two-pointer traversal
        i, j = 0, 0
        min_distance = float("inf")

        if word1 == word2:
            for i in range(len(pos1)):
                for j in range(len(pos2)):
                    if i != j:
                        min_distance = min(min_distance, abs(pos2[i] - pos2[j]))
            return min_distance

        while i < len(pos1) and j < len(pos2):
            index1 = pos1[i]
            index2 = pos2[j]
            min_distance = min(min_distance, abs(index1 - index2))

            # Move the pointer pointing to the smaller index
            if index1 < index2:
                i += 1
            else:
                j += 1

        return min_distance


# @leet end

