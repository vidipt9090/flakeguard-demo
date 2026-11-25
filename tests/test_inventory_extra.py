from inventory.report import Report


def test_report_title_is_stable():
    assert Report().title() == "Report"
