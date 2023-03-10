from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import jsonify
from lib.cognito_token_verification import CognitoTokenVerification, TokenVerifyError

import os

from services.home_activities import *
from services.notifications_activities import *
from services.user_activities import *
from services.create_activity import *
from services.create_reply import *
from services.search_activities import *
from services.message_groups import *
from services.messages import *
from services.create_message import *
from services.show_activity import *

# Honeycomb io otel tracing.
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
# from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# XRay specific imports and stuff.
#from aws_xray_sdk.core import xray_recorder
#from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

# Watchtower specific imports.
import watchtower
import logging
from time import strftime

from auth_middleware import middleware

# Rollbar specific
#import rollbar
#import rollbar.contrib.flask
#from flask import got_request_exception

# Configuring Logger to Use CloudWatch
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
LOGGER.addHandler(console_handler)
LOGGER.addHandler(cw_handler)
LOGGER.info("some message")

# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
# consoleprocessor = SimpleSpanProcessor(ConsoleSpanExporter)
# provider.add_span_processor(consoleprocessor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

app = Flask(__name__)
app.wsgi_app = middleware(app.wsgi_app)
#app = middleware(app)

# Authentication via Flask_AWSCOGNITO
#aws_default_region = os.getenv("AWS_DEFAULT_REGION")
#user_pool_id = os.getenv("AWS_COGNITO_USER_POOL_ID")
#user_pool_client_id = os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID")

#aws_auth = CognitoTokenVerification(user_pool_id, user_pool_client_id, aws_default_region)

# Honeycomb
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

# X-Ray middleware initialisation.
#xray_url = os.getenv("AWS_XRAY_URL")
#xray_recorder.configure(service='backend-flask', dynamic_naming=xray_url)
#XRayMiddleware(app, xray_recorder)

# General
frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
origins = [frontend, backend]

#cors = CORS(
#  app, 
#  resources={r"/api/*": {"origins": origins}},
#  expose_headers="location,link",
#  allow_headers="content-type,if-modified-since",
#  methods="OPTIONS,GET,HEAD,POST"
#)

cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  headers=['Content-Type', 'Authorization'], 
  expose_headers='Authorization',
  methods="OPTIONS,GET,HEAD,POST"
)

# Watchtower logging after requests, especially for errors.
@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response

# Rollbar
#@app.before_first_request
#def init_rollbar():
#    """init rollbar module"""
#    rollbar.init(
#        # access token
#        os.getenv("ROLLBAR_ACCESS_TOKEN"),
#        # environment name
#        'production',
#        # server root directory, makes tracebacks prettier
#        root=os.path.dirname(os.path.realpath(__file__)),
#        # flask already sets up logging
#        allow_logging_basic_config=False)
#
#    # send exceptions from `app` to rollbar, using flask's signal system.
#    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

#@app.route("/rollbar/test")
#def rollbar_test():
#  rollbar.report_message('Hello World!','warning')
#  return "Hello World!"

# Normal stuff
@app.route("/api/message_groups", methods=['GET'])
def data_message_groups():
  user_handle  = 'andrewbrown'
  model = MessageGroups.run(user_handle=user_handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

@app.route("/api/messages/@<string:handle>", methods=['GET'])
def data_messages(handle):
  user_sender_handle = 'andrewbrown'
  user_receiver_handle = request.args.get('user_reciever_handle')

  model = Messages.run(user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/messages", methods=['POST','OPTIONS'])
@cross_origin()
def data_create_message():
  user_sender_handle = 'andrewbrown'
  user_receiver_handle = request.json['user_receiver_handle']
  message = request.json['message']

  model = CreateMessage.run(message=message,user_sender_handle=user_sender_handle,user_receiver_handle=user_receiver_handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/activities/home", methods=['GET'])
def data_home():
  #access_token = aws_auth.extract_access_token(request.headers)
  #try:
  #  app.logger.debug(access_token)
  #  aws_auth.verify(access_token)
  #  claims = aws_auth.claims
  #  app.logger.debug(claims)
    #user_info = aws_auth.get_user_info(access_token)
    #app.logger.debug(user_info)
    data = HomeActivities.run(username=claims['username'])
    return data, 200
  #except TokenVerifyError as e:
  #  app.logger.error(e);
  #  app.logger.error("Error authenticating");
  #  return "",401

@app.route("/api/activities/notifications", methods=['GET'])
def data_notifications():
  data = NotificationsActivities.run()
  return data, 200

@app.route("/api/activities/@<string:handle>", methods=['GET'])
def data_handle(handle):
  model = UserActivities.run(handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

@app.route("/api/activities/search", methods=['GET'])
def data_search():
  term = request.args.get('term')
  model = SearchActivities.run(term)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/activities", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities():
  user_handle  = 'andrewbrown'
  message = request.json['message']
  ttl = request.json['ttl']
  model = CreateActivity.run(message, user_handle, ttl)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
def data_show_activity(activity_uuid):
  data = ShowActivity.run(activity_uuid=activity_uuid)
  return data, 200

@app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities_reply(activity_uuid):
  user_handle  = 'andrewbrown'
  message = request.json['message']
  model = CreateReply.run(message, user_handle, activity_uuid)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

if __name__ == "__main__":
  app.run(debug=True)