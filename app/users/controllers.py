from . import models


class UserController():

    """:TODO: Docstring for User. """

    def user_to_json(self, user):
        """TODO: Docstring for to_json.

        :user: TODO
        :returns: TODO

        """
        return {
            'id': str(user.id),
            'username': user.username
        }

    def get_user(self, query_filter):
        """Get user by filters. The filters should be attributes of the
        User model.

        :query_filter: A dict with User's attr and a valid value.
        :returns: a iterable object with User objects or None.

        """
        invalid_keys = list(filter(
            lambda key: key not in models.User.get_fields_list(), query_filter
        ))

        if any(invalid_keys):
            return {
                'error': 'The keys "{}" are not valid User attributes'.format(
                    invalid_keys
                )
            }

        user = models.User.objects(**query_filter).first()

        if not user:
            return {'no-data': 'No Content'}
        else:
            return {'success': self.user_to_json(user)}
