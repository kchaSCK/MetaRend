# coding: utf-8

"""
    SAFRS Demo Application

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_usersstring_user_id2665(self):
        """Test case for delete_usersstring_user_id2665

        Delete a User object              # noqa: E501
        """
        pass

    def test_delete_usersstring_user_id_booksstring_book_id24aa(self):
        """Test case for delete_usersstring_user_id_booksstring_book_id24aa

        Delete from User books  # noqa: E501
        """
        pass

    def test_get_users_b2b8(self):
        """Test case for get_users_b2b8

        Retrieve a User object              # noqa: E501
        """
        pass

    def test_get_usersstring_user_id_books8b31(self):
        """Test case for get_usersstring_user_id_books8b31

        Retrieve a books object  # noqa: E501
        """
        pass

    def test_get_usersstring_user_id_booksstring_book_id9c49(self):
        """Test case for get_usersstring_user_id_booksstring_book_id9c49

        Retrieve a books object  # noqa: E501
        """
        pass

    def test_get_usersstring_user_id_c5e7(self):
        """Test case for get_usersstring_user_id_c5e7

        Retrieve a User object                          # noqa: E501
        """
        pass

    def test_patch_usersstring_user_id_c1d3(self):
        """Test case for patch_usersstring_user_id_c1d3

        Update a User object              # noqa: E501
        """
        pass

    def test_post_users1c2c(self):
        """Test case for post_users1c2c

        Create a User object              # noqa: E501
        """
        pass

    def test_post_users_get_list3413(self):
        """Test case for post_users_get_list3413

        Invoke User.get_list              # noqa: E501
        """
        pass

    def test_post_users_lookupd016(self):
        """Test case for post_users_lookupd016

        Invoke User.lookup              # noqa: E501
        """
        pass

    def test_post_usersstring_user_id_books0a50(self):
        """Test case for post_usersstring_user_id_books0a50

        Update books  # noqa: E501
        """
        pass

    def test_post_usersstring_user_id_cd56(self):
        """Test case for post_usersstring_user_id_cd56

        Create a User object                          # noqa: E501
        """
        pass

    def test_post_usersstring_user_id_send_mail5969(self):
        """Test case for post_usersstring_user_id_send_mail5969

        Invoke User.send_mail              # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
