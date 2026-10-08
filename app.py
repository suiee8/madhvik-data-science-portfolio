import os
from pathlib import Path

from fastapi.responses import FileResponse
from nicegui import app, ui

ROOT = Path(__file__).resolve().parent

app.add_static_files('/css', ROOT / 'css')
app.add_static_files('/js', ROOT / 'js')


@app.get('/', include_in_schema=False)
async def portfolio() -> FileResponse:
    return FileResponse(ROOT / 'index.html', media_type='text/html')


if __name__ == '__main__':
    ui.run(
        title='Madhvik Rashmin Panchal – Data Scientist',
        host='0.0.0.0',
        port=int(os.environ.get('PORT', '8080')),
        reload=False,
        show=False,
    )
