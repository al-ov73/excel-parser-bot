import os
import pandas as pd

def format_sources_output(df: pd.DataFrame) -> str:
    result = []
    for _, row in df.iterrows():
        result.append(
            f"Название: {row['title']}\nurl: {row['url']}\nxpath: {row['xpath']}"
        )
    return "\n\n".join(result)

def validate_dataframe(df: pd.DataFrame):
    required_columns = {'title', 'url', 'xpath'}
    return required_columns.issubset(df.columns)

def format_sources(sources: list[tuple[str, str, str]]) -> str:
    return "\n\n".join(
        f"Название: {title}\nurl: {url}\nxpath: {xpath}"
        for title, url, xpath in sources
    )

def create_data_folder() -> None:
    os.makedirs("data/files", exist_ok=True)