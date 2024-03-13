import pytest
from smsactivate.api import SMSActivateAPI


API_KEY = 'TEST'
SERVICE_CODES = ['vk_0', 'ok_0', 'wa_0']
RUS_OPERATORS = ['megafon', 'mts', 'beeline']


@pytest.fixture(scope='function')
def sa():
    SA = SMSActivateAPI(API_KEY)
    SA.debug_mode = True
    return SA

@pytest.fixture
def sa_wrong_api_key():
    SA = SMSActivateAPI('WRONG_API_KEY')
    SA.debug_mode = True
    return SA


class TestGetNumbersStatus():

    @pytest.mark.xfail(reason='apy key needed')
    @pytest.mark.parametrize('code', SERVICE_CODES)
    @pytest.mark.parametrize('operator', RUS_OPERATORS)
    def test_status_services_ru(self, sa, code, operator):
        
        status = sa.getNumbersStatus(country=0, operator=operator)

        assert code in status, status['message']
        assert status[code] > 0, f'There is no available cell numbers for {code}'

    def test_status_services_ua(self):
        pass

    def test_status_services_kz(self):
        pass

    def test_status_services_without_operator(self):
        pass

    def test_status_services_without_country(self):
        pass

    def test_status_services_incorrect_operator(self):
        pass

    def test_status_services_incorrect_country(self):
        pass

    def test_status_services_wrong_api_key(self, sa_wrong_api_key):

        status = sa_wrong_api_key.getNumbersStatus(country=0, operator='beeline')

        assert 'error' in status, 'Wrong API key matched!'
