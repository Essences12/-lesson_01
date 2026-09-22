import pytest
from string_utils import StringUtils


class TestStringUtils:

    # ---------- capitalize ----------

    def test_capitalize_positive(self):
        utils = StringUtils()
        assert utils.capitalize("skypro") == "Skypro"

    def test_capitalize_empty_string(self):
        utils = StringUtils()
        assert utils.capitalize("") == ""

    def test_capitalize_none(self):
        utils = StringUtils()
        with pytest.raises(AttributeError):
            utils.capitalize(None)

    # ---------- trim ----------

    def test_trim_positive(self):
        utils = StringUtils()
        assert utils.trim("   skypro") == "skypro"

    def test_trim_no_spaces(self):
        utils = StringUtils()
        assert utils.trim("skypro") == "skypro"

    def test_trim_none(self):
        utils = StringUtils()
        with pytest.raises(AttributeError):
            utils.trim(None)

    # ---------- contains ----------

    def test_contains_positive(self):
        utils = StringUtils()
        assert utils.contains("SkyPro", "S") is True

    def test_contains_symbol_absent(self):
        utils = StringUtils()
        assert utils.contains("SkyPro", "U") is False

    def test_contains_empty_string(self):
        utils = StringUtils()
        assert utils.contains("", "a") is False

    def test_delete_symbol_positive(self):
        utils = StringUtils()
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_substring(self):
        utils = StringUtils()
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_not_found(self):
        utils = StringUtils()
        assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"