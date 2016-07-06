from kao_command import Commands

commands = Commands(__name__, {'import': {None:'import_cmd.ImportCmd',
                                          'ambiguity':'import_ambiguity_cmd.ImportAmbiguityCmd'},  
                               'seed': 'seed.Seed'})