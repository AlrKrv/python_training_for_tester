# -*- coding: utf-8 -*-
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroyed)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(name="dfgh", header="dfgh", footer="dfgh")
    app.log_out()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(name="", header="", footer="")
    app.log_out()
