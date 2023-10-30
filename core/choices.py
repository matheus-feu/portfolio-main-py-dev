import json


def load_icons_data():
    with open('static/vendor/bootstrap-icons/bootstrap-icons.json') as json_file:
        data = json.load(json_file)
        return [(key, key) for key in data.keys()]


ICONS_CHOICES = load_icons_data()

STATES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BH', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espirito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RR', 'Roraima'),
    ('RO', 'Rondônia'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)
