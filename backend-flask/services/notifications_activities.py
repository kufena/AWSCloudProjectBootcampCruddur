from datetime import datetime, timedelta, timezone
#from aws_xray_sdk.core import xray_recorder

class NotificationsActivities:
  def run():

    #with xray_recorder.in_segment("notification-activities") as segment:
    #  segment = xray_recorder.begin_subsegment("notification-activities")
    #  segment.put_metadata("silly-value", "Exeter the king maker!")
      now = datetime.now(timezone.utc).astimezone()
      results = [{
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Jimney Cricket',
        'message': 'I am a cricket.  And not very nice.',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 1,
        'reposts_count': 0,
        'replies': [{
          'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
          'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
          'handle':  'Worf',
          'message': 'This post has no honor!',
          'likes_count': 0,
          'replies_count': 0,
          'reposts_count': 0,
          'created_at': (now - timedelta(days=2)).isoformat()
        }],
      }
      ]
      #segment.close()
      return results