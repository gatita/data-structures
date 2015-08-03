# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
import random


@pytest.fixture
def normal_list():
    return [random.randit(0, 100) for i in range(15)
