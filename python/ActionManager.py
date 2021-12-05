# This class controls what functions get called from the

class ActionManager():
    def __init__(self, file, user_id, document_id, task_id):
        self.file = file
        self.user_id = user_id
        self.document_id = document_id
        self.task_id = task_id

        self.perfromAction()

    # Use function decoration here
    def perfromAction(self):
        print(
            f"Action Manager:\n\tFile:\t{self.file}\n\tUser:\t{self.user_id}\n\tDoc:\t{self.document_id}\n\tTask:\t{self.task_id}")
