{
    'name' : 'Gestion Comptable',
    'author' : 'Telia Informatique',
    'version' : "1.0",
    'depends' : ['base','erp_budget'],
    'description' : 'Gestion de la comptabilit√©',
    'summary' : "Gestion de la Comptabilit√©",
    'data' : ['security/compta_security.xml','views/typec.xml', 'views/compta.xml', 'views/report_compta.xml', 'data/compta_data.xml', 'security/ir.model.access.csv',],
    'installable' : True,
    'auto_install' : False,
}
