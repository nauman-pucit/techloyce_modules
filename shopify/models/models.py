# -*- coding: utf-8 -*-
import shopify
from odoo import fields, models, api, osv
from openerp.exceptions import ValidationError
from openerp.osv import osv


class CustomUser(models.Model):
    _inherit = 'res.users'

    # Add a new columns to the res.users model,
    @api.one
    def test_connectiom(self):
        # Generates a random name between 9 and 15 characters long and writes it to the record.
        shop_url = "https://%s:%s@%s.myshopify.com/admin" % (self.api_key, self.api_password,self.shop_name)
        shopify.ShopifyResource.set_site(shop_url)
        shopify.Session.setup(api_key=self.api_key, secret=self.api_secret_key)

        try:
            shop = shopify.Shop.current()
        except:
            raise ValidationError('Connection Failed >> invalid credentials')

        raise osv.except_osv(("Success!"), (" Connection Successful !"))

    shop_name = fields.Char(required=True)
    api_key = fields.Char(required=True)
    api_password = fields.Char(required=True)
    api_secret_key = fields.Char(required=True)