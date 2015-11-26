from kao_flask.kao_url import KaoUrl

SymbolListConcepts = KaoUrl('/api/admin/symbollists/<int:listId>/concepts')
SymbolListConcept = KaoUrl('/api/admin/symbollists/<int:listId>/concepts/<int:conceptId>')
WordListConcepts = KaoUrl('/api/admin/wordlists/<int:listId>/concepts')
WordListConcept = KaoUrl('/api/admin/wordlists/<int:listId>/concepts/<int:conceptId>')