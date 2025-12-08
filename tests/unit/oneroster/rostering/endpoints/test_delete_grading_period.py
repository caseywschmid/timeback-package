from timeback.services.oneroster.rostering.endpoints.delete_grading_period import delete_grading_period


class MockHttp:
    def __init__(self):
        self.last_path = None

    def delete(self, path):
        self.last_path = path
        return None


def test_delete_grading_period_success():
    mock_http = MockHttp()
    result = delete_grading_period(mock_http, "gp-001")
    assert result is None
    assert "/ims/oneroster/rostering/v1p2/gradingPeriods/gp-001" in mock_http.last_path

