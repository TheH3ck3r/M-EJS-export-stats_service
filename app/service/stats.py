import httpx
from ..models import stats


async def get_stats(journal_id: str) -> stats.Stats:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://mejs.api.adev-team.ru/attendance/v1/jobs/journal/{journal_id}/disciplines?with_students=1&with_disciplines=both")
        json = response.text

        return stats.Stats.parse_raw(json)


async def get_common_stats(journal_id: str) -> stats.CommonStats:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://mejs.api.adev-team.ru/attendance/v1/jobs/journal/{journal_id}/student/stats/discipline")
        json = response.text

        return stats.CommonStatsList.parse_raw(json).__root__


async def get_month_stats(journal_id: str) -> stats.MonthStats:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://mejs.api.adev-team.ru/attendance/v1/jobs/journal/{journal_id}/stats/months")
        json = response.text

        return stats.MonthStatsList.parse_raw(json).__root__
