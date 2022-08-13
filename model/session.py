from model.oauth import Oauth
from utils.logger import logger


class Session:
    __token = None

    def __int__(self, oauth: Oauth):
        self.__token = self.refresh_token(oauth)
        Session.__token = self.__token
        # logger.info("token is {}".format(self.__token))

    def refresh_token(self, oauth: Oauth):
        pass

    def get_token(self):
        return self.__token
