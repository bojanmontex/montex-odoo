from odoo import models
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def get_paperformat(self):
        # First check if paperformat is defined directly on the report
        if self.paperformat_id:
            return self.paperformat_id
        
        # Try to get company from document layout
        company_id = None
        
        # Try to get record and its company from the request
        try:
            if request and hasattr(request, 'httprequest'):
                url_path = request.httprequest.path
                if '/report/' in url_path:
                    # Format URL: /[lang]/report/[format]/[report_name]/[record_id]
                    path_parts = url_path.split('/')
                    if len(path_parts) > 1 and path_parts[-1].isdigit():
                        record_id = int(path_parts[-1])
                        model_name = self.model
                        
                        if model_name and record_id:
                            record = self.env[model_name].browse(record_id)
                            if hasattr(record, 'company_id') and record.company_id:
                                company_id = record.company_id.id
        except Exception as e:
            _logger.error("Error extracting company from URL: %s", e)
        
        # If we have a company_id, use document layout for that company
        if company_id:
            document_layout = self.env['base.document.layout'].sudo().search([('company_id', '=', company_id)], limit=1)
            if document_layout and document_layout.paperformat_id:
                return document_layout.paperformat_id
            
            # If no document layout paperformat, use company's paperformat
            company = self.env['res.company'].sudo().browse(company_id)
            return company.paperformat_id
        
        # Fallback to standard logic (company from environment)
        return self.env.company.paperformat_id