info = {'personal_data':
        {'name': 'Lauren',
        'age': 20,
        'major':'Information Science',
        'physical_features':
            {'color': {'eye':'blue',
                        'hair':'brown'},
            'height': '80kg'}
        },
        'other':
            {'favorite_colors': ['purple','green','blue'],
            'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
            }
        }

color = info['personal_data']['physical_features']['color'] #We just call the keys which represents the value that we want to extract
print(color)