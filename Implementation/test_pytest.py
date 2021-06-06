from main import Main
from profile import profile_data
from academics import academics_data
from cities import cities_data
from skills import skills_data
from hobbies import hobbies_data
user=Main()
# def test_console_data():
#     assert user.console_data()==1
def test_profile_data():
    assert profile_data(1,"nik.xlsx")==1
def test_academics_data():
    assert academics_data(1,"nik.xlsx")==1
def test_skills_data():
    assert skills_data(1,"nik.xlsx")==1
def test_hobbies_data():
    assert hobbies_data(1,"nik.xlsx")==1
def test_cities_data():
    assert cities_data(1,"nik.xlsx")==1