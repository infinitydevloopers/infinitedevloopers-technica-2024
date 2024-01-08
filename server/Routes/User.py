from Controller.user import urls
from . import user

user.add_url_rule('/user','user_greeting',urls.hello_user_dev,methods=['GET'])
