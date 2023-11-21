from freezegun import freeze_time


def test_temp_service__add_record(date, temp_record, temp_service_class):
    with freeze_time(date):
        assert temp_record == temp_service_class.add_record(temp_record.value)


def test_temp_service__get_records_by_day(
    date,
    temp_record,
    temp_db_record,
    temp_service_class,
):
    assert [temp_record] == temp_service_class.get_records_by_day(date)
