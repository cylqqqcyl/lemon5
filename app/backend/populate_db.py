import json
from server import db, Voice, Attribute, app


def populate_database():
    with open('voices_data.json', 'r', encoding='utf-8') as file:
        voices_data = json.load(file)

    for voice_data in voices_data:
        # Check if a Voice with the same name already exists
        existing_voice = Voice.query.filter_by(name=voice_data['name']).first()

        if existing_voice:
            # Optional: Update existing record with new data
            existing_voice.avatar = voice_data['avatar']
            existing_voice.audio = voice_data['audio']

            voice = existing_voice
        else:
            # Create a new Voice instance if it doesn't exist
            voice = Voice(name=voice_data['name'], avatar=voice_data['avatar'], audio=voice_data['audio'], page=voice_data['page'])
            db.session.add(voice)

            db.session.flush()  # This will assign an ID to voice without committing the transaction

            attr_data = voice_data['attributes']
            # Assuming each Voice has unique attributes, or adjust accordingly
            attribute = Attribute(
                element=attr_data['element'],
                style=attr_data['style'],
                voice_id=voice.id
            )
            db.session.add(attribute)

    db.session.commit()  # Commit all changes at once

def remove_duplicate_attributes():
    voices = Voice.query.all()
    for voice in voices:
        unique_attributes = set()
        for attribute in voice.attributes:
            attr_key = (attribute.element, attribute.style)
            if attr_key in unique_attributes:
                db.session.delete(attribute)
            else:
                unique_attributes.add(attr_key)

    db.session.commit()

def show_all():
    voices = Voice.query.all()
    for voice in voices:
        print(voice.name)
        for attribute in voice.attributes:
            print(attribute.element, attribute.style)


if __name__ == '__main__':
    with app.app_context():
        populate_database()
