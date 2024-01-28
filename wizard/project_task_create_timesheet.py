from odoo import _, models

class ProjectTaskCreateTimesheet(models.TransientModel):
    _inherit = 'project.task.create.timesheet'

    def save_timesheet(self):
        res = super(ProjectTaskCreateTimesheet, self).save_timesheet()
        if res:
            self.task_id.write({
                'it_was_sent': False
            })
        return res
