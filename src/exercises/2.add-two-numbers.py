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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def node(self, val, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        value_l1 = l1
        value_l2 = l2
        head = None
        tail = None
        while value_l1 or value_l2:
            l2_val = l2.val if l2 else 0
            l1_val = l1.val if l1 else 0
            addition = l1_val + l2_val + carry
            if addition > 9:
                temp = str(addition)
                carry = int(temp[0])
                addition = int(temp[1])
            else:
                carry = 0
            new_node = ListNode(addition)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            value_l1 = l1.next if l1 else None
            value_l2 = l2.next if l2 else None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            new_node = ListNode(carry)
            tail.next = new_node
            tail = new_node

        return head


# @leet end
