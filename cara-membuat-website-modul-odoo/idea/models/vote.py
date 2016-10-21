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


# BELAJAR ORM Function - CRUD
    def cara_search(self):
        idea_obj = self.env['res.partner'].search([('name', 'ilike', 'edy')])
        if idea_obj:
            idea_obj[0].name = 'Edy Kend'

    def cara_create(self):
        res = self.create(
            {'name': 'Spam recipe',
             'description': 'spam & eggs',
             'owner': 45,
             })

    def cara_create(self):
        vals = {'name':'Edy',
                'street': 'Jl. Manyar'}

        res = self.env['res.partner'].create(vals)

    def cara_update_data_TIDAK_disarankan(self):
        idea_obj = self.env['res.partner'].search([('name', 'ilike', 'edy')])
        if idea_obj:
            idea_obj[0].name = 'Edy Kend'
            idea_obj[0].street = 'Jalan.....'
            idea_obj[0].city = 'Surabaya'

    def cara_update_data_yg_BENAR(self):
        idea_obj = self.env['res.partner'].search([('name', 'ilike', 'edy')])
        if idea_obj:
            idea_obj.write({
                'name': 'Edy Kend',
                'street': 'Jalan.....',
                'city': 'Surabaya'
            })

