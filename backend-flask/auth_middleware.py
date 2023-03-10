from werkzeug.wrappers import Request, Response, ResponseStream
from lib.cognito_token_verification import CognitoTokenVerification
from lib.cognito_token_verification import TokenVerifyError
import os

class middleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app
        self.userName = 'Tony'
        self.password = 'IamIronMan'

    aws_default_region = os.getenv("AWS_DEFAULT_REGION")
    user_pool_id = os.getenv("AWS_COGNITO_USER_POOL_ID")
    user_pool_client_id = os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID")
    logger = None
    aws_auth = CognitoTokenVerification(user_pool_id, user_pool_client_id, aws_default_region)

    def __call__(self, environ, start_response):
        request = Request(environ)
        self.logger.debug(request.headers)
        access_token = self.aws_auth.extract_access_token(request.headers)
        try:
            self.logger.debug(access_token)
            self.aws_auth.verify(access_token)
            claims = aws_auth.claims
            #app.logger.debug(claims)
            #user_info = aws_auth.get_user_info(access_token)
            #app.logger.debug(user_info)

            res = self.app(environ, start_response)
            return res
        
        except TokenVerifyError as e:
            self.logger.error(e);
            self.logger.error("Error authenticating");
            return Response(e, mimetype= 'text/plain', status=401)
            #return Response(u'Authorization failed', mimetype= 'text/plain', status=401)