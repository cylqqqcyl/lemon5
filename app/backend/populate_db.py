import json
from server import db, Voice, Attribute, app

def populate_database():
    with open('voices_data.json', 'r', encoding='utf-8') as file:
        voices_data = json.load(file)
    print(voices_data)
    for voice_data in voices_data:
        voice = Voice(name=voice_data['name'], avatar=voice_data['avatar'], audio=voice_data['audio'])
        db.session.add(voice)
        db.session.flush()  # This will assign an ID to voice without committing the transaction

        attr_data = voice_data['attributes']
        attribute = Attribute(
            element=attr_data['element'],
            style=attr_data['style'],
            voice_id=voice.id
        )
        db.session.add(attribute)

    db.session.commit()  # Commit all changes at once

if __name__ == '__main__':
    with app.app_context():
        populate_database()
