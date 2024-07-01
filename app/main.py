from typing import Union
from fastapi import FastAPI
from .service import stats, excel, stats_storage
import uuid


app = FastAPI()


@app.get("/v1/stats/{journal_id}")
async def export_stats(journal_id: str):
    current_stats = await stats.get_stats(journal_id)
    common_stats = await stats.get_common_stats(journal_id)
    month_stats = await stats.get_month_stats(journal_id)
    file_name = await excel.export_stats(current_stats, common_stats, month_stats)

    file_link = await stats_storage.upload_file_to_s3(file_name)

    return {"file": file_link}
