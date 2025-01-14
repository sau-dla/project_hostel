{
    'name': "Hostel Management",
    'summary': "Manage your hostel in a simple way",
    'description': """
Efficient management of all residential facilities in the school.
""",
    'author': "sau",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '18.0',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'data/data.xml',
        'security/hostel_security.xml',
        'security/ir.model.access.csv',
        'views/hostel.xml',
        'views/hostel_room.xml',
        'views/hostel_room_category.xml',
        'views/hostel_student.xml',
        'views/hostel_amenities.xml',
        'views/hostel_category.xml',
        'views/hostel_book.xml',
        'views/hostel_room_members.xml',
        'views/assign_room_student_wizard.xml',
        'views/action.xml',
        'views/menu.xml',
    
    ],
    'demo': [
            'data/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'web/static/src/xml/**/*', 
            ],
    },
}