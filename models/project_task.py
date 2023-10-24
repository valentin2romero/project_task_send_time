from odoo import _, fields, models, api

class ProjectTask(models.Model):
    _inherit = "project.task"

    it_was_sent = fields.Boolean("It was sent?")
    sent_time = fields.Float("Sent Time")

    @api.onchange("effective_hours")
    def _onchange_effective_hours(self):
        if(self.it_was_sent):
            self.it_was_sent = False

    @api.onchange("it_was_sent")
    def _onchange_it_was_sent(self):
        if(self.it_was_sent):
            self.sent_time = self.effective_hours

    def clear_sent_time(self):
        self.sent_time = 0
