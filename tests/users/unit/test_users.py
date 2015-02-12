class TestUserController():

    """Docstring for TestUserController. """

    def test_get_users_without_filter(self, app_db, mock_user):
        """TODO: Docstring

        :returns: TODO

        """
        pass

    def test_get_users_by_id(self, app_db, mock_user):
        """TODO: Docstring for test_get_users_by_id.

        :app_db: TODO
        :mock_user: TODO
        :returns: TODO

        """
        pass

    def test_get_users_by_username(self, app_db, mock_user):
        """TODO: Docstring for test_get_users_by_username.

        :returns: TODO

        """
        pass

    def test_get_users_invalid_data(self):
        """TODO: Docstring for test_get_users_invalid_data.

        :returns: TODO

        """
        pass

    def test_create_user_invalid_username(self):
        """TODO: Docstring for test_create_user_invalid_username.

        :returns: TODO

        """
        pass

    def test_create_user_valid_username(self):
        """TODO: Docstring for test_create_user_valid_username.

        :returns: TODO

        """
        pass

    def test_create_user_too_short_password(self):
        """TODO: Docstring for test_create_user_too_short_password.

        :returns: TODO

        """
        pass

    def test_update_user_invalid_username(self):
        """TODO: Docstring for test_update_user_invalid_username.

        :returns: TODO

        """
        pass

    def test_update_user_valid_username(self, mock_user):
        """TODO: Docstring for test_update_user_valid_username.

        :returns: TODO

        """
        pass

    def test_delete_user_invalid_id(self):
        """TODO: Docstring for test_delete_user_invalid_id.

        :returns: TODO

        """
        pass

    def test_delete_user_valid_id(self, mock_user):
        """TODO: Docstring for test_delete_user_valid_id.

        :returns: TODO

        """
        pass
