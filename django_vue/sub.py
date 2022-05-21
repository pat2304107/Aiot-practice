import os
import django
import mqtt
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_tutorial_4x.settings")
django.setup()


def handlerGenerator(models):
    def handler(client, userdata, msg):
        data = msg.payload.decode('utf-8')
        data_json = json.loads(data)

        models.WeatherInfo.objects.create(
            temperature=data_json["Temperature"],
            time=data_json["Time"],
        )

        print(data)

    return handler


if __name__ == "__main__":
    from weather import models

    scope = "625639c4649b297b8f2172a0"
    username = "6284c047649b297b8f2172b2"
    password = "1234"

    sub = mqtt.IdeaSkyMQTTSubscriber(
        scope, username, password, handlerGenerator(models)
    )
    sub.run()