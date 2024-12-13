import pytest
from askbosco_client import AskBosco


class TestAskBosco:
    def test_class_instantiates_correctly(self):
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        assert test_bosco.client_code == "cl13ntc0d3"
        assert test_bosco.display_name == "test_display_name"
        assert test_bosco.owner == "test_owner"
        assert test_bosco.settings == {"is_active": False, "focus": "ecommerce"}
        assert test_bosco.engine_list == []


class TestGetClientCode:
    def test_get_client_code_accepts_only_strings(self):
        expected_error_message = "invalid data type: client_code must be a string"
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco(True, "test_display_name", "test_owner", "ecommerce")
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco(123, "test_display_name", "test_owner", "ecommerce")
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco(["cl13ntc0d3"], "test_display_name", "test_owner", "ecommerce")

    def test_get_client_code_accepts_only_alphanumeric_strings(self):
        expected_error_message = "client_code must be an alphanumeric URL safe value that cannot start with a number or underscore"
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("cl13ntc0d3!", "test_display_name", "test_owner", "ecommerce")
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("cl13nt_c0d3", "test_display_name", "test_owner", "ecommerce")
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("cl13nt'c0d3!'", "test_display_name", "test_owner", "ecommerce")

    def test_get_client_rejects_url_unsafe_characters(self):
        expected_error_message = "client_code must be an alphanumeric URL safe value that cannot start with a number or underscore"
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("cl13nt/c0d3", "test_display_name", "test_owner", "ecommerce")
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("cl13ntc0d3&more", "test_display_name", "test_owner", "ecommerce")

    def test_get_client_code_rejects_num_or_underscore_as_first_char(self):
        expected_error_message = "client_code must be an alphanumeric URL safe value that cannot start with a number or underscore"
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("0cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("_cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")

    def test_client_initialises_successfully_with_approriate_client_code(self):
        AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")


class TestStringCheck:
    def test_string_check_rejects_non_string_inputs(self):
        with pytest.raises(Exception, match="invalid data type: display_name must be a string"):
            AskBosco("cl13ntc0d3", False, "test_owner", "ecommerce")
        with pytest.raises(Exception, match="invalid data type: owner must be a string"):
            AskBosco("cl13ntc0d3", "test_display_name", 5432, "ecommerce")

    def test_string_check_accepts_strings(self):
        AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")


class TestGetFocus:
    def test_get_focus_rejects_non_string_inputs(self):
        expected_error_message = "invalid data type: focus must be a string"
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("cl13ntc0d3", "test_display_name", "test_owner", 567)
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("cl13ntc0d3","test_display_name","test_owner",["lead_generation" or "ecommerce"])

    def test_get_focus_rejects_strings_that_are_not_valid_focuses(self):
        expected_error_message = "invalid client focus, must be 'lead_generation' or 'ecommerce'"
        with pytest.raises(Exception, match=expected_error_message):
            AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "making_money")

    def test_get_focus_accepts_correct_focusses(self):
        AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "lead_generation")
        AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")


class TestPauseAndUnpause:
    def test_client_initiates_paused(self):
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        assert test_bosco.settings["is_active"] == False

    def test_client_can_be_unpauses(self):
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        test_bosco.start_client()
        assert test_bosco.settings["is_active"] == True

    def test_client_can_be_paused(self):
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        test_bosco.start_client()
        assert test_bosco.settings["is_active"] == True
        test_bosco.pause_client()
        assert test_bosco.settings["is_active"] == False


class TestEngineMethods:
    def test_add_engine_adds_engine_sucessfully(self):
        """add_engine works regardless of the type of the engine, so the test
        can use anything as an input"""
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        test_bosco.add_engine("engine_0")
        assert test_bosco.engine_list == ["engine_0"]

    def test_add_engine_can_be_called_repeatedly(self):
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        test_bosco.add_engine("engine_0")
        test_bosco.add_engine("engine_1")
        test_bosco.add_engine("engine_2")
        assert test_bosco.engine_list == ["engine_0", "engine_1", "engine_2"]

    def test_remove_enigine_can_remove_engine_sucessfully(self):
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        test_bosco.add_engine("engine_0")
        assert test_bosco.engine_list == ["engine_0"]
        test_bosco.remove_engine_by_index(0)
        assert test_bosco.engine_list == []

    def test_list_engines_returns_correctly(self):
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        test_bosco.add_engine("engine_0")
        test_bosco.add_engine("engine_1")
        test_bosco.add_engine("engine_2")
        assert test_bosco.list_engines() == ["engine_0", "engine_1", "engine_2"]


class TestGetState:
    def test_get_state_returns_correct_state_string(self):
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")
        assert test_bosco.get_state() == """client_code: cl13ntc0d3
display_name: test_display_name
owner: test_owner
focus: ecommerce
is_active: False
engine_count: 0"""

    def test_get_state_accurately_reflects_changing_state(self):
        test_bosco = AskBosco("cl13ntc0d3", "test_display_name", "test_owner", "ecommerce")

        test_bosco.start_client()
        test_bosco.add_engine("engine_0")
        test_bosco.add_engine("engine_1")
        test_bosco.add_engine("engine_2")
        test_bosco.remove_engine_by_index(1)

        assert test_bosco.get_state() == """client_code: cl13ntc0d3
display_name: test_display_name
owner: test_owner
focus: ecommerce
is_active: True
engine_count: 2
engine_list: ['engine_0', 'engine_2']"""
