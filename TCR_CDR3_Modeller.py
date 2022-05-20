#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 16:18:11 2021

@author: zrollins
"""

# Comparative modeling by the AutoModel class
#
# Demonstrates how to build multi-chain models
#
from modeller import *
from modeller.automodel import *    # Load the AutoModel class

log.verbose()

class MyModel(AutoModel):
    def special_patches(self, aln):
        # Rename both chains and renumber the residues in each
        self.rename_segments(segment_ids=['A', 'B','C','D','E'],
                             renumber_residues=[1, 1])
        # Another way to label individual chains:
        self.chains[0].name = 'A'
        self.chains[1].name = 'B'
        self.chains[2].name = 'C'
        self.chains[3].name = 'D'
        self.chains[4].name = 'E'


env = Environ()
# directories for input atom files
env.io.atom_files_directory = ['.', '/Users/zrollins/Documents/Documents/AI_Patent/CEA/TCR000002/']

# Be sure to use 'MyModel' rather than 'AutoModel' here!
a = MyModel(env,
            alnfile  = 'align.ali' ,     # alignment filename
            knowns   = '3qdj',              # codes of the templates
            sequence = 'tcr000002')              # code of the target

a.starting_model= 1                # index of the first model
a.ending_model  = 10                # index of the last model
                                   # (determines how many models to calculate)
a.make()                           # do comparative modeling
