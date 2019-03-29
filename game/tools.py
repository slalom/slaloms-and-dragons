import PyInquirer
import examples


def show_picker(options):

    config = {
        'type': 'list',
        'qmark': '🐉 ⚔️ ',
        'message': 'Select a choice',
        'name': 'option'
    }

    config['choices'] = options

    return PyInquirer.prompt([config], style=examples.custom_style_3)
