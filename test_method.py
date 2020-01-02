import pytest

iplist=[1,2,3,4,5]

@pytest.mark.parametrize('ip', iplist)
def test_hi(ip):
	assert ip==4 
	print('im',ip)

