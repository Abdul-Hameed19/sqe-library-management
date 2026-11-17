import pytest
from src.gradebook import Roster, percentile


def test_percentile_with_empty_roster():
    roster = Roster()

    with pytest.raises(ValueError, match="Roster cannot be empty"):
        percentile(None, roster)