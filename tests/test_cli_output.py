import sys


class RecordingStream:
    def __init__(self, encoding: str) -> None:
        self.encoding = encoding
        self.reconfigure_calls: list[dict[str, str]] = []

    def reconfigure(self, **kwargs: str) -> None:
        self.reconfigure_calls.append(kwargs)
        self.encoding = kwargs["encoding"]


def test_configure_output_encoding_uses_utf8_for_stdout_and_stderr(monkeypatch):
    stdout = RecordingStream("cp1252")
    stderr = RecordingStream("cp1252")
    monkeypatch.setattr(sys, "stdout", stdout)
    monkeypatch.setattr(sys, "stderr", stderr)

    from yasbd.cli import _configure_output_encoding

    _configure_output_encoding()

    assert stdout.encoding == "utf-8"
    assert stderr.encoding == "utf-8"
    assert stdout.reconfigure_calls == [{"encoding": "utf-8"}]
    assert stderr.reconfigure_calls == [{"encoding": "utf-8"}]
