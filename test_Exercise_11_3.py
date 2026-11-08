import pytest
from employee import Employee

@pytest.fixture
def employee():
    return Employee('budi', 'santoso', 65000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.gaji_tahunan == 70000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.gaji_tahunan == 75000