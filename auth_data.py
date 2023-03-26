
def user_info() -> list:
    response = []
    user_name = input('Username: ')
    pass_word = input('Password: ')
    hash_tag = input('Hashtag: ')
    response.append(user_name)
    response.append(pass_word)
    response.append(hash_tag)
    return response
