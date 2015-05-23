from Server import server

class FormsWrapper:
    """ Wrapper to handle properly loading the various concept forms """
    
    def __init__(self, forms, FormCls):
        """ Initialize the Forms Wrapper with the forms from the egg and the corresponding Model Class """
        self.eggForms = forms
        self.FormCls = FormCls
        self.conceptIdToForm = {}
        
    def load(self, concepts, languageWrapper):
        """ Load the forms """
        for eggForm in self.eggForms:
            if eggForm.conceptId not in self.conceptIdToForm:
                form = self.FormCls(text=eggForm.text, concept=concepts[eggForm.conceptId], language=languageWrapper.language)
                self.conceptIdToForm[eggForm.conceptId] = form
                server.db.session.add(form)
        
    def find(self):
        """ Find the existing forms """
        for eggForm in self.eggForms:
            form = self.FormCls.query.filter_by(text=eggForm.text).first()
            if form is not None:
                self.conceptIdToForm[eggForm.conceptId] = form
        return self.conceptIdToForm