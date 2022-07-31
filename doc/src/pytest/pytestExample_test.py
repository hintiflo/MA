import pytest

'''	function under test '''
def mult( a, b ):
	result = a*b
	print("inside tested function: ", result)
	return result

'''	test-fixture '''
@pytest.fixture(scope="session", autouse=True)
def init_session(request):	
	print("before a session")
	request.addfinalizer(finalize_session)

def finalize_session():		print("after a session")

@pytest.fixture(scope="function", autouse=True)
def init_function(request):	
	print("before every case")
	request.addfinalizer(finalize_function)

def finalize_function():	print("after every case")

''' actual test cases: '''
def test_multStd():
	retval = mult(4,6)
	print("inside test-case : ", retval)
	assert 24 == retval

def test_multBig():
	assert 24000000000000 == mult(4e6,6e6)

def test_multSmall():
	assert 0.000000000024 == mult(4e-6,6e-6)

def test_multNegative():
	assert -24 == mult(-4,6)
