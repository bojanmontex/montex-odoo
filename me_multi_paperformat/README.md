# ME Multi Paperformat

## Overview
ME Multi Paperformat is a technical module that enhances Odoo 16's report system to properly handle paperformats in multicompany environments. It ensures that reports use the correct paperformat based on the company of the record being printed, rather than always using the paperformat of the main company.

## Problem Solved
In standard Odoo, when using multicompany environments, reports often use the paperformat of the main company (usually company ID 1) regardless of which company the user is currently logged into or which company the record belongs to. This can lead to inconsistent report layouts and incorrect paper sizes.

## Features
- **Company-Aware Paperformat Selection**: Automatically selects the correct paperformat based on the company of the record being printed
- **URL-Based Detection**: Uses the URL path to extract record information when viewing reports directly
- **Document Layout Integration**: Checks for company-specific document layouts before falling back to company defaults
- **Fallback Mechanism**: If no specific paperformat can be determined, falls back to the standard company paperformat

## Technical Implementation
The module extends the `get_paperformat` method in `ir.actions.report` to:
1. First check if the report has a specific paperformat defined
2. Extract the record ID from the URL path when viewing a report directly
3. Find the company associated with that record
4. Use the document layout paperformat for that company if available
5. Fall back to the company's default paperformat if needed

## Important Notes
- **Company Context**: Always be aware of which company you are logged into when designing report templates
- **Document Layouts**: Configure document layouts for each company to ensure proper paperformat selection
- **Testing**: Test reports in different companies to ensure they use the correct paperformats

## Compatibility
- Odoo 16.0 Community and Enterprise editions

## License
This module is published under the LGPL-3 license.

## Support
For questions, please contact support at support@example.com