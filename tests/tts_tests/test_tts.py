import os
import unittest

from app.backend.tts import synthesize


class TTSTest(unittest.TestCase):
    def test_language(self):
        # check invalid language
        error_raised = False
        try:
            synthesize(text="lemon5를 이용해 주셔서 환영합니다", lang="kr")
        except ValueError:
            error_raised = True
        self.assertTrue(error_raised)

    def test_tts_japanese(self):
        # check output audio length
        audio = synthesize(text="レモンファイブへようこそ。", lang="ja")
        self.assertGreater(len(audio), 0)

    def test_tts_chinese(self):
        # TODO: waiting for implementation
        pass

    def test_tts_english(self):
        # TODO: waiting for implementation
        pass
