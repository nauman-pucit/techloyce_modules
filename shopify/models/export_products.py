import shopify

from odoo import models, fields, api
from openerp.osv import osv
from . import wizard


class ExportProduct(models.Model):
    _inherit = "product.template"

    def export_product(self):
        """
                This functions export products of the user to his shopify shop
                :return:
                """
        shop_name = self.env.user.shop_name
        api_key = self.env.user.api_key
        api_password = self.env.user.api_password
        api_secret_key = self.env.user.api_secret_key
        shop_url = "https://%s:%s@%s.myshopify.com/admin" % (api_key, api_password, shop_name)
        shopify.ShopifyResource.set_site(shop_url)
        shopify.Session.setup(api_key=api_key, secret=api_secret_key)
        exported_products = ""
        products = self.env['product.template'].search([('id', 'in', self.ids)])
        shopify_products = shopify.Product.find(limit=250)
        for product in products:
            already_exist = False
            for shopify_product in shopify_products:
                if shopify_product.attributes['title'] == product.name:
                    already_exist = True
                    break
            if already_exist:
                continue
            exported_products = exported_products + product.name + " "
            new_product = shopify.Product()
            new_product.title = product.name
            new_product.body_html = product.description
            new_product.product_type = product.type
            product_variant = shopify.Variant({"title": "v1", "price": 123123})
            new_product.variants = [product_variant]
            new_product.save()
        if exported_products:
            raise osv.except_osv(("Products Export Success"), (exported_products + " exported successfully"))
        else:
            raise osv.except_osv(("Products Export Message"), ("non product to export"))

