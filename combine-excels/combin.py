import pandas as pd
from pathlib import Path

excel_dir = Path('excel目录,如：E:/excel_files')

# files_xls = os.listdir(root)
excel_files = excel_dir.glob('*.xlsx')

df = pd.DataFrame()

for xls in excel_files:
    data = pd.read_excel(xls, 'sheet_name')
    df = df.append(data)

df.to_excel(excel_dir / "output.xlsx")
