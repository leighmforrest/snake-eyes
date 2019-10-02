import re

from flask import url_for


class TestPage:
    def test_home_page(self, client):
        """Home page should respond with a success 200."""
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """Terms page should respond with a success 200."""
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """Privacy page should respond with a success 200."""
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_faq_page(self, client):
        """FAQ page should respond with a success 200."""
        response = client.get(url_for('page.faq'))
        assert response.status_code == 200

    def test_faq_page_title_tag(self, client):
        response = client.get(url_for('page.faq'))
        assert '<title>' in str(response.data)

    def test_faq_title_tag_open_and_close(self, client):
        regex = "<title>(.*?)</title>"
        response = client.get(url_for('page.faq'))
        assert re.search(regex, str(response.data)) is not None
