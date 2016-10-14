from odoo import models, fields


class IdeaVote(models.Model):
    _name = 'idea.vote'
    _description = 'Daftar vote'

    idea_id = fields.Many2one('idea.idea', string='Idea', required=True)
    voter_id = fields.Many2one('res.partner', string='Voter',
                               help='orang yang memberikan vote terhadap Ide')
    date = fields.Date('Tanggal', default=fields.Date.context_today)
    score = fields.Float('Score')
    description = fields.Text('Description')
    is_member = fields.Boolean('Member')

    voter_name = fields.Char(related='voter_id.name')
    voter_street = fields.Char(related='voter_id.street')