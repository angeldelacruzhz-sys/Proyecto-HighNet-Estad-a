from pathlib import Path
import sys

try:
    from xhtml2pdf import pisa
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Falta la dependencia xhtml2pdf. Instala con: python -m pip install xhtml2pdf"
    ) from exc

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "highnet-orquestador-catalogo-v1.2.html"
TARGET = ROOT / "highnet-orquestador-catalogo-v1.2.pdf"


def main() -> int:
    html = SOURCE.read_text(encoding="utf-8")
    with TARGET.open("wb") as pdf_file:
        result = pisa.CreatePDF(html, dest=pdf_file, path=str(ROOT))
    if result.err:
        print("La generación del PDF reportó errores.", file=sys.stderr)
        return 1
    print(f"PDF generado en: {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
