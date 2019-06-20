import PyInquirer
import examples


def show_picker(options):

    config = {
        "type": "list",
        "qmark": "🐉 ⚔️ ",
        "message": "Select a choice",
        "name": "option",
    }

    config["choices"] = [{"name": option} for option in options]

    pick = PyInquirer.prompt([config], style=examples.custom_style_3)
    return pick["option"]
