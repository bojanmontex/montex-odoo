{
    'name': 'ME Multi Paperformat',
    'version': '16.0.1.0.0',
    'category': 'Technical',
    'summary': 'Enhanced paperformat selection for multicompany environments',
    'description': """
ME Multi Paperformat
====================
This module enhances the paperformat selection logic in Odoo reports to properly handle multicompany environments.

Key features:
- Automatically selects the correct paperformat based on the company of the record being printed
- Works for both inline viewing and downloading of reports
- Respects the company hierarchy and layout settings

Technical details:
- Extends the get_paperformat method in ir.actions.report
- Uses the URL path to extract record information when viewing reports directly
- Falls back to standard company paperformat if no specific one is found
""",
    'author': 'Bojan Mijuskovic, Montex-Elektronika',
    'website': 'https://www.montexel.com',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}