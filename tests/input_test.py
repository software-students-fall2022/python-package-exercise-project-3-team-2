import pytest
from thisday import ProcessInput

class tests:
    def test_input():
        assert ProcessInput("film-tv")=="film-tv","film-tv doesn't run correctly"
        assert ProcessInput("history")=="history","history doesn't run correctly"
        assert ProcessInput("sport")=="sport","sport doesn't run correctly"
        assert ProcessInput("music")=="music","music doesn't run correctly"
        assert ProcessInput("foo")==0,"other cases doesn't run correctly"