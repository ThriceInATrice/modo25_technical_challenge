class AskBosco:
    """this class serves as a client for ASKBOSCO. it accepts only strings as arguments.
    the client initiates in paused mode and must be manually unpaused using the
    start_client method"""

    def __init__(self, client_code, display_name, owner, focus):
        self.client_code = self.get_client_code(client_code)
        self.display_name = self.string_check(display_name, "display_name")
        self.owner = self.string_check(owner, "owner")
        self.settings = {
            "is_active": False,
            "focus": self.get_focus(focus),
        }
        self.engine_list = []

    def get_client_code(self, client_code):
        """this method checks the client code to match the following requirements:
        - alphanumeric
        - url safe
        - does not start with a number or underscore
        it is assumed that by accepting only alphanumeric characters, no url-unsafe
        characters can be included"""
        if isinstance(client_code, str):
            if client_code.isalnum() and not client_code[0].isnumeric():
                return client_code
            else:
                raise Exception("client_code must be an alphanumeric URL safe value that cannot start with a number or underscore")
        else:
            raise Exception("invalid data type: client_code must be a string")

    def string_check(self, value, field):
        """this method serves to makes sure that fields like display_name are strings
        and raises an objection with an informative message if they are not"""
        if isinstance(value, str):
            return value
        else:
            raise Exception(f"invalid data type: {field} must be a string")

    def get_focus(self, focus):
        """this method makes sure that the focus argument is of an appropraite form.
        it first checks if the argument is a string, and returns an appropriate
        exception if not. then it checks if the string matches a valid focus for the
        client and returns a different exception if not."""
        if isinstance(focus, str):
            if focus in ["lead_generation", "ecommerce"]:
                return focus
            else:
                raise Exception("invalid client focus, must be 'lead_generation' or 'ecommerce'")
        else:
            raise Exception("invalid data type: focus must be a string")

    def start_client(self):
        "this method activates the client"
        self.settings["is_active"] = True

    def pause_client(self):
        "this method pauses the client"
        self.settings["is_active"] = False

    def add_engine(self, engine):
        """this method adds an engine to the client's list of engines"""
        self.engine_list.append(engine)

    def remove_engine_by_index(self, engine_index):
        """this method removes the engine at the specific index in the clients engine list.
        this method was chosen in the absence of any knowledge about the engine class.
        it is advised to use list_engines() to locate the engine you wish to remove"""
        self.engine_list.pop(engine_index)

    def list_engines(self):
        """this method returns a list of the engines. with more detail on the properties of
        an engine, the method might have more functionality, such as listing ids or statuses
        """
        return self.engine_list

    def get_state(self):
        """this method returns a string detailing the current state of the client.
        it has a conditional string that lists the engines, if any are present"""
        status_strings = [
            f"client_code: {self.client_code}",
            f"display_name: {self.display_name}",
            f"owner: {self.owner}",
            f"focus: {self.settings['focus']}",
            f"is_active: {self.settings['is_active']}",
            f"engine_count: {len(self.engine_list)}",
        ]
        if len(self.engine_list):
            status_strings.append(f"engine_list: {self.engine_list}")

        return "\n".join(status_strings)
