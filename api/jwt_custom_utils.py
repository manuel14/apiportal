def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.

    Example:

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }

    """
    # Se agregan pk de usuario y staff flag a la respuesta de jwt_create_token
    return {
        'token': token,
        'userid': user.id,
        "staff": user.is_staff
    }