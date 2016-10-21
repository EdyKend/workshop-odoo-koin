from odoo import http           #http merupakan suatu module/object besar dimana didalamnya diimplementasikan HTTP Layer
from odoo.http import request   #request merupakan suatu module/object untuk Request Handle yg telah diperkaya dengan ENV odoo
from odoo.addons.website.models.website import unslug
import datetime
# from odoo.tools.translate import _

class WebsiteIdea(http.Controller):

    # website = True : module dedicate to building website  (styly, theme, assets,
    # snippet, inline editor, SEO Tools, etc)

    @http.route(["/idea"], type="http", auth="public", website=True)
    def idea(self, succes=0):
        domain = []
        idea_obj = request.env['idea.idea'].search(domain)
        values = {
            'idea_data': idea_obj,
            'title': 'Idea : My First Website',
            'success': succes,
        }
        return request.render('website_idea.index', values)

    @http.route(['/idea/<idea_id>'], type='http', auth='public', website=True)
    def vote(self, idea_id):
        _title, _id = unslug(idea_id)
        idea_obj = request.env['idea.idea'].sudo().browse(_id)
        values = {
            'idea_data': idea_obj,
        }
        return request.render('website_idea.vote', values)

    @http.route(['/vote/update'], type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def vote_update(self, **post):
        # idea_obj = request.env['idea.idea'].sudo().browse(post['id'])
        value = {
            'idea_id': post['id'],
            'date': datetime.datetime.today(),
            'score': post['score'],
            'is_member': False,
        }
        vote = request.env['idea.vote'].sudo().create(value)
        return request.redirect("/idea?succes=1")

