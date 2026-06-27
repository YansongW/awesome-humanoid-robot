"""FastAPI web frontend for the humanoid robot knowledge graph."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Form, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from web.kg_store import get_store
from web.llm_qa import answer

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="Humanoid Robot Knowledge Graph")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@app.on_event("startup")
def startup():
    get_store().load()


@app.get("/", response_class=HTMLResponse)
def index(request: Request, q: str = ""):
    store = get_store()
    results = store.search(q, top_k=50) if q.strip() else []
    all_entries = sorted(store.entries.values(), key=lambda e: e.name or e.id)
    domains = sorted({d for e in store.entries.values() for d in e.domains})
    types = sorted({e.type for e in store.entries.values()})
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "query": q,
            "results": results,
            "all_entries": all_entries,
            "domains": domains,
            "types": types,
        },
    )


@app.get("/entry/{entry_id}", response_class=HTMLResponse)
def entry_page(request: Request, entry_id: str):
    store = get_store()
    entry = store.get_entry(entry_id)
    if not entry:
        return templates.TemplateResponse(
            "not_found.html", {"request": request, "entry_id": entry_id}, status_code=404
        )
    outgoing = store.outgoing.get(entry_id, [])
    incoming = store.incoming.get(entry_id, [])
    related = store.related_entries(entry_id)
    return templates.TemplateResponse(
        "entry.html",
        {
            "request": request,
            "entry": entry,
            "outgoing": outgoing,
            "incoming": incoming,
            "related": related,
        },
    )


@app.get("/api/search")
def api_search(q: str = Query(..., min_length=1), top_k: int = 10):
    store = get_store()
    entries = store.search(q, top_k=top_k)
    return {
        "query": q,
        "count": len(entries),
        "results": [
            {
                "id": e.id,
                "name": e.name,
                "type": e.type,
                "summary": e.summary,
                "domains": e.domains,
            }
            for e in entries
        ],
    }


@app.get("/api/entry/{entry_id}")
def api_entry(entry_id: str):
    store = get_store()
    entry = store.get_entry(entry_id)
    if not entry:
        return JSONResponse({"error": "not found"}, status_code=404)
    return {
        "id": entry.id,
        "name": entry.name,
        "type": entry.type,
        "summary": entry.summary,
        "domains": entry.domains,
        "layers": entry.layers,
        "body_html": entry.body_html,
        "outgoing": [
            {"rel": r.type, "target_id": r.target_id, "target_name": r.target_name, "description": r.description}
            for r in store.outgoing.get(entry_id, [])
        ],
        "incoming": [
            {"rel": r.type, "source_id": r.source_id, "source_name": r.source_name, "description": r.description}
            for r in store.incoming.get(entry_id, [])
        ],
    }


@app.post("/api/ask")
def api_ask(question: str = Form(..., min_length=1)):
    return answer(question)
