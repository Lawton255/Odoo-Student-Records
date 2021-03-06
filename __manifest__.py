# -*- coding: utf-8 -*-
{
    'name': "School",
    
    


    'summary': 'Record Student Information',

    'description': """
        Long description of module's purpose
    """,

    'author': "Emmanuel Lawton",
    'company': 'QuickCodes Tech',
    'website': "#",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #   'views/views.xml',
         # 'views/templates.xml',
        'views/student_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'image': ['static/school.jpeg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}