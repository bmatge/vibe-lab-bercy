"""Tests d'intégration API — Viewer et export DOCX."""
import os


def test_view_doc(client):
    """Slug valide → 200, HTML contient du contenu."""
    resp = client.get('/docs/view/manifeste-vibe-lab')
    assert resp.status_code == 200
    assert b'Manifeste' in resp.data


def test_view_doc_not_found(client):
    """Slug inexistant → 404."""
    resp = client.get('/docs/view/document-inexistant-xyz')
    assert resp.status_code == 404


def test_view_doc_slug_sanitized(client):
    """Slug avec ../ → nettoyé et 404."""
    resp = client.get('/docs/view/../../etc/passwd')
    # Le regex [^a-z0-9_-] supprime les caractères dangereux
    assert resp.status_code in (404, 308)


def test_export_docx(client):
    """Slug valide → DOCX binaire valide."""
    resp = client.get('/docs/export/manifeste-vibe-lab.docx')
    assert resp.status_code == 200
    assert resp.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    # DOCX est un ZIP, les premiers bytes sont PK
    assert resp.data[:2] == b'PK'


def test_export_docx_not_found(client):
    """Slug inexistant → 404."""
    resp = client.get('/docs/export/document-inexistant-xyz.docx')
    assert resp.status_code == 404
