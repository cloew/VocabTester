from kao_flask.kao_url import KaoUrl

SymbolListConcepts = KaoUrl('/api/admin/symbollists/<int:listId>/concepts')
WordListConcepts = KaoUrl('/api/admin/wordlists/<int:listId>/concepts')