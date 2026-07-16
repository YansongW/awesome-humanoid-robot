"""Minify our own CSS/JS assets in dist/ after copying.

Vendored libraries under lib/ are already minified and are skipped. If the
minifier packages are unavailable the build silently keeps the originals.
"""

from __future__ import annotations

from pathlib import Path

try:
    import rcssmin
    import rjsmin

    _AVAILABLE = True
except ImportError:  # pragma: no cover - optional dependency
    _AVAILABLE = False


def minify_assets(dist_dir: Path) -> None:
    if not _AVAILABLE:
        return
    for css_path in (dist_dir / "css").glob("*.css"):
        text = css_path.read_text(encoding="utf-8")
        css_path.write_text(rcssmin.cssmin(text), encoding="utf-8")
    for js_path in (dist_dir / "js").glob("*.js"):
        text = js_path.read_text(encoding="utf-8")
        js_path.write_text(rjsmin.jsmin(text), encoding="utf-8")
