import os
import django
import mqtt
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_vue.settings")
django.setup()


def handlerGenerator(models):
    def handler(client, userdata, msg):
        data = msg.payload.decode('utf-8')
        data_json = json.loads(data)

        models.BadmintonInfo.objects.create(
            occupied=data_json["Occupied"],
            nums=data_json["Nums"],
        )

        print(data)

    return handler


if __name__ == "__main__":
    from app import models

    scope = "625639b8649b297b8f21729f"
    username = "62986aa5649b297b8f2172b7"
    password = "1234"

    sub = mqtt.IdeaSkyMQTTSubscriber(
        scope, username, password, handlerGenerator(models)
    )
    sub.run()