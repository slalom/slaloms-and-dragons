def generate():
    return [{'type': 'monster',
             'monster': {'name': 'Chupacabra',
                         'strength': 5}},


            {'type': 'trophy',
             'trophy': {'name': 'The Sword of Damocles',
                        'value': 10}},

            # non plyr char

            {'type': 'npc',
             'npc': {'name': 'mary',
                     'npc_class': 'human',
                     'greeting': 'Well hello there! My name is Mary. Can you help me??'}},

            {'type': 'mountain',
             'mountain': {'name': 'Zagros',
                          'greeting': 'You have arrived at Zagros mountain. The largest mountian in all of Kurdistan. Will you climb it?'}},

            {'type': 'cave',
             'cave': {'greeting': 'You have arrived at the deepest darkest cave, DEATH cave. Will you enter?'}}
            ]
