import arrow
import acp_times as acp
import nose

"""
Test suite for brevet calculator. Might need to explicitly call it in terminal 'nosetests test_brevets.py'. I looked through
various stackoverflows and couldn't find a solution. Perhaps it is a local issue.
"""

def test_low_open_case():
	"""
	Checking a lower open value of the brevet open time calculator.
	"""
	assert(acp.open_time(120,200,"2017-01-01T00:00") == "2017-01-01T03:32:00+00:00")

def test_medium_open_case():
	"""
	Checking a medium open value case for the brevet open time calculator.
	"""
	assert(acp.open_time(150,200,"2017-01-01T00:00") == "2017-01-01T04:25:00+00:00")

def test_high_open_case():
	"""
	Checking a high open value case where the max brevet distance is equal to the control distance.
	"""
	assert(acp.open_time(200,200,"2017-01-01T00:00") == "2017-01-01T05:53:00+00:00")

def test_low_close_case():
	"""
	Checking a lower close value of the brevet close time calculator.
	"""
	assert(acp.close_time(120,200,"2017-01-01T00:00") == "2017-01-01T08:00:00+00:00")

def test_medium_close_case():
	"""
	Checking a medium close value of the brevet close time calculator.
	"""
	assert(acp.close_time(150,200,"2017-01-01T00:00") == "2017-01-01T10:00:00+00:00")

def test_high_close_case():
	"""
	Checking a high close value case where the max brevet distance is equal to the control distance.
	"""
	assert(acp.close_time(200,200,"2017-01-01T00:00") == "2017-01-01T13:30:00+00:00")

def test_overflow_close_case():
	"""
	Checking a value between 100-110% of the max brevet distance to see if it calculates the max time properly.
	"""
	assert(acp.close_time(205,200,"2017-01-01T00:00") == "2017-01-01T13:30:00+00:00")

def test_medium_open_diff_dist():
	"""
	Checking a medium open time with a different brevet distance.
	"""
	assert(acp.open_time(200,400,"2017-01-01T00:00") == "2017-01-01T05:53:00+00:00")
