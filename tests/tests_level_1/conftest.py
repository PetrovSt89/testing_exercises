import datetime
import pytest
import dataclasses

@dataclasses.dataclass(frozen=True, kw_only=True)
class Gender:
    male: str
    female: str


@pytest.fixture
def gender_fix():
    return Gender(male="муж", female="жен")

@pytest.fixture
def date_now():
    return datetime.datetime.now()

@pytest.fixture
def loc_host():
    return "http://127.0.0.1:5000"
    