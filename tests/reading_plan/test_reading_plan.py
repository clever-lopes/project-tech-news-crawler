import pytest

from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501


def test_reading_plan_group_news():
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)
