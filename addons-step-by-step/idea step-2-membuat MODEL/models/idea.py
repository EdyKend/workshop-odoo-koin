from odoo import models, fields, api, _

class idea(models.Model):
    _name = 'idea.idea'

    name = fields.Char('Title', size=64, required=True, translate=True)
    state = fields.Selection([('draft', 'Draft'),
                              ( 'confirmed', 'Confirmed')], 'State', required= True, readonly=True,
                             default='draft')
    # Description is read-only when not draft!
    description = fields.Text('Description', states={'draft': [('readonly', False)]})
    active = fields.Boolean('Active', default=True)
    confirm_date = fields.Date('Confirm date')
    # by convention, many2one fields end with '_id'
    confirm_partner_id = fields.Many2one('res.partner', 'Confirm By')
    sponsor_ids = fields.Many2many('res.partner', 'idea_sponsor_rel', 'idea_id', 'sponsor_id', 'Sponsors')
    score = fields.Float('Score', digits=(6, 2))
    owner = fields.Many2one('res.partner', 'Owner', index=True)

    _sql_constraints = [('name_unik', 'unique(name)', _('Ideas must be unique!'))]
