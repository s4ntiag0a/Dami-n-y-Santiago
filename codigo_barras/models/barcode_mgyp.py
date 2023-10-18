from odoo import models, fields

class Barcode(models.Model):
    _name = 'barcode.barcode'
    _description = 'Códigos de Barras'

    name = fields.Char(string='Nombre del Producto', required=True)
    barcode = fields.Char(string='Código de Barras', required=True)
    state = fields.Selection([
        ('asignado', 'Asignado'),
        ('pendiente', 'Pendiente'),
        ('sin_asignar', 'Sin Asignar')],
        string='Estado', default='pendiente')
