import uuid
from datetime import datetime, timedelta, timezone
from opentelemetry import trace
tracer = trace.get_tracer("create.reply")

class CreateReply:
  def run(message, user_handle, activity_uuid):
    model = {
      'errors': None,
      'data': None
    }

    if user_handle == None or len(user_handle) < 1:
      model['errors'] = ['user_handle_blank']

    if activity_uuid == None or len(activity_uuid) < 1:
      model['errors'] = ['activity_uuid_blank']

    if message == None or len(message) < 1:
      model['errors'] = ['message_blank'] 
    elif len(message) > 1024:
      model['errors'] = ['message_exceed_max_chars'] 

    if model['errors']:
      # return what we provided
      model['data'] = {
        'display_name': 'Andrew Brown',
        'handle':  user_sender_handle,
        'message': message,
        'reply_to_activity_uuid': activity_uuid
      }
    else:
      now = datetime.now(timezone.utc).astimezone()
      with tracer.start_as_current_span("http-handler") as outer_span:
        outer_span.set_attribute("outer", True)
        model['data'] = {
          'uuid': uuid.uuid4(),
          'display_name': 'Andrew Brown',
          'handle':  user_handle,
          'message': message,
          'created_at': now.isoformat(),
          'reply_to_activity_uuid': activity_uuid
        }

        span = trace.get_current_span()
        span.set_attribute("user.id", uuid.uuid4())
        span.set_attribute("message", message)
    return model